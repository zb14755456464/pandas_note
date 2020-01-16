import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(6, 4), index=[0, 1, 2, 3, 4, 5], columns=list('ABCD'))
print(df)


def pd_bool():
    print('用单列的值进行判断，会把不符合条件的值置为 False')
    print(df.A > 0)
    # 只会保留为 True 的数据
    data = df[df.A > 0]
    print(data)

    print('使用整个df进行判断, 会对里面的所有元素进行挨个判断')
    data = df[df > 0]
    print(data)


def df_isin():
    df2 = df.copy()
    df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
    data = df2[df2['E'].isin(['three', 'four'])]
    print(data)


if __name__ == '__main__':
    df_isin()
