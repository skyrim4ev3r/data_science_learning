import torch
print(torch.range(start=1,end=10, dtype=torch.int16))
print(torch.arange(start=1,end=10, dtype=torch.int16))
r = torch.arange(start=1, end=5)
print(torch.zeros_like(input=r))

x = torch.rand(size=(1, 3), dtype=None) # None will be default f32

print(x, x.dtype)
torch.rand(size=(3, 3), dtype=None, device=None, requires_grad=False) #default "cpu" change to -> "cuda"

x_f16 = x.type(torch.float16)

print(x_f16, x_f16)
print(torch.rand(size=(1, 3), dtype=None, device="cuda", requires_grad=False))
print(x.device, x.dtype, x.shape, x.size())