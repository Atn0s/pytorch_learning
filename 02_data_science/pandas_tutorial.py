# -*- coding: utf-8 -*-

"""
Pandas Tutorial
This script demonstrates fundamental and advanced concepts of Pandas.
"""

import pandas as pd
import numpy as np

def main():
    """Main function to demonstrate Pandas features."""
    print("--- Pandas Tutorial ---")

    # 1. Data Structures: Series and DataFrame
    print("\n1. Creating Series and DataFrame")
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(f"Series:\n{s}")

    dates = pd.date_range('20230101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(f"\nDataFrame:\n{df}")

    # 2. Viewing Data
    print("\n2. Viewing Data")
    print(f"Top 3 rows:\n{df.head(3)}")
    print(f"\nBottom 2 rows:\n{df.tail(2)}")
    print(f"\nIndex: {df.index}")
    print(f"\nColumns: {df.columns}")
    print(f"\nStatistical summary:\n{df.describe()}")

    # 3. Selection and Indexing
    print("\n3. Selection")
    print(f"Column 'A':\n{df['A']}")
    print(f"\nRows 0-2:\n{df[0:3]}")
    print(f"\nBy label (loc):\n{df.loc['20230101':'20230103', ['A', 'B']]}")
    print(f"\nBy position (iloc):\n{df.iloc[0:2, 0:2]}")
    print(f"\nBoolean indexing (A > 0):\n{df[df.A > 0]}")

    # 4. Handling Missing Data
    print("\n4. Handling Missing Data")
    df_missing = df.copy()
    df_missing.iloc[1, 1] = np.nan
    print(f"DataFrame with NaN:\n{df_missing}")
    print(f"\nDrop NA:\n{df_missing.dropna(how='any')}")
    print(f"\nFill NA with 5:\n{df_missing.fillna(value=5)}")
    print(f"\nCheck for NaN: {pd.isna(df_missing).any().any()}")

    # 5. GroupBy
    print("\n5. GroupBy")
    df_group = pd.DataFrame({
        'group': ['A', 'B', 'A', 'B', 'A', 'B'],
        'value': [10, 20, 12, 22, 15, 25]
    })
    print(f"Original DataFrame for grouping:\n{df_group}")
    grouped = df_group.groupby('group')
    print(f"\nMean value by group:\n{grouped.mean()}")
    print(f"\nSum of values by group:\n{grouped.sum()}")

    # 6. Merging and Concatenating
    print("\n6. Merging and Concatenating")
    left = pd.DataFrame({'key': ['K0', 'K1'], 'A': ['A0', 'A1']})
    right = pd.DataFrame({'key': ['K0', 'K1'], 'B': ['B0', 'B1']})
    merged = pd.merge(left, right, on='key')
    print(f"Merged DataFrame:\n{merged}")

    df_concat = pd.concat([df.head(3), df.tail(3)])
    print(f"\nConcatenated DataFrame:\n{df_concat}")

    # 7. Pivot Tables
    print("\n7. Pivot Tables")
    df_pivot = pd.DataFrame({
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    })
    print(f"Original DataFrame for pivot:\n{df_pivot.head()}")
    pivot = pd.pivot_table(df_pivot, values='D', index=['A', 'B'], columns=['C'])
    print(f"\nPivot Table:\n{pivot}")

    # 8. Time Series
    print("\n8. Time Series")
    ts = pd.Series(np.random.randn(100), index=pd.date_range('2023-01-01', periods=100))
    ts = ts.cumsum()
    print(f"Time series data (first 5):\n{ts.head()}")
    print(f"\nResampled to monthly sum:\n{ts.resample('M').sum()}")

if __name__ == "__main__":
    main()
