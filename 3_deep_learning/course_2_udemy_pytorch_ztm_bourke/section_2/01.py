import torch
#a = torch.tensor([7, 7])
#b = torch.tensor([7])
#c = torch.tensor([[7, 7], [7, 7]])

#print(a.ndim, a.size(), a.shape)
#print(b.ndim, b.size(), b.shape)
#print(c.ndim, c.size(), c.shape, c[1])

scalar = torch.tensor(7)
print(scalar, scalar.ndim)
vector = torch.tensor([1, 2])
MAT = torch.tensor([[1, 2],
                    [3, 4]])
TENSOR = torch.tensor([[[1, 2],
                        [3, 4]],
                        [[5, 6],
                         [7, 8]]])

print(TENSOR.ndim)
rand_tensor = torch.rand(3, 4)
rand_img = torch.rand(3, 224, 224) #ch, h, w
print(rand_tensor)
rand_tensor2 = torch.rand(size=(2, 3))
print(rand_tensor2)

zeros = torch.zeros(size=(2, 3))
ones = torch.ones(size=(2, 3), dtype=torch.int32)
print(zeros * rand_tensor2)
print(ones)