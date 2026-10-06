import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 75000]
})

df.head()
df.tail()
# df.shape
# df.colunms
df.info()
df.describe()
df["Name"]
