# -*- coding: utf-8 -*-

"""
NumPy Tutorial
This script demonstrates the fundamental and advanced concepts of NumPy.
"""

import numpy as np

def main():
    """Main function to demonstrate NumPy features."""
    print("--- NumPy Tutorial ---")

    # 1. Creating NumPy Arrays
    print("\n1. Creating Arrays")
    arr_a = np.array([1, 2, 3, 4])
    print(f"1D Array from list: {arr_a}")
    arr_b = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"2D Array:\n{arr_b}")
    arr_zeros = np.zeros((2, 3))
    print(f"Zeros Array:\n{arr_zeros}")
    arr_ones = np.ones((3, 2))
    print(f"Ones Array:\n{arr_ones}")
    arr_range = np.arange(0, 10, 2)
    print(f"Range Array: {arr_range}")
    arr_linspace = np.linspace(0, 1, 5)
    print(f"Linspace Array: {arr_linspace}")

    # 2. Array Attributes
    print("\n2. Array Attributes")
    print(f"Shape of arr_b: {arr_b.shape}")
    print(f"Dimensions of arr_b: {arr_b.ndim}")
    print(f"Data type of arr_b: {arr_b.dtype}")
    print(f"Size of arr_b: {arr_b.size}")
    print(f"Item size of arr_b: {arr_b.itemsize} bytes")

    # 3. Array Operations
    print("\n3. Array Operations")
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6], [7, 8]])
    print(f"x + y:\n{x + y}")
    print(f"x * y (element-wise):\n{x * y}")
    print(f"x @ y (matrix multiplication):\n{x @ y}")
    print(f"sqrt(x):\n{np.sqrt(x)}")
    print(f"Transpose of x:\n{x.T}")

    # 4. Indexing, Slicing, and Boolean Indexing
    print("\n4. Indexing and Slicing")
    arr_c = np.arange(10, 20)
    print(f"Original array: {arr_c}")
    print(f"Element at index 3: {arr_c[3]}")
    print(f"Elements from index 2 to 5: {arr_c[2:6]}")
    arr_d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Original 2D array:\n{arr_d}")
    print(f"First two rows:\n{arr_d[:2, :]}")
    print(f"Second column: {arr_d[:, 1]}")

    print("\nBoolean Indexing:")
    print(f"Elements in arr_d > 5: {arr_d[arr_d > 5]}")

    # 5. Reshaping and Stacking
    print("\n5. Reshaping and Stacking")
    arr_e = np.arange(1, 13)
    reshaped_arr = arr_e.reshape(3, 4)
    print(f"Reshaped to 3x4:\n{reshaped_arr}")

    arr_v = np.vstack((x, y))
    print(f"Vertically stacked:\n{arr_v}")
    arr_h = np.hstack((x, y))
    print(f"Horizontally stacked:\n{arr_h}")

    # 6. Broadcasting
    print("\n6. Broadcasting")
    arr_f = np.array([[1, 2, 3], [4, 5, 6]])
    scalar = 10
    print(f"Array + scalar:\n{arr_f + scalar}")

    vector = np.array([1, 0, 1])
    print(f"Array + vector:\n{arr_f + vector}")

    # 7. Linear Algebra
    print("\n7. Linear Algebra")
    A = np.array([[1, 1], [0, 1]])
    B = np.array([[2, 0], [3, 4]])
    print(f"A:\n{A}\nB:\n{B}")
    print(f"Determinant of A: {np.linalg.det(A)}")
    print(f"Inverse of A:\n{np.linalg.inv(A)}")
    print(f"Eigenvalues and eigenvectors of A:\n{np.linalg.eig(A)}")

    # 8. Statistical Functions
    print("\n8. Statistical Functions")
    stats_arr = np.array([1, 2, 3, 4, 5, 6])
    print(f"Array: {stats_arr}")
    print(f"Mean: {np.mean(stats_arr)}")
    print(f"Median: {np.median(stats_arr)}")
    print(f"Standard Deviation: {np.std(stats_arr)}")
    print(f"Sum: {np.sum(stats_arr)}")

if __name__ == "__main__":
    main()
