# -*- coding: utf-8 -*-

"""
Pandas 教程
本脚本演示了 Pandas 的基础和高级概念。
"""

import pandas as pd
import numpy as np

def main():
    """主函数，用于演示 Pandas 的各种功能。"""
    print("--- Pandas 教程 ---")

    # 1. 数据结构: Series 和 DataFrame
    print("\n1. 创建 Series 和 DataFrame")
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(f"Series:\n{s}")

    dates = pd.date_range('20230101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(f"\nDataFrame:\n{df}")

    # 2. 查看数据
    print("\n2. 查看数据")
    print(f"前 3 行:\n{df.head(3)}")
    print(f"\n后 2 行:\n{df.tail(2)}")
    print(f"\n索引: {df.index}")
    print(f"\n列名: {df.columns}")
    print(f"\n统计摘要:\n{df.describe()}")

    # 3. 选择和索引
    print("\n3. 选择数据")
    print(f"选择 'A' 列:\n{df['A']}")
    print(f"\n选择 0-2 行:\n{df[0:3]}")
    print(f"\n按标签选择 (loc):\n{df.loc['20230101':'20230103', ['A', 'B']]}")
    print(f"\n按位置选择 (iloc):\n{df.iloc[0:2, 0:2]}")
    print(f"\n布尔索引 (A > 0):\n{df[df.A > 0]}")

    # 4. 处理缺失数据
    print("\n4. 处理缺失数据")
    df_missing = df.copy()
    df_missing.iloc[1, 1] = np.nan
    print(f"含有 NaN 的 DataFrame:\n{df_missing}")
    print(f"\n删除含有 NaN 的行:\n{df_missing.dropna(how='any')}")
    print(f"\n用 5 填充 NaN:\n{df_missing.fillna(value=5)}")
    print(f"\n检查是否有 NaN: {pd.isna(df_missing).any().any()}")

    # 5. 分组 (GroupBy)
    print("\n5. 分组")
    df_group = pd.DataFrame({
        'group': ['A', 'B', 'A', 'B', 'A', 'B'],
        'value': [10, 20, 12, 22, 15, 25]
    })
    print(f"用于分组的原始 DataFrame:\n{df_group}")
    grouped = df_group.groupby('group')
    print(f"\n按组计算平均值:\n{grouped.mean()}")
    print(f"\n按组计算总和:\n{grouped.sum()}")

    # 6. 合并和连接
    print("\n6. 合并和连接")
    left = pd.DataFrame({'key': ['K0', 'K1'], 'A': ['A0', 'A1']})
    right = pd.DataFrame({'key': ['K0', 'K1'], 'B': ['B0', 'B1']})
    merged = pd.merge(left, right, on='key')
    print(f"合并后的 DataFrame:\n{merged}")

    df_concat = pd.concat([df.head(3), df.tail(3)])
    print(f"\n连接后的 DataFrame:\n{df_concat}")

    # 7. 数据透视表 (Pivot Tables)
    print("\n7. 数据透视表")
    df_pivot = pd.DataFrame({
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    })
    print(f"用于透视的原始 DataFrame (前5行):\n{df_pivot.head()}")
    pivot = pd.pivot_table(df_pivot, values='D', index=['A', 'B'], columns=['C'])
    print(f"\n数据透视表:\n{pivot}")

    # 8. 时间序列
    print("\n8. 时间序列")
    ts = pd.Series(np.random.randn(100), index=pd.date_range('2023-01-01', periods=100))
    ts = ts.cumsum()
    print(f"时间序列数据 (前5行):\n{ts.head()}")
    print(f"\n按月重采样并求和:\n{ts.resample('M').sum()}")

if __name__ == "__main__":
    main()
