# -*- coding: utf-8 -*-

"""
PyTorch Autograd Tutorial
This script demonstrates the automatic differentiation feature of PyTorch.
"""

import torch

def main():
    """Main function to demonstrate Autograd features."""
    print("--- PyTorch Autograd Tutorial ---")

    # 1. Basic Gradient Calculation
    print("\n1. Basic Gradient Calculation")
    # Create a tensor with requires_grad=True to track computation
    x = torch.tensor(2.0, requires_grad=True)
    print(f"x: {x}")

    # Define a simple function
    y = x**2 + 3*x + 1
    print(f"y = x^2 + 3x + 1 = {y}")

    # Backpropagate to compute gradients
    y.backward()

    # The gradient dy/dx is stored in x.grad
    print(f"Gradient dy/dx at x=2: {x.grad}") # Expected: 2*x + 3 = 7

    # 2. Gradients with Multiple Variables
    print("\n2. Gradients with Multiple Variables")
    a = torch.tensor(1.0, requires_grad=True)
    b = torch.tensor(3.0, requires_grad=True)
    z = 2*a**3 + 3*b**2
    print(f"a: {a}, b: {b}")
    print(f"z = 2a^3 + 3b^2 = {z}")

    z.backward()
    print(f"Gradient dz/da at a=1: {a.grad}") # Expected: 6*a^2 = 6
    print(f"Gradient dz/db at b=3: {b.grad}") # Expected: 6*b = 18

    # 3. Disabling Gradient Tracking
    print("\n3. Disabling Gradient Tracking")
    # Using torch.no_grad()
    with torch.no_grad():
        k = x**2
        print(f"k = x^2 within torch.no_grad(): {k}")
        print(f"k.requires_grad: {k.requires_grad}")

    # Using .detach()
    j = y.detach()
    print(f"j = y.detach(): {j}")
    print(f"j.requires_grad: {j.requires_grad}")

    # 4. Gradient Accumulation
    print("\n4. Gradient Accumulation")
    q = torch.tensor(3.0, requires_grad=True)
    r = q**2
    r.backward() # First backward pass
    print(f"Gradient dr/dq after first pass: {q.grad}") # 2*q = 6

    s = q**3
    s.backward() # Second backward pass
    print(f"Gradient after second pass (accumulated): {q.grad}") # 6 + 3*q^2 = 6 + 27 = 33

    # Zero out the gradient to prevent accumulation
    q.grad.zero_()
    print(f"Gradient after zeroing: {q.grad}")


if __name__ == "__main__":
    main()
