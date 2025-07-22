# -*- coding: utf-8 -*-

"""
NumPy 教程
本脚本演示了 NumPy 的基础和高级概念。
"""

import numpy as np

def main():
    """主函数，用于演示 NumPy 的各种功能。"""
    print("--- NumPy 教程 ---")

    # 1. 创建 NumPy 数组
    print("\n1. 创建数组")
    arr_a = np.array([1, 2, 3, 4])
    print(f"从列表创建的一维数组: {arr_a}")
    arr_b = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"二维数组:\n{arr_b}")
    arr_zeros = np.zeros((2, 3))
    print(f"全零数组:\n{arr_zeros}")
    arr_ones = np.ones((3, 2))
    print(f"全一数组:\n{arr_ones}")
    arr_range = np.arange(0, 10, 2)
    print(f"范围数组: {arr_range}")
    arr_linspace = np.linspace(0, 1, 5)
    print(f"线性间隔数组: {arr_linspace}")

    # 2. 数组属性
    print("\n2. 数组属性")
    print(f"arr_b 的形状: {arr_b.shape}")
    print(f"arr_b 的维度: {arr_b.ndim}")
    print(f"arr_b 的数据类型: {arr_b.dtype}")
    print(f"arr_b 的元素数量: {arr_b.size}")
    print(f"arr_b 每个元素占用的字节数: {arr_b.itemsize} 字节")

    # 3. 数组运算
    print("\n3. 数组运算")
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6], [7, 8]])
    print(f"x + y (逐元素加法):\n{x + y}")
    print(f"x * y (逐元素乘法):\n{x * y}")
    print(f"x @ y (矩阵乘法):\n{x @ y}")
    print(f"sqrt(x) (逐元素求平方根):\n{np.sqrt(x)}")
    print(f"x 的转置:\n{x.T}")

    # 4. 索引、切片和布尔索引
    print("\n4. 索引和切片")
    arr_c = np.arange(10, 20)
    print(f"原始数组: {arr_c}")
    print(f"索引为 3 的元素: {arr_c[3]}")
    print(f"从索引 2 到 5 的元素: {arr_c[2:6]}")
    arr_d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"原始二维数组:\n{arr_d}")
    print(f"前两行:\n{arr_d[:2, :]}")
    print(f"第二列: {arr_d[:, 1]}")

    print("\n布尔索引:")
    print(f"arr_d 中大于 5 的元素: {arr_d[arr_d > 5]}")

    # 5. 数组重塑和堆叠
    print("\n5. 数组重塑和堆叠")
    arr_e = np.arange(1, 13)
    reshaped_arr = arr_e.reshape(3, 4)
    print(f"重塑为 3x4 数组:\n{reshaped_arr}")

    arr_v = np.vstack((x, y))
    print(f"垂直堆叠:\n{arr_v}")
    arr_h = np.hstack((x, y))
    print(f"水平堆叠:\n{arr_h}")

    # 6. 广播 (Broadcasting)
    print("\n6. 广播")
    arr_f = np.array([[1, 2, 3], [4, 5, 6]])
    scalar = 10
    print(f"数组 + 标量:\n{arr_f + scalar}")

    vector = np.array([1, 0, 1])
    print(f"数组 + 向量:\n{arr_f + vector}")

    # 7. 线性代数
    print("\n7. 线性代数")
    A = np.array([[1, 1], [0, 1]])
    B = np.array([[2, 0], [3, 4]])
    print(f"A:\n{A}\nB:\n{B}")
    print(f"A 的行列式: {np.linalg.det(A)}")
    print(f"A 的逆矩阵:\n{np.linalg.inv(A)}")
    print(f"A 的特征值和特征向量:\n{np.linalg.eig(A)}")

    # 8. 统计函数
    print("\n8. 统计函数")
    stats_arr = np.array([1, 2, 3, 4, 5, 6])
    print(f"数组: {stats_arr}")
    print(f"平均值: {np.mean(stats_arr)}")
    print(f"中位数: {np.median(stats_arr)}")
    print(f"标准差: {np.std(stats_arr)}")
    print(f"总和: {np.sum(stats_arr)}")

if __name__ == "__main__":
    main()
