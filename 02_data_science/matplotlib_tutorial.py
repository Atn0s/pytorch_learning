# -*- coding: utf-8 -*-

"""
Matplotlib Tutorial
This script demonstrates basic data visualization using Matplotlib.
"""

import matplotlib.pyplot as plt
import numpy as np

def main():
    """Main function to demonstrate Matplotlib features."""
    print("--- Matplotlib Tutorial ---")
    print("Generating plots... Close the plot windows to continue.")

    # 1. Basic Plot
    print("\n1. Basic Plot")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='sin(x)')
    plt.title('Basic Sine Wave Plot')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()

    # 2. Scatter Plot
    print("\n2. Scatter Plot")
    x_scatter = np.random.rand(50)
    y_scatter = np.random.rand(50)
    colors = np.random.rand(50)
    sizes = 1000 * np.random.rand(50)

    plt.figure(figsize=(8, 6))
    plt.scatter(x_scatter, y_scatter, c=colors, s=sizes, alpha=0.5)
    plt.title('Scatter Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.colorbar()
    plt.show()

    # 3. Bar Chart
    print("\n3. Bar Chart")
    labels = ['A', 'B', 'C', 'D']
    values = [10, 20, 15, 5]

    plt.figure(figsize=(8, 6))
    plt.bar(labels, values)
    plt.title('Bar Chart')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.show()

    # 4. Histogram
    print("\n4. Histogram")
    data = np.random.randn(1000)

    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=30, edgecolor='black')
    plt.title('Histogram of a Normal Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

    # 5. Subplots
    print("\n5. Subplots")
    x_sub = np.linspace(0, 2 * np.pi, 400)
    y_sin = np.sin(x_sub**2)
    y_cos = np.cos(x_sub**2)

    fig, axs = plt.subplots(2, 1, figsize=(8, 8))

    axs[0].plot(x_sub, y_sin)
    axs[0].set_title('sin(x^2)')

    axs[1].plot(x_sub, y_cos, 'tab:orange')
    axs[1].set_title('cos(x^2)')

    fig.suptitle('Subplots Example')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

if __name__ == '__main__':
    main()
