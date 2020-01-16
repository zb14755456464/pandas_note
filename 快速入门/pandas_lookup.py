import pandas as pd

li = [
    {"name": "zhang", "age": 12, "six": "boy"},
    {"name": "zyc", "age": 15, "six": "girl"},
]

res = pd.DataFrame(li, index=['A', 'B'])
print(res)
data = res.lookup(row_labels=['A', 'A', "B"], col_labels=['name', 'age', "six"])
print(data)