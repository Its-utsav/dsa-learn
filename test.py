import pandas as pd

data = {
    "name": ["Jack", "Piper", "Mia", "Ulysses"],
    "salary": [19666, 74754, 62509, 54866],
}


df = pd.DataFrame(data)
df["bonus "] = df["salary"] * 2
print(df)
