import pandas as pd
import numpy as np

li = [
    [1, 2, 3, np.NAN],
    [1, 2, 3, np.NAN],
    [1, 2, 3, np.NAN],
    [1, 2, 3, 4],
    [np.NAN, np.NAN, np.NAN],
]

frame = pd.DataFrame(li)
print(frame)


def drop_nan():
    print('删除 nan 的值')
    # all 表示删除所有行为 nan 的值, inplace 替换原有数据
    frame.dropna(how='all', inplace=True)
    print(frame)


def fill_nan():
    frame.fillna(value=0, inplace=True)
    print(frame)


if __name__ == '__main__':
    # drop_nan()
    fill_nan()