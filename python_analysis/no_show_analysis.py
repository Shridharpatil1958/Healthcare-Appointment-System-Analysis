import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset

df = pd.read_csv('../dataset/cleaned_healthcare_data.csv')

# No-show Percentage

no_show_percentage = (
    df['No_show'].value_counts(normalize=True) * 100
)

print(no_show_percentage)

# SMS Reminder Impact

sms_analysis = pd.crosstab(
    df['SMS_received'],
    df['No_show']
)

print(sms_analysis)

# Plot SMS Reminder Analysis

sms_analysis.plot(kind='bar')
plt.title('SMS Reminder vs No-show')
plt.xlabel('SMS Received')
plt.ylabel('Count')
plt.show()

# Age-wise No-show

age_groups = pd.cut(
    df['Age'],
    bins=[0,18,40,60,100],
    labels=['Children','Adults','Middle Age','Senior']
)

age_analysis = pd.crosstab(age_groups, df['No_show'])

print(age_analysis)

age_analysis.plot(kind='bar')
plt.title('Age Group vs No-show')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.show()