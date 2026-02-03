#库导入与环境设置
matplotlib inline
import torch
import torchvision
from torch.utils import data
from torchvision import transforms
from d21 import torch as d21
d21.use_svg_display()


数据加载相关代码
# 批量大小设置
batch_size = 256

# 定义数据读取进程数
def get_dataloader_workers():
    """使用4个进程来读取的数据。"""
    return 4

# 构建训练数据迭代器
train_iter = data.DataLoader(mnist_train, batch_size, shuffle=True, num_workers=get_dataloader_workers())

# 计时统计数据读取耗时
timer = d21.Timer()
for X, y in train_iter:
    continue
f'{timer.stop():.2f}sec'  # 输出耗时结果

模型参数初始化:
# 输入维度（图像展平后长度）、输出维度（类别数）
num_inputs = 784
num_outputs = 10

# 权重W：正态分布初始化（均值0，标准差0.01），需计算梯度
W = torch.normal(0, 0.01, size=(num_inputs, num_outputs), requires_grad=True)
# 偏置b：初始化为0，需计算梯度
b = torch.zeros(num_outputs, requires_grad=True)


矩阵求和示例代码
# 定义示例矩阵
X = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
# 按维度求和（0：行维度求和→行向量；1：列维度求和→列向量）
X.sum(0, keepdim=True), X.sum(1, keepdim=True)

 网络模型定义
def net(X):
    # 图像展平后矩阵乘法 + 偏置，再通过softmax激活
    return softmax(torch.matmul(X.reshape((-1, W.shape[0])), W) + b)

交叉熵损失函数实现
def cross_entropy(y_hat, y):
    # 交叉熵损失计算（取预测概率的对数再取负）
    return -torch.log(y_hat[range(len(y_hat)), y])

# 示例调用（假设y_hat为预测值，y为真实标签）
cross_entropy(y_hat, y)


 准确率评估相关代码
# 累加器类：用于统计正确预测数和总预测数
class Accumulator:
    """在n个变量上累加。"""
    def __init__(self, n):
        self.data = [0.0] * n
    
    def add(self, *args):
        self.data = [a + float(b) for a, b in zip(self.data, args)]
    
    def reset(self):
        self.data = [0.0] * len(self.data)  # 修正原文不完整的reset方法
    
    def __getitem__(self, idx):
        return self.data[idx]

# 评估模型在测试集上的准确率
evaluate_accuracy(net, test_iter)

感知机训练代码（含伪代码与损失函数）
# 初始化参数
w = 0
b = 0

# 迭代训练
repeat:
    if y * (w · xi + b) ≤ 0:  # 分类错误时更新参数
        w ← w + yi · xi
        b ← b + yi
until all samples are classified correctly

# 感知机损失函数定义
def感知机损失函数 e(y, x, w):
    return max(0, -y * (torch.matmul(w, x) + b))  # 对应原文e(y,x,w)=max(0,-y(w,x))







