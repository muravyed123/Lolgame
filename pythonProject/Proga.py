import numpy as np
import random

import torch
from torch import nn
import json
import math
from torch.functional import F

import gymnasium as gym

from tqdm import tqdm
AUTO_TRAIN = True

GAMMA = 0.99
EPS_START = 0.9
EPS_END = 0.05
EPS_DECAY = 1000
BATCH_SIZE = 100
TAU = 0.005
LR = 0.0001

mean_ac = 0

device = torch.device(
    "cuda" if torch.cuda.is_available() else
    "mps" if torch.backends.mps.is_available() else
    "cpu"
)
count = 0
sum_lens = 0

def analyse(moves, how_played):
    global count, sum_lens, mean_ac
    win = (len(moves)+int(how_played)) % 2
    los = 1 - win
    data = [0]*10
    data[-1] = moves[0]*3/8
    data[moves[0]] += 1
    for i in range(1, len(moves)-1):
        action = moves[i]
        state = np.array(data) / 3
        if i == 0:
            continue
        if i % 2 == 0:
            model1.memory.push(tuple(state // 0.1 / 10), action)  # insert experience into memory
        elif i % 2 == 1:
            model2.memory.push(tuple(state // 0.1 / 10), action)  # insert experience into memory
        data[moves[i]] += (i % 2 + 1)
        data[-1] = moves[i] * 3 / 8
    action = moves[len(moves)-1]
    state = np.array(data) / 3

    count += 1
    mean_ac = round(sum_lens / count, 3)
    sum_lens += len(moves) - int(how_played)
    if count == 100 and AUTO_TRAIN:
        loss1 = dqn_training(model1)
        loss2 = dqn_training(model2)
        print('len is ', sum_lens / 100, 'loss is', loss1, loss2)
    if count == 100:
        sum_lens = 0
        count = 1


class DQNetworkModel(nn.Module):
    def __init__(self, in_channels, out_classes):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(in_channels, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.Sigmoid(),
            nn.Linear(128, out_classes),
        )
        self.optimizer = torch.optim.AdamW(self.parameters(), lr=LR)
        self.memory = ReplayMemory(10000)

    def forward(self, x):
        return self.layers(x)


class ReplayMemory(object):

    def __init__(self, capacity):
        self.memory = set()

    def push(self, *args):
        """Save a transition"""
        self.memory.add(args)

    def sample(self, batch_size):
        mem = list(self.memory)
        random.shuffle(mem)
        bs = []
        for i in range(len(mem)//batch_size):
            bs.append(mem[i:i+batch_size])

        return bs

    def __len__(self):
        return len(self.memory)


steps_done = 0


def select_action(state, model):
    global steps_done
    sample = random.random()
    eps_threshold = EPS_END + (EPS_START - EPS_END) * \
                    math.exp(-1. * steps_done / EPS_DECAY)
    steps_done += 1
    if sample > eps_threshold:
        with torch.no_grad():
            return torch.argmax(model(state))
    else:
        return torch.tensor(random.randint(0, 8), device=device, dtype=torch.long)


def new_model():
    name = 'model'

    model_1 = DQNetworkModel(10, 9).to(device)
    model_2 = DQNetworkModel(10, 9).to(device)

    if 0:
        model_1.load_state_dict(torch.load(name + '1'))
        model_2.load_state_dict(torch.load(name + '2'))

    return model_1, model_2


def save_model(name):
    torch.save(model1.state_dict(), name + '1')
    torch.save(model2.state_dict(), name + '2')


def save_data(name):
    with open(name+'1.json', 'w') as f:
        json.dump(tuple(model1.memory.memory), f)
    with open(name+'2.json', 'w') as f:
        json.dump(tuple(model2.memory.memory), f)


def load_model(name):
    l_model1 = torch.load(name + '1')
    l_model2 = torch.load(name + '2')
    return l_model1, l_model2


def load_data(name):
    with open(name + '1.json') as json_file:
        arr = json.load(json_file)
        for i in arr:
            model1.memory.push(tuple(i[0]), i[1])
    with open(name + '2.json') as json_file:
        arr = json.load(json_file)
        for i in arr:
            model2.memory.push(tuple(i[0]), i[1])
def dqn_training(
    model,
        epochs=25
):
    memory = model.memory
    optimizer = model.optimizer
    if len(memory) < BATCH_SIZE:
        return None
    loss = []
    criterion = nn.CrossEntropyLoss()
    model.train()
    for i in range(epochs):
        transitions = memory.sample(BATCH_SIZE)
        for batch in transitions:

            state_batch = torch.zeros((BATCH_SIZE, 10))
            action_batch = torch.LongTensor([0]*(BATCH_SIZE))
            for i in range(len(batch)):
                state_batch[i] = torch.tensor(batch[i][0])
                action_batch[i] = int(batch[i][1])

            X = state_batch
            y = action_batch

            # model forward-pass

            preds = model(X)

            # model backward-pass
            optimizer.zero_grad()  # t.grad = torch.tensor([0., 0., 0.])
            loss1 = criterion(preds, y)
            loss1.backward()
            optimizer.step()
            loss1 += loss1.detach()
            loss.append(loss1)

            # save loss and accuracy
    model.eval()
    return loss[-1]

def make_move(Data, last, number):
    global nodes
    data = np.array([0]*10)
    for i in range(len(Data)):
        data[i] = Data[i]/3
    if last == -1:
        last = 1
    data[-1] = last/8
    X = torch.tensor(data).float()
    with torch.no_grad():
        if number % 2 == 0:
            preds = select_action(X//0.1*10, model1)  # select action based on epsilon greedy policy

        else:
            preds = select_action(X//0.1*10, model2)  # select action based on epsilon greedy policy
    return int(preds)


model1, model2 = new_model()
if 1:
    load_data('data')
