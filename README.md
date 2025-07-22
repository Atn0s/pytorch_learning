# Python & PyTorch 深度学习完整学习路径 🐍🔥

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-red)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Atn0s/pytorch_learning)](https://github.com/Atn0s/pytorch_learning)

欢迎来到Python和PyTorch深度学习的学习之旅！本项目为您提供了一个系统性的学习路径，从Python基础到深度学习应用。

> **⭐ 如果这个项目对您有帮助，请给个星标支持！**

## 📚 学习路径

### 阶段1: Python基础
- **目标**: 掌握Python编程基础
- **内容**: 
  - 变量、数据类型、运算符 (`01_python_basics/variables_and_types.py`)
  - 控制结构 (`01_python_basics/control_structures.py`)

### 阶段2: 数据科学基础
- **目标**: 学会数据处理和可视化
- **内容**:
  - NumPy：数值计算 (`02_data_science/numpy_tutorial.py`)
  - Pandas：数据处理 (`02_data_science/pandas_tutorial.py`)
  - Matplotlib：数据可视化 (`02_data_science/matplotlib_tutorial.py`)

### 阶段3: PyTorch基础
- **目标**: 掌握PyTorch深度学习框架
- **内容**:
  - Tensor操作 (`03_pytorch_basics/tensor_operations.py`)
  - 自动求导机制 (`03_pytorch_basics/autograd_tutorial.py`)
  - 神经网络构建 (`03_pytorch_basics/neural_network_basics.py`)

### 阶段4: 深度学习进阶
- **目标**: 理解和实现各种深度学习模型
- **内容**:
  - 卷积神经网络(CNN) (`04_deep_learning/cnn_tutorial.py`)
  - 循环神经网络(RNN) (`04_deep_learning/rnn_tutorial.py`)

### 阶段5: 实战项目
- **目标**: 通过实际项目巩固知识
- **项目**:
  - 图像分类 (`05_projects/image_classification/train_cifar10.py`)
  - 情感分析 (`05_projects/nlp_sentiment/sentiment_analysis.py`)

## 🗂️ 项目结构

```
.
├── 01_python_basics/
│   ├── variables_and_types.py
│   └── control_structures.py
├── 02_data_science/
│   ├── numpy_tutorial.py
│   ├── pandas_tutorial.py
│   └── matplotlib_tutorial.py
├── 03_pytorch_basics/
│   ├── tensor_operations.py
│   ├── autograd_tutorial.py
│   └── neural_network_basics.py
├── 04_deep_learning/
│   ├── cnn_tutorial.py
│   └── rnn_tutorial.py
├── 05_projects/
│   ├── image_classification/
│   │   └── train_cifar10.py
│   └── nlp_sentiment/
│       └── sentiment_analysis.py
├── notebooks/
│   └── python_pytorch_learning_guide.ipynb
└── requirements.txt
```

## 🚀 快速开始

### 1. 环境配置
```bash
# 创建虚拟环境（推荐）
python -m venv venv
# Windows:
venv\\Scripts\\activate
# Mac/Linux:
# source venv/bin/activate

# 安装必要的包
pip install -r requirements.txt
```

### 2. 开始学习
1. 从 `notebooks/python_pytorch_learning_guide.ipynb` 开始，它提供了所有主题的交互式概述。
2. 深入研究每个目录中的Python脚本以获取更详细的示例。
3. 尝试运行和修改 `05_projects/` 中的实战项目。

## 🤝 贡献

欢迎贡献！如果您发现任何错误或有改进建议，请提交一个Pull Request。

## 📝 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。
