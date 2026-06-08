import pandas as pd

df = pd.read_csv("../dataset/cleaned_healthcare_data.csv")

print("Missing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())
