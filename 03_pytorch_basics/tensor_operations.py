"""
PyTorch基础教程 - Tensor操作

学习目标：
1. 理解什么是Tensor（张量）
2. 掌握Tensor的创建和基本操作
3. 学会Tensor的数学运算
4. 了解GPU加速的基本使用
"""

import torch
import numpy as np

print("PyTorch版本:", torch.__version__)
print("CUDA是否可用:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("CUDA版本:", torch.version.cuda)
    print("GPU设备数量:", torch.cuda.device_count())

# ============================================================================
# 1. 什么是Tensor？
# ============================================================================

print(f"\n=== 什么是Tensor？ ===")
print("""
Tensor（张量）是PyTorch中的核心数据结构，类似于NumPy的数组，但有以下优势：
1. 可以在GPU上运行，实现并行计算
2. 支持自动微分（自动求导）
3. 为深度学习优化

张量的维度：
- 0维张量：标量 (scalar)
- 1维张量：向量 (vector)
- 2维张量：矩阵 (matrix)
- 3维及以上：多维张量
""")

# ============================================================================
# 2. 创建Tensor
# ============================================================================

print(f"\n=== 创建Tensor ===")

# 2.1 从Python列表创建
list_1d = [1, 2, 3, 4, 5]
tensor_1d = torch.tensor(list_1d)
print(f"从列表创建1维张量: {tensor_1d}")
print(f"形状: {tensor_1d.shape}, 数据类型: {tensor_1d.dtype}")

list_2d = [[1, 2, 3], [4, 5, 6]]
tensor_2d = torch.tensor(list_2d)
print(f"从嵌套列表创建2维张量:\n{tensor_2d}")
print(f"形状: {tensor_2d.shape}")

# 2.2 从NumPy数组创建
np_array = np.array([1.0, 2.0, 3.0, 4.0])
tensor_from_numpy = torch.from_numpy(np_array)
print(f"从NumPy数组创建: {tensor_from_numpy}")

# 2.3 使用特殊函数创建
zeros_tensor = torch.zeros(3, 4)  # 3x4的零张量
ones_tensor = torch.ones(2, 3)    # 2x3的全1张量
random_tensor = torch.randn(2, 2) # 2x2的随机张量（标准正态分布）
identity_tensor = torch.eye(3)    # 3x3的单位矩阵

print(f"\n零张量 (3x4):\n{zeros_tensor}")
print(f"全1张量 (2x3):\n{ones_tensor}")
print(f"随机张量 (2x2):\n{random_tensor}")
print(f"单位矩阵 (3x3):\n{identity_tensor}")

# 2.4 指定数据类型和设备
float_tensor = torch.tensor([1, 2, 3], dtype=torch.float32)
long_tensor = torch.tensor([1, 2, 3], dtype=torch.long)

print(f"\n浮点数张量: {float_tensor}, 类型: {float_tensor.dtype}")
print(f"长整型张量: {long_tensor}, 类型: {long_tensor.dtype}")

# 2.5 创建序列张量
range_tensor = torch.arange(0, 10, 2)  # 从0到10，步长为2
linspace_tensor = torch.linspace(0, 1, 5)  # 从0到1，均匀分成5个点

print(f"范围张量: {range_tensor}")
print(f"线性空间张量: {linspace_tensor}")

# ============================================================================
# 3. Tensor的属性
# ============================================================================

print(f"\n=== Tensor的属性 ===")

sample_tensor = torch.randn(3, 4, 5)
print(f"张量: 形状{sample_tensor.shape}")
print(f"维度数量: {sample_tensor.ndim}")
print(f"元素总数: {sample_tensor.numel()}")
print(f"数据类型: {sample_tensor.dtype}")
print(f"设备: {sample_tensor.device}")
print(f"内存布局: {sample_tensor.layout}")

# ============================================================================
# 4. Tensor索引和切片
# ============================================================================

print(f"\n=== Tensor索引和切片 ===")

# 创建示例张量
matrix = torch.tensor([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print(f"原始矩阵:\n{matrix}")

# 基本索引
print(f"第1行: {matrix[0]}")
print(f"第2列: {matrix[:, 1]}")
print(f"第2行第3列的元素: {matrix[1, 2]}")

# 切片操作
print(f"前2行: \n{matrix[:2]}")
print(f"后2列: \n{matrix[:, 2:]}")
print(f"中间2x2区域: \n{matrix[1:3, 1:3]}")

# 高级索引
indices = torch.tensor([0, 2])
print(f"选择第1和第3行: \n{matrix[indices]}")

# 布尔索引
mask = matrix > 6
print(f"大于6的元素: {matrix[mask]}")

# ============================================================================
# 5. Tensor形状操作
# ============================================================================

print(f"\n=== Tensor形状操作 ===")

original = torch.arange(12)
print(f"原始张量: {original}")

# reshape：改变形状
reshaped = original.reshape(3, 4)
print(f"reshape为3x4:\n{reshaped}")

# view：改变视图（共享内存）
viewed = original.view(2, 6)
print(f"view为2x6:\n{viewed}")

# transpose：转置
transposed = reshaped.transpose(0, 1)  # 交换维度0和1
print(f"转置后:\n{transposed}")

# squeeze：去除大小为1的维度
squeezed = torch.tensor([[[1, 2, 3]]]).squeeze()
print(f"squeeze前形状: {torch.tensor([[[1, 2, 3]]]).shape}")
print(f"squeeze后: {squeezed}, 形状: {squeezed.shape}")

# unsqueeze：增加维度
unsqueezed = squeezed.unsqueeze(0)
print(f"unsqueeze后: {unsqueezed}, 形状: {unsqueezed.shape}")

# flatten：展平
flattened = reshaped.flatten()
print(f"展平后: {flattened}")

# ============================================================================
# 6. Tensor数学运算
# ============================================================================

print(f"\n=== Tensor数学运算 ===")

# 创建示例张量
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])
matrix_a = torch.randn(2, 3)
matrix_b = torch.randn(3, 2)

print(f"张量a: {a}")
print(f"张量b: {b}")

# 基本运算
print(f"加法 a + b: {a + b}")
print(f"减法 a - b: {a - b}")
print(f"乘法 a * b: {a * b}")
print(f"除法 a / b: {a / b}")
print(f"幂运算 a ** 2: {a ** 2}")

# 矩阵运算
print(f"\n矩阵A (2x3):\n{matrix_a}")
print(f"矩阵B (3x2):\n{matrix_b}")
print(f"矩阵乘法 A @ B:\n{torch.matmul(matrix_a, matrix_b)}")

# 聚合运算
data = torch.randn(3, 4)
print(f"\n数据矩阵:\n{data}")
print(f"求和: {torch.sum(data)}")
print(f"按行求和: {torch.sum(data, dim=0)}")
print(f"按列求和: {torch.sum(data, dim=1)}")
print(f"平均值: {torch.mean(data)}")
print(f"最大值: {torch.max(data)}")
print(f"最小值: {torch.min(data)}")
print(f"标准差: {torch.std(data)}")

# ============================================================================
# 7. 广播机制
# ============================================================================

print(f"\n=== 广播机制 ===")

# 广播允许不同形状的张量进行运算
scalar = 10
vector = torch.tensor([1, 2, 3])
matrix = torch.tensor([[1, 2, 3], [4, 5, 6]])

print(f"标量: {scalar}")
print(f"向量: {vector}")
print(f"矩阵:\n{matrix}")

print(f"标量 + 向量: {scalar + vector}")
print(f"向量 + 矩阵:\n{vector + matrix}")

# 不同形状的矩阵运算
a = torch.randn(3, 1)
b = torch.randn(1, 4)
print(f"\nA形状: {a.shape}, B形状: {b.shape}")
print(f"A + B的形状: {(a + b).shape}")

# ============================================================================
# 8. GPU加速（如果可用）
# ============================================================================

print(f"\n=== GPU加速 ===")

if torch.cuda.is_available():
    print("CUDA可用，演示GPU操作:")
    
    # 创建CPU张量
    cpu_tensor = torch.randn(1000, 1000)
    print(f"CPU张量设备: {cpu_tensor.device}")
    
    # 移动到GPU
    gpu_tensor = cpu_tensor.cuda()  # 或者 cpu_tensor.to('cuda')
    print(f"GPU张量设备: {gpu_tensor.device}")
    
    # 在GPU上进行运算
    gpu_result = torch.matmul(gpu_tensor, gpu_tensor)
    print(f"GPU计算结果形状: {gpu_result.shape}")
    
    # 移回CPU
    cpu_result = gpu_result.cpu()
    print(f"结果移回CPU: {cpu_result.device}")
    
else:
    print("CUDA不可用，使用CPU进行计算")
    
    # 演示CPU上的操作
    large_tensor = torch.randn(1000, 1000)
    result = torch.matmul(large_tensor, large_tensor)
    print(f"CPU计算完成，结果形状: {result.shape}")

# ============================================================================
# 9. 实际应用示例
# ============================================================================

def image_processing_example():
    """图像处理示例"""
    print(f"\n=== 图像处理示例 ===")
    
    # 模拟一个RGB图像 (3通道, 32x32像素)
    image = torch.randn(3, 32, 32)
    print(f"原始图像形状: {image.shape} (通道, 高, 宽)")
    
    # 批处理：添加批次维度
    batch_images = image.unsqueeze(0)  # 添加批次维度
    print(f"批处理图像形状: {batch_images.shape} (批次, 通道, 高, 宽)")
    
    # 图像归一化
    normalized = (image - image.mean()) / image.std()
    print(f"归一化后的统计信息:")
    print(f"  均值: {normalized.mean():.4f}")
    print(f"  标准差: {normalized.std():.4f}")
    
    # 图像翻转
    flipped = torch.flip(image, dims=[2])  # 水平翻转
    print(f"翻转后图像形状: {flipped.shape}")
    
    # 通道转换：从CHW到HWC
    hwc_image = image.permute(1, 2, 0)
    print(f"HWC格式图像形状: {hwc_image.shape} (高, 宽, 通道)")

def linear_regression_data():
    """线性回归数据生成示例"""
    print(f"\n=== 线性回归数据生成 ===")
    
    # 生成训练数据
    n_samples = 100
    x = torch.linspace(-1, 1, n_samples).unsqueeze(1)  # 输入特征
    true_w = 2.0  # 真实权重
    true_b = 1.0  # 真实偏置
    noise = torch.randn(n_samples, 1) * 0.1  # 噪声
    
    y = true_w * x + true_b + noise  # 目标值
    
    print(f"输入X形状: {x.shape}")
    print(f"目标Y形状: {y.shape}")
    print(f"前5个样本:")
    for i in range(5):
        print(f"  x={x[i].item():.2f}, y={y[i].item():.2f}")
    
    # 数据统计
    print(f"X的范围: [{x.min():.2f}, {x.max():.2f}]")
    print(f"Y的均值: {y.mean():.2f}, 标准差: {y.std():.2f}")
    
    return x, y

# ============================================================================
# 10. 练习题
# ============================================================================

def practice_exercises():
    """练习题"""
    print(f"\n=== 练习题 ===")
    
    # 练习1: 创建和操作张量
    print("练习1: 张量基本操作")
    
    # TODO: 创建一个5x5的随机矩阵
    matrix = torch.randn(5, 5)
    print(f"5x5随机矩阵:\n{matrix}")
    
    # TODO: 计算矩阵的行和列的平均值
    row_means = torch.mean(matrix, dim=1)
    col_means = torch.mean(matrix, dim=0)
    print(f"行平均值: {row_means}")
    print(f"列平均值: {col_means}")
    
    # 练习2: 矩阵运算
    print("\n练习2: 矩阵运算")
    
    A = torch.randn(3, 4)
    B = torch.randn(4, 2)
    
    # TODO: 计算A和B的矩阵乘法
    C = torch.matmul(A, B)
    print(f"A形状: {A.shape}, B形状: {B.shape}")
    print(f"C = A @ B, 形状: {C.shape}")
    
    # 练习3: 张量形状变换
    print("\n练习3: 形状变换")
    
    # TODO: 创建一个1维张量，然后reshape为不同形状
    vector = torch.arange(24)
    print(f"原始向量: {vector}")
    
    matrix_2x12 = vector.reshape(2, 12)
    matrix_3x8 = vector.reshape(3, 8)
    matrix_4x6 = vector.reshape(4, 6)
    
    print(f"2x12矩阵:\n{matrix_2x12}")
    print(f"3x8矩阵:\n{matrix_3x8}")
    print(f"4x6矩阵:\n{matrix_4x6}")
    
    # 练习4: 统计运算
    print("\n练习4: 统计运算")
    
    data = torch.randn(100)
    
    # TODO: 计算基本统计量
    stats = {
        "均值": torch.mean(data).item(),
        "中位数": torch.median(data).item(),
        "标准差": torch.std(data).item(),
        "最大值": torch.max(data).item(),
        "最小值": torch.min(data).item()
    }
    
    print("100个随机数的统计信息:")
    for key, value in stats.items():
        print(f"  {key}: {value:.4f}")

if __name__ == "__main__":
    image_processing_example()
    x, y = linear_regression_data()
    practice_exercises()

# ============================================================================
# 学习总结
# ============================================================================
"""
🎓 学习总结：

1. Tensor基础:
   - Tensor是PyTorch的核心数据结构
   - 支持GPU加速和自动微分
   - 类似NumPy数组但功能更强大

2. 创建Tensor:
   - torch.tensor(): 从数据创建
   - torch.zeros(), torch.ones(): 特殊值
   - torch.randn(): 随机数
   - torch.arange(), torch.linspace(): 序列

3. Tensor操作:
   - 索引和切片
   - 形状变换: reshape, view, transpose
   - 数学运算: +, -, *, /, @
   - 聚合操作: sum, mean, max, min

4. 高级特性:
   - 广播机制
   - GPU加速
   - 内存管理

5. 最佳实践:
   - 选择合适的数据类型
   - 合理使用GPU资源
   - 注意内存使用
   - 利用广播减少计算

下一步学习: autograd_tutorial.py - 自动微分机制
"""
