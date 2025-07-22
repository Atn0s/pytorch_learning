# -*- coding: utf-8 -*-

"""
Matplotlib 教程
本脚本演示了使用 Matplotlib 进行各种数据可视化。
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from mpl_toolkits.mplot3d import Axes3D

def main():
    """主函数，用于演示 Matplotlib 的各种功能。"""
    print("--- Matplotlib 教程 ---")
    print("正在生成图表... 请在关闭图表窗口后继续。")

    # 1. 基础绘图与定制
    print("\n1. 基础绘图")
    x = np.linspace(0, 10, 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_sin, color='blue', linestyle='-', linewidth=2, marker='o', markersize=4, label='sin(x)')
    plt.plot(x, y_cos, color='red', linestyle='--', linewidth=2, label='cos(x)')
    plt.title('正弦与余弦函数图像')
    plt.xlabel('x轴')
    plt.ylabel('y轴')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

    # 2. 散点图
    print("\n2. 散点图")
    x_scatter = np.random.rand(50)
    y_scatter = np.random.rand(50)
    colors = np.random.rand(50)
    sizes = 1000 * np.random.rand(50)
    plt.figure(figsize=(10, 6))
    plt.scatter(x_scatter, y_scatter, c=colors, s=sizes, alpha=0.6, cmap='viridis')
    plt.title('高级散点图')
    plt.xlabel('X 值')
    plt.ylabel('Y 值')
    plt.colorbar(label='颜色强度')
    plt.show()

    # 3. 条形图 (水平)
    print("\n3. 条形图")
    labels = ['A', 'B', 'C', 'D']
    values = [10, 20, 15, 5]
    plt.figure(figsize=(10, 6))
    plt.barh(labels, values, color='skyblue')
    plt.title('水平条形图')
    plt.xlabel('值')
    plt.ylabel('类别')
    plt.show()

    # 4. 直方图和密度图
    print("\n4. 直方图和密度图")
    data = np.random.randn(1000)
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
    # 叠加一个密度图
    xmin, xmax = plt.xlim()
    x_density = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x_density, np.mean(data), np.std(data))
    plt.plot(x_density, p, 'k', linewidth=2)
    plt.title('带密度曲线的直方图')
    plt.show()

    # 5. 饼图
    print("\n5. 饼图")
    sizes = [15, 30, 45, 10]
    labels = ['青蛙', '生猪', '狗', '原木']
    explode = (0, 0.1, 0, 0)  # 仅“突出”显示第二块 (即 '生猪')
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')  # 保证饼图是正圆
    plt.title('饼图示例')
    plt.show()

    # 6. 子图 (面向对象方法)
    print("\n6. 子图")
    x_sub = np.linspace(0, 2 * np.pi, 400)
    y1, y2 = np.sin(x_sub**2), np.cos(x_sub**2)
    y3, y4 = np.tan(x_sub), np.exp(-x_sub)

    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    axs[0, 0].plot(x_sub, y1)
    axs[0, 0].set_title('sin(x^2)')
    axs[0, 1].plot(x_sub, y2, 'tab:orange')
    axs[0, 1].set_title('cos(x^2)')
    axs[1, 0].plot(x_sub, y3, 'tab:green')
    axs[1, 0].set_title('tan(x)')
    axs[1, 0].set_ylim(-5, 5) # 限制 tan 函数的y轴范围
    axs[1, 1].plot(x_sub, y4, 'tab:red')
    axs[1, 1].set_title('exp(-x)')
    fig.suptitle('复杂子图示例', fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

    # 7. 3D 图
    print("\n7. 3D 图")
    fig_3d = plt.figure(figsize=(10, 8))
    ax = fig_3d.add_subplot(111, projection='3d')
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)
    r = z**2 + 1
    x_3d, y_3d = r * np.sin(theta), r * np.cos(theta)
    ax.plot(x_3d, y_3d, z, label='参数曲线')
    ax.legend()
    plt.title('3D 图示例')
    plt.show()

if __name__ == '__main__':
    main()
