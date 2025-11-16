import numpy as np
import torch

n = np.array([[1, 2, 3]])
#print(n.T, n.T.T)
#print(np.transpose(n))

t = torch.tensor([[1,2,3]])
#print(t.T, t.T.T)
#print(torch.transpose(t,0,1))
#####################################
# entropy
x = [.25, .75] # prob of x is .25 => and prob of not x 1 - 0.25
H=0

for p in x:
    H -= p * np.log(p)

print("entropy {}".format(H))

#####################################
# this formula use for: Binary cross-entropy loss function? search..
p = [1, 0]
q = [.25, .75]

H = 0
for i in range(len(p)):
    H -= p[i] * np.log(q[i]) # => when p is 1 and 0 then => H = -np.log(q[0])

print("cross entropy {}".format(H))
####################################

import torch.nn.functional as F

q_tensor = torch.Tensor(q)
p_tensor = torch.Tensor(p)

print("torch cross entropy {}".format(F.binary_cross_entropy(q_tensor, p_tensor))) # q first

n = np.array([1, 2 ,3 ,4 , 3, 2, 1])
print("argmin: {}   min: {}".format(np.argmin(n), np.min(n)))
print("argmax: {}   max: {}".format(np.argmax(n), np.max(n)))
print()
print()

n = np.array([[1, 2 ,3], [4 , 3, 2], [1, 3 ,7]])

print("argmin: {}   min: {}".format(np.argmin(n), np.min(n)))
print("argmin: {}   min: {}".format(np.argmin(n, axis=0), np.min(n, axis=0))) # min of each col (across rows)
print("argmin: {}   min: {}".format(np.argmin(n, axis=1), np.min(n, axis=1)))  # min of each row (across cols)
print("----------------------------------------------------------------")
n = torch.tensor([[1, 2 ,3], [4 , 3, 2], [1, 3 ,7]])

print("argmin: {}   min: {}".format(torch.argmin(n), torch.min(n)))
print("----------------------------------------------------------------")
print("argmin: {}   min: {}".format(torch.argmin(n, axis=0), torch.min(n, axis=0))) # min of each col (across rows)
print("----------------------------------------------------------------")
print("argmin: {}   min: {}".format(torch.argmin(n, axis=1), torch.min(n, axis=1)))  # min of each row (across cols)
print("#####")
returned_val = torch.min(n, axis=0)
print(type(returned_val), returned_val.values)