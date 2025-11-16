import torch
import numpy as np

print(np.random.randn(5))
np.random.seed(7)
print(np.random.randn(5))

randseed1 = np.random.RandomState(777)
randseed2 = np.random.RandomState(77)

print(randseed1.randn(5))
print(randseed2.randn(5))

#####################################
print(torch.randn(5))
torch.manual_seed(77)
print(torch.randn(5))
print(torch.randn(3, 3))