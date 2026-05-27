import pandas as pd

# Load Dataset
file_path = '../Dataset/KaggleV2-May-2016.csv'

df = pd.read_csv(file_path)

# Display First Rows
print(df.head())

# Check Shape
print(df.shape)

# Check Missing Values
print(df.isnull().sum())

# Rename Columns

df.rename(columns={
    'Hipertension':'Hypertension',
    'Handcap':'Handicap',
    'No-show':'No_show'
}, inplace=True)

# Convert Date Columns

df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])

# Remove Negative Age

df = df[df['Age'] >= 0]

# Create Waiting Days Column

df['Waiting_Days'] = (
    df['AppointmentDay'] - df['ScheduledDay']
).dt.days

# Save Cleaned Data

df.to_csv('../dataset/cleaned_healthcare_data.csv', index=False)

print('Data Cleaning Completed')