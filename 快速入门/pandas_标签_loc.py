import numpy as np
import pandas as pd


df = pd.DataFrame(np.random.randn(6, 4), index=[0, 1, 2, 3, 4, 5], columns=list('ABCD'))
print(df)


# df.loc 用标签提取行数据
def df_loc():
    print('===============', '获取一行数据')
    one_line = df.loc[0]
    print(one_line)

    print('用标签提取多列数据')
    many_line = df.loc[:, ['A', 'B']]
    print(many_line)

    print('用标签进行切片')
    spilt_line = df.loc[2:3, ['A', 'C']]
    print(spilt_line)

    print('快速的提取某行中具体的标量值')
    print(df.loc[0, "A"])

    print('与上述的方法一致')
    print(df.at[0, 'A'])


# 按位置进行选择
def df_iloc():
    print('通过索引获取指定的行')
    three_data = df.iloc[3]
    print(three_data)

    print('通过索引切片和标量切片')
    splie_data = df.iloc[3:5, 0:2]
    print(splie_data)

    print('获取指定的行中的标量')
    data = df.iloc[[1, 2, 3], [0, 1, 3]]
    print(data)

    print('获取1,2 行中的所有标量')
    data = df.iloc[1:3, :]
    print(data)

    print('显示的提取数据，如提取第一行中的第二个元素')
    data = df.iloc[1, 2]
    print(data)


if __name__ == '__main__':
    # df_loc()
    df_iloc()
