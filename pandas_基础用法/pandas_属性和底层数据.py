import numpy as np
import pandas as pd


df = pd.DataFrame(np.random.randn(6, 4), index=[0, 1, 2, 3, 4, 5], columns=list('ABCD'))


def pd_meta():
    print(df)
    print('输出轴维度')
    print(df.shape)  # (6, 4)
    print('输出所有列')
    print(df.columns)  # Index(['A', 'B', 'C', 'D'], dtype='object')
    for columns in df.columns:
        print(columns)
    print('输出所有行')
    print(df.index)  # Int64Index([0, 1, 2, 3, 4, 5], dtype='int64')

def pd_values():
    li = [
        {'name': 'biao', 'age': 12},
        {'name': 'biao1', 'age': 123}
    ]
    res = pd.DataFrame(li)
    print(res.values)
    print(res.to_numpy)


if __name__ == '__main__':
    # pd_meta()
    pd_values()
