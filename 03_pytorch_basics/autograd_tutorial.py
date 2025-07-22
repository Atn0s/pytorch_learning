# -*- coding: utf-8 -*-

"""
PyTorch Autograd Tutorial
This script demonstrates the automatic differentiation feature of PyTorch in depth.
"""

import torch

def main():
    """Main function to demonstrate Autograd features."""
    print("--- PyTorch Autograd Tutorial ---")

    # 1. Basic Gradient Calculation
    print("\n1. Basic Gradient Calculation")
    x = torch.tensor(2.0, requires_grad=True)
    y = x**2 + 3*x + 1
    print(f"y = x^2 + 3x + 1 at x=2 is {y}")
    y.backward()
    print(f"Gradient dy/dx at x=2: {x.grad}")

    # 2. Gradients for Tensors
    print("\n2. Gradients for Tensors")
    x_tensor = torch.randn(3, requires_grad=True)
    y_tensor = x_tensor * 2
    # To backpropagate on a non-scalar output, we need to provide a gradient argument
    # which is a tensor of matching shape.
    v = torch.tensor([0.1, 1.0, 0.001], dtype=torch.float)
    y_tensor.backward(v)
    print(f"Gradient for a tensor output: {x_tensor.grad}")

    # 3. Understanding the Computation Graph
    print("\n3. Understanding the Computation Graph")
    a = torch.tensor(2.0, requires_grad=True)
    b = a * 3
    c = b + 1
    d = c.sin()
    print(f"a.grad_fn: {a.grad_fn}")
    print(f"b.grad_fn: {b.grad_fn}") # MulBackward0
    print(f"c.grad_fn: {c.grad_fn}") # AddBackward0
    print(f"d.grad_fn: {d.grad_fn}") # SinBackward0
    d.backward()
    print(f"Gradient dd/da: {a.grad}") # cos(c) * 3

    # 4. Disabling Gradient Tracking
    print("\n4. Disabling Gradient Tracking")
    # Using torch.no_grad() for inference
    with torch.no_grad():
        k = a**2
        print(f"k within torch.no_grad() requires_grad: {k.requires_grad}")
    # Using .detach() to create a new tensor that shares storage but not history
    j = d.detach()
    print(f"j detached from d requires_grad: {j.requires_grad}")

    # 5. Gradient Accumulation and Zeroing
    print("\n5. Gradient Accumulation")
    q = torch.tensor(3.0, requires_grad=True)
    r = q**2
    r.backward()
    print(f"Gradient dr/dq after first pass: {q.grad}")
    s = q**3
    s.backward()
    print(f"Gradient after second pass (accumulated): {q.grad}")
    # Zero out the gradient to prevent accumulation in the next iteration
    q.grad.zero_()
    print(f"Gradient after zeroing: {q.grad}")

    # 6. Higher-Order Derivatives (Gradient of a Gradient)
    print("\n6. Higher-Order Derivatives")
    x_ho = torch.tensor(2.0, requires_grad=True)
    y_ho = x_ho**3
    # First derivative
    first_grad = torch.autograd.grad(y_ho, x_ho, create_graph=True)[0]
    print(f"First derivative dy/dx = 3x^2 at x=2: {first_grad}")
    # Second derivative
    second_grad = torch.autograd.grad(first_grad, x_ho)[0]
    print(f"Second derivative d^2y/dx^2 = 6x at x=2: {second_grad}")

if __name__ == "__main__":
    main()
