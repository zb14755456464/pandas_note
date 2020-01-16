import pandas as pd

df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})

# 将 grade 的原生数据转换为类别型数据：
df["grade"] = df["raw_grade"].astype("category")
print(df["grade"])
df["grade"].cat.categories = ["very good", "good", "very bad"]
print(df["grade"])
