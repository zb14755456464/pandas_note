import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6, 4), index=[0, 1, 2, 3, 4, 5], columns=list('ABCD'))
print(df)
s1 = pd.Series([10, 20, 30, 40, 50, 60], index=[0, 1, 2, 3, 4, 5])
print(s1)


def one_cow():
    print('整列进行赋值')
    df['D'] = s1
    print(df)

    print('按照标签进行赋值')
    df.at[0, 'A'] = 123
    print(df)

    print('按照位置进行赋值')
    df.iat[1, 0] = 345
    print(df)

    print('按照 numpy 属组进行赋值')
    df.loc[:, 'D'] = np.array([5] * len(df))
    

if __name__ == '__main__':
    one_cow()
