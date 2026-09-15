# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load CSV file
# -----------------------------
df = pd.read_csv('student_scores.csv')

# Display first five rows
print("First Five Rows:")
print(df.head())

# -----------------------------
# Basic Data Analysis
# -----------------------------

# Dataset information
print("\nDataset Information:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Average Math score
average_math = df['Math'].mean()
print(f"\nAverage Math Score: {average_math:.2f}")

# Average Science score
average_science = df['Science'].mean()
print(f"Average Science Score: {average_science:.2f}")

# -----------------------------
# Bar Chart
# -----------------------------
plt.figure(figsize=(8,5))
plt.bar(df['Name'], df['Math'])
plt.title("Math Scores of Students")
plt.xlabel("Students")
plt.ylabel("Math Score")
plt.grid(axis='y')
plt.show()

# -----------------------------
# Scatter Plot
# -----------------------------
plt.figure(figsize=(8,5))
plt.scatter(df['Hours_Studied'], df['Math'])
plt.title("Hours Studied vs Math Score")
plt.xlabel("Hours Studied")
plt.ylabel("Math Score")
plt.grid(True)
plt.show()

# -----------------------------
# Correlation Heatmap
# -----------------------------
correlation = df[['Math', 'Science', 'English', 'Hours_Studied']].corr()

plt.figure(figsize=(6,5))
plt.imshow(correlation, cmap='coolwarm', interpolation='nearest')
plt.colorbar()

plt.xticks(range(len(correlation.columns)), correlation.columns, rotation=45)
plt.yticks(range(len(correlation.columns)), correlation.columns)

# Display correlation values
for i in range(len(correlation.columns)):
    for j in range(len(correlation.columns)):
        plt.text(j, i,
                 f"{correlation.iloc[i, j]:.2f}",
                 ha='center',
                 va='center',
                 color='black')

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()