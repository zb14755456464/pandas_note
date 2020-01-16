import pandas as pd

res = pd.DataFrame([
    {"name": "za", "age": 12},
    {"name": "za", "age": 'null'},
])

print(res.replace({"null": 0}))
