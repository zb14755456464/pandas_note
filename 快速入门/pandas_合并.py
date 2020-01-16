import pandas as pd
import numpy as np


def pd_concat():
    # 随机生成 10行4列
    df = pd.DataFrame(np.random.randn(10, 4))
    print(df)

    pieces = [df[:3], df[3:7], df[7:]]
    print(pieces)
    print(pd.concat(pieces, ignore_index=True))


def pd_join():
    left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
    right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
    print(left)
    print(right)
    data = pd.merge(left, right, on='key')
    print(data)

def pd_append():
    df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
    s = df.iloc[3]
    res = df.append(s, ignore_index=True)
    print(res)


if __name__ == '__main__':
    # pd_concat()
    # pd_join()
    pd_append()
