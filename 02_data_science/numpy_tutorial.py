# -*- coding: utf-8 -*-

"""
NumPy Tutorial
This script demonstrates the fundamental concepts of NumPy.
"""

import numpy as np

def main():
    """Main function to demonstrate NumPy features."""
    print("--- NumPy Tutorial ---")

    # 1. Creating NumPy Arrays
    print("\n1. Creating Arrays")
    # From a Python list
    list_a = [1, 2, 3, 4]
    arr_a = np.array(list_a)
    print(f"From list: {arr_a}")

    # 2D array
    list_b = [[1, 2, 3], [4, 5, 6]]
    arr_b = np.array(list_b)
    print(f"2D array:\n{arr_b}")

    # Special arrays
    arr_zeros = np.zeros((2, 3))
    print(f"Zeros array:\n{arr_zeros}")

    arr_ones = np.ones((3, 2))
    print(f"Ones array:\n{arr_ones}")

    arr_range = np.arange(0, 10, 2)
    print(f"Range array: {arr_range}")

    # 2. Array Attributes
    print("\n2. Array Attributes")
    print(f"Shape of arr_b: {arr_b.shape}")
    print(f"Dimensions of arr_b: {arr_b.ndim}")
    print(f"Data type of arr_b: {arr_b.dtype}")
    print(f"Size of arr_b: {arr_b.size}")

    # 3. Array Operations
    print("\n3. Array Operations")
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6], [7, 8]])

    print(f"x:\n{x}")
    print(f"y:\n{y}")

    # Element-wise operations
    print(f"x + y:\n{x + y}")
    print(f"x * y:\n{x * y}")

    # Matrix multiplication
    print(f"x @ y (dot product):\n{np.dot(x, y)}")

    # Universal functions
    print(f"sqrt(x):\n{np.sqrt(x)}")

    # 4. Indexing and Slicing
    print("\n4. Indexing and Slicing")
    arr_c = np.arange(10, 20)
    print(f"Original array: {arr_c}")
    print(f"Element at index 3: {arr_c[3]}")
    print(f"Elements from index 2 to 5: {arr_c[2:6]}")

    # Slicing 2D arrays
    arr_d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Original 2D array:\n{arr_d}")
    print(f"Element at (1, 1): {arr_d[1, 1]}")
    print(f"First two rows:\n{arr_d[:2, :]}")
    print(f"Second column: {arr_d[:, 1]}")

    # 5. Reshaping Arrays
    print("\n5. Reshaping Arrays")
    arr_e = np.arange(1, 13)
    print(f"Original array: {arr_e}")
    reshaped_arr = arr_e.reshape(3, 4)
    print(f"Reshaped to 3x4:\n{reshaped_arr}")

    # 6. Broadcasting
    print("\n6. Broadcasting")
    arr_f = np.array([[1, 2, 3], [4, 5, 6]])
    scalar = 10
    print(f"Array:\n{arr_f}")
    print(f"Array + scalar:\n{arr_f + scalar}")

if __name__ == "__main__":
    main()
