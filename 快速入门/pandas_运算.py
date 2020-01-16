import numpy as np
import pandas as pd


df = pd.DataFrame(np.random.randn(6, 4), index=[0, 1, 2, 3, 4, 5], columns=list('ABCD'))


def mean():
    print(df)
    df.dropna()
    # 运算的时候删除为 nan 的数值
    print('求出每一列的最小值')
    data = df.mean()
    print(data)

    print('求出每一行的最小值')
    data = df.mean(1)
    print(data)


def weidu():
    # shift 把数据向下移动的位置
    s = pd.Series([1, 3, np.nan, 6, 8, 9], index=[0, 1, 2, 3, 4, 5]).shift(2)
    print(s)
    print(df)
    data = df.sub(s, axis='index')
    print(data)


def pd_str():
    # Series 的 str 属性包含一组字符串处理功能
    s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
    print(s)
    data = s.str.lower()
    print(data)


if __name__ == '__main__':
    # mean()
    # weidu()
    pd_str()
