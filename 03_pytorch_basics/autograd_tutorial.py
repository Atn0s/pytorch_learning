# -*- coding: utf-8 -*-

"""
PyTorch Autograd 教程
本脚本深入演示了 PyTorch 的自动微分功能。
"""

import torch

def main():
    """主函数，用于演示 Autograd 的各种功能。"""
    print("--- PyTorch Autograd 教程 ---")

    # 1. 基础梯度计算
    print("\n1. 基础梯度计算")
    # 创建一个需要计算梯度的张量
    x = torch.tensor(2.0, requires_grad=True)
    y = x**2 + 3*x + 1
    print(f"函数 y = x^2 + 3x + 1 在 x=2 处的值为 {y}")
    # 反向传播计算梯度
    y.backward()
    print(f"梯度 dy/dx 在 x=2 处的值: {x.grad}") # 理论值: 2*x + 3 = 7

    # 2. 张量的梯度
    print("\n2. 张量的梯度")
    x_tensor = torch.randn(3, requires_grad=True)
    y_tensor = x_tensor * 2
    # 对一个非标量输出进行反向传播，需要提供一个梯度参数，其形状与输出匹配
    v = torch.tensor([0.1, 1.0, 0.001], dtype=torch.float)
    y_tensor.backward(v)
    print(f"张量输出的梯度: {x_tensor.grad}")

    # 3. 理解计算图
    print("\n3. 理解计算图")
    a = torch.tensor(2.0, requires_grad=True)
    b = a * 3
    c = b + 1
    d = c.sin()
    # .grad_fn 属性指向创建该张量的函数
    print(f"a.grad_fn: {a.grad_fn}") # 用户创建的叶子节点没有 grad_fn
    print(f"b.grad_fn: {b.grad_fn}") # 乘法操作
    print(f"c.grad_fn: {c.grad_fn}") # 加法操作
    print(f"d.grad_fn: {d.grad_fn}") # sin 操作
    d.backward()
    print(f"梯度 dd/da: {a.grad}") # 链式法则: cos(c) * 3

    # 4. 停止梯度追踪
    print("\n4. 停止梯度追踪")
    # 使用 torch.no_grad() 进行推理，可以节省内存
    with torch.no_grad():
        k = a**2
        print(f"在 torch.no_grad() 中计算的 k.requires_grad: {k.requires_grad}")
    # 使用 .detach() 创建一个共享数据但不共享计算历史的新张量
    j = d.detach()
    print(f"从 d 分离出的 j.requires_grad: {j.requires_grad}")

    # 5. 梯度累加与清零
    print("\n5. 梯度累加与清零")
    q = torch.tensor(3.0, requires_grad=True)
    r = q**2
    r.backward() # 第一次反向传播
    print(f"第一次反向传播后的梯度 dr/dq: {q.grad}") # 2*q = 6
    s = q**3
    s.backward() # 第二次反向传播
    print(f"第二次传播后累加的梯度: {q.grad}") # 6 + 3*q^2 = 6 + 27 = 33
    # 在下一次迭代前清零梯度以防止累加
    q.grad.zero_()
    print(f"清零后的梯度: {q.grad}")

    # 6. 高阶导数 (梯度的梯度)
    print("\n6. 高阶导数")
    x_ho = torch.tensor(2.0, requires_grad=True)
    y_ho = x_ho**3
    # 计算一阶导数，需要设置 create_graph=True 来构建用于计算高阶导数的图
    first_grad = torch.autograd.grad(y_ho, x_ho, create_graph=True)[0]
    print(f"一阶导数 dy/dx = 3x^2 在 x=2 处的值: {first_grad}")
    # 计算二阶导数
    second_grad = torch.autograd.grad(first_grad, x_ho)[0]
    print(f"二阶导数 d^2y/dx^2 = 6x 在 x=2 处的值: {second_grad}")

if __name__ == "__main__":
    main()
