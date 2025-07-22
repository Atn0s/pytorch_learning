# -*- coding: utf-8 -*-

"""
PyTorch RNN/LSTM 教程
本脚本演示如何构建一个 LSTM 模型用于序列到一的预测任务。
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
import numpy as np

# 1. 定义 LSTM 模型
class AdvancedLSTM(nn.Module):
    """一个用于序列预测的 LSTM 模型。"""
    def __init__(self, input_size, hidden_size, num_layers, output_size, dropout_prob=0.5):
        super(AdvancedLSTM, self).__init__()
        # 使用 LSTM，它比标准 RNN 更擅长捕捉长期依赖
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers,
                            batch_first=True, # 输入和输出张量以 (batch, seq, feature) 形式提供
                            bidirectional=True) # 双向 LSTM
        self.dropout = nn.Dropout(dropout_prob)
        # 因为是双向 LSTM，所以全连接层的输入维度是 hidden_size 的两倍
        self.fc = nn.Linear(hidden_size * 2, output_size)

    def forward(self, x):
        # LSTM 返回输出、隐藏状态和细胞状态
        out, (h_n, c_n) = self.lstm(x)
        # 我们使用最后一个时间步的输出进行预测
        out = self.dropout(out[:, -1, :])
        out = self.fc(out)
        return out

def create_dataset(n_samples=1000, seq_length=20):
    """为正弦波预测任务创建一个虚拟数据集。"""
    X, y = [], []
    for _ in range(n_samples):
        start = np.random.rand() * 10
        time_steps = np.linspace(start, start + 5, seq_length + 1)
        sequence = np.sin(time_steps)
        X.append(sequence[:-1])
        y.append(sequence[-1])
    # 将数据转换为张量并增加一个维度
    return torch.tensor(np.array(X), dtype=torch.float32).unsqueeze(-1), torch.tensor(np.array(y), dtype=torch.float32).unsqueeze(-1)

def main():
    """主函数，用于训练和测试 LSTM。"""
    print("--- PyTorch LSTM 教程 ---")

    # 超参数
    input_size = 1
    hidden_size = 128
    num_layers = 2
    output_size = 1
    seq_length = 20
    learning_rate = 0.001
    num_epochs = 10
    batch_size = 64

    # 2. 创建数据集和数据加载器
    X_train, y_train = create_dataset(n_samples=5000, seq_length=seq_length)
    train_dataset = TensorDataset(X_train, y_train)
    train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)

    # 3. 模型、损失函数和优化器
    model = AdvancedLSTM(input_size, hidden_size, num_layers, output_size)
    criterion = nn.MSELoss() # 均方误差损失，适用于回归任务
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    print("\n模型结构:")
    print(model)

    # 4. 训练循环
    print("\n开始训练...")
    for epoch in range(num_epochs):
        model.train()
        for i, (sequences, labels) in enumerate(train_loader):
            outputs = model(sequences)
            loss = criterion(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        print(f'周期 [{epoch+1}/{num_epochs}], 损失: {loss.item():.4f}')

    # 5. 推理
    print("\n进行预测...")
    model.eval()
    with torch.no_grad():
        X_test, y_test = create_dataset(n_samples=1, seq_length=seq_length)
        prediction = model(X_test)
        print(f"输入序列 (后5个): {...X_test.squeeze().numpy()[-5:]}")
        print(f"实际下一个值: {y_test.item():.4f}")
        print(f"预测的下一个值: {prediction.item():.4f}")

if __name__ == "__main__":
    main()
