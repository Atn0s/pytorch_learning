# -*- coding: utf-8 -*-

"""
Pandas Tutorial
This script demonstrates the fundamental concepts of Pandas.
"""

import pandas as pd
import numpy as np

def main():
    """Main function to demonstrate Pandas features."""
    print("--- Pandas Tutorial ---")

    # 1. Creating Pandas Series
    print("\n1. Creating Series")
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    print(f"Pandas Series:\n{s}")

    # 2. Creating Pandas DataFrame
    print("\n2. Creating DataFrame")
    dates = pd.date_range('20230101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(f"DataFrame:\n{df}")

    # From a dictionary
    df2 = pd.DataFrame({
        'A': 1.,
        'B': pd.Timestamp('20230102'),
        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
        'D': np.array([3] * 4, dtype='int32'),
        'E': pd.Categorical(["test", "train", "test", "train"]),
        'F': 'foo'
    })
    print(f"\nDataFrame from dict:\n{df2}")

    # 3. Viewing Data
    print("\n3. Viewing Data")
    print(f"First 3 rows:\n{df.head(3)}")
    print(f"Last 2 rows:\n{df.tail(2)}")
    print(f"Index: {df.index}")
    print(f"Columns: {df.columns}")
    print(f"Statistical summary:\n{df.describe()}")

    # 4. Selection
    print("\n4. Selection")
    # By column
    print(f"Selecting column 'A':\n{df['A']}")
    # By slice
    print(f"Slicing rows 0 to 2:\n{df[0:3]}")
    # By label
    print(f"Selecting by label '2023-01-01':\n{df.loc['2023-01-01']}")
    # By position
    print(f"Selecting by position 3:\n{df.iloc[3]}")
    # Boolean indexing
    print(f"Rows where A > 0:\n{df[df.A > 0]}")

    # 5. Handling Missing Data
    print("\n5. Handling Missing Data")
    df_missing = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
    df_missing.loc[dates[0]:dates[1], 'E'] = 1
    print(f"DataFrame with missing data:\n{df_missing}")
    # Drop rows with missing data
    print(f"Drop NA:\n{df_missing.dropna(how='any')}")
    # Fill missing data
    print(f"Fill NA with 5:\n{df_missing.fillna(value=5)}")

    # 6. Operations
    print("\n6. Operations")
    print(f"Mean of all columns:\n{df.mean()}")
    print(f"Mean of rows:\n{df.mean(1)}")
    # Apply function
    print(f"Cumulative sum:\n{df.apply(np.cumsum)}")

if __name__ == "__main__":
    main()
