# -*- coding: utf-8 -*-

"""
Matplotlib Tutorial
This script demonstrates a variety of data visualizations using Matplotlib.
"""

import matplotlib.pyplot as plt
import numpy as np

def main():
    """Main function to demonstrate Matplotlib features."""
    print("--- Matplotlib Tutorial ---")
    print("Generating plots... Close the plot windows to continue.")

    # 1. Basic Plot with Customization
    print("\n1. Basic Plot")
    x = np.linspace(0, 10, 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_sin, color='blue', linestyle='-', linewidth=2, marker='o', markersize=4, label='sin(x)')
    plt.plot(x, y_cos, color='red', linestyle='--', linewidth=2, label='cos(x)')
    plt.title('Sine and Cosine Waves')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

    # 2. Scatter Plot
    print("\n2. Scatter Plot")
    x_scatter = np.random.rand(50)
    y_scatter = np.random.rand(50)
    colors = np.random.rand(50)
    sizes = 1000 * np.random.rand(50)
    plt.figure(figsize=(10, 6))
    plt.scatter(x_scatter, y_scatter, c=colors, s=sizes, alpha=0.6, cmap='viridis')
    plt.title('Advanced Scatter Plot')
    plt.xlabel('X Value')
    plt.ylabel('Y Value')
    plt.colorbar(label='Color Intensity')
    plt.show()

    # 3. Bar Chart (Horizontal)
    print("\n3. Bar Chart")
    labels = ['A', 'B', 'C', 'D']
    values = [10, 20, 15, 5]
    plt.figure(figsize=(10, 6))
    plt.barh(labels, values, color='skyblue')
    plt.title('Horizontal Bar Chart')
    plt.xlabel('Value')
    plt.ylabel('Category')
    plt.show()

    # 4. Histogram and Density Plot
    print("\n4. Histogram and Density Plot")
    data = np.random.randn(1000)
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
    # Overlay a density plot
    from scipy.stats import norm
    xmin, xmax = plt.xlim()
    x_density = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x_density, np.mean(data), np.std(data))
    plt.plot(x_density, p, 'k', linewidth=2)
    plt.title('Histogram with Density Plot')
    plt.show()

    # 5. Pie Chart
    print("\n5. Pie Chart")
    sizes = [15, 30, 45, 10]
    labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Pie Chart Example')
    plt.show()

    # 6. Subplots (Object-Oriented Approach)
    print("\n6. Subplots")
    x_sub = np.linspace(0, 2 * np.pi, 400)
    y1 = np.sin(x_sub**2)
    y2 = np.cos(x_sub**2)
    y3 = np.tan(x_sub)
    y4 = np.exp(-x_sub)

    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    axs[0, 0].plot(x_sub, y1)
    axs[0, 0].set_title('sin(x^2)')
    axs[0, 1].plot(x_sub, y2, 'tab:orange')
    axs[0, 1].set_title('cos(x^2)')
    axs[1, 0].plot(x_sub, y3, 'tab:green')
    axs[1, 0].set_title('tan(x)')
    axs[1, 0].set_ylim(-5, 5) # Limit tan y-axis
    axs[1, 1].plot(x_sub, y4, 'tab:red')
    axs[1, 1].set_title('exp(-x)')
    fig.suptitle('Complex Subplots Example', fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

    # 7. 3D Plot
    print("\n7. 3D Plot")
    from mpl_toolkits.mplot3d import Axes3D
    fig_3d = plt.figure(figsize=(10, 8))
    ax = fig_3d.add_subplot(111, projection='3d')
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)
    r = z**2 + 1
    x_3d = r * np.sin(theta)
    y_3d = r * np.cos(theta)
    ax.plot(x_3d, y_3d, z, label='parametric curve')
    ax.legend()
    plt.title('3D Plot Example')
    plt.show()


if __name__ == '__main__':
    main()
