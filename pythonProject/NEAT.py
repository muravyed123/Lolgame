import torch
a = set({(torch.tensor(1), torch.tensor(2))})
print(a)
a.add((torch.tensor(1), torch.tensor(2)))
print(a)
