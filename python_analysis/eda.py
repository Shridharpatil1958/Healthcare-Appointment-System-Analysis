import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset

df = pd.read_csv('../dataset/cleaned_healthcare_data.csv')

# Total Appointments
print('Total Appointments:', len(df))

# No-show Distribution
print(df['No_show'].value_counts())

# Gender Distribution
print(df['Gender'].value_counts())
