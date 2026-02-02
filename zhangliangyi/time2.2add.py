In[2]: x.requires_grad_(True)  # 等价于x=torch.arange(4.0, requires_grad=True)
x.grad  # 默认值是None

In [3]: y=2*torch.dot(x,x)
y
Out[3]: tensor(28.grad_fn=<MulBackward0>)

