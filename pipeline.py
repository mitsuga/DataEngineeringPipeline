import pandas as pd

# Read CSV
df = pd.read_csv("employees.csv")

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Save cleaned data
df.to_csv("cleaned_employees.csv", index=False)

# Create report
report = f"""
DATA ENGINEERING PIPELINE REPORT

Total Employees: {len(df)}
Average Age: {df['Age'].mean():.2f}
Average Salary: {df['Salary'].mean():.2f}

Departments:
{df['Department'].value_counts()}
"""

with open("report.txt", "w") as file:
    file.write(report)

print("Project completed successfully!")