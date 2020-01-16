import pandas as pd
import numpy as np


df = pd.DataFrame(
    {
        'A': ['foo', 'bar', 'foo', 'bar','foo', 'bar', 'foo', 'foo'],
        'B': ['one', 'one', 'two', 'three','two', 'two', 'one', 'three'],
        'C': np.random.randn(8),
        'D': np.random.randn(8)
    }
)

print(df)
# 先分组，再用 sum()函数计算每组的汇总数据
data = df.groupby('A').sum()
print(data.to_dict(orient='records'))
print(data)

# 多列分组后，生成多层索引，也可以应用 sum 函数
more_group = df.groupby(['A', 'B']).sum()
print(more_group)
