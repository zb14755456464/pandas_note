import pandas as pd
import numpy as np


df = pd.DataFrame(
    {
        'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
        'two': pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
        'three': pd.Series([1, 2, 3], index=['b', 'c', 'd'])
    }
)

def pd_sub():
    row = df.iloc[1]
    column = df['two']
    print('-------row-------')
    print(row)
    print('-------column----')
    # print(column)
    data = df.sub(row, axis='columns')
    print('------result------')
    print(data)

def pd_bool():
    data = (df > 3).any()
    data1 = (df > 3).any().any()
    print('是否有大于3的值')
    print(data)
    print('总体是否有大于3的值')
    print(data1)

def pd_empty():
    '''
    验证 pd 是否为空
    :return: True/False
    '''
    res = pd.DataFrame([])
    print(res.empty)

def pd_combine_first():
    """
    合并 A 里面为 NAN的用 B 中的数据进行填充
    :return:
    """
    df1 = pd.DataFrame(
        {
            'A': [1., np.nan, 3., 5., np.nan],
            'B': [np.nan, 2., 3., np.nan, 6.]
        }
    )
    df2 = pd.DataFrame(
        {'A': [5., 2., 4., np.nan, 3., 7.],
         'B': [np.nan, np.nan, 3., 4., 6., 8.]
         }
    )
    data = df1.combine_first(df2)
    print(data)


if __name__ == '__main__':
    # pd_sub()
    # pd_bool()
    # pd_empty()
    pd_combine_first()