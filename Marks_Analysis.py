import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset
data = {
    "Semester": ["Sem 1", "Sem 2", "Sem 3", "Sem 4", "Sem 5", "Sem 6"],
    "Marks": [78, 80, 74, 75, 77, 82]
}

df = pd.DataFrame(data)

print(df)


# 1. Number of semesters
print("Number of semesters:", len(df))


# 2. Highest marks
print("Highest marks:", df["Marks"].max())


# 3. Lowest marks
print("Lowest marks:", df["Marks"].min())


# 4. Best semester
best = df.loc[df["Marks"].idxmax(), "Semester"]
print("Best semester:", best)


# 5. Worst semester
worst = df.loc[df["Marks"].idxmin(), "Semester"]
print("Worst semester:", worst)


# 6. Average marks
print("Average marks:", df["Marks"].mean())


# 7. Improvement from Sem 1 to Sem 6
improvement = df["Marks"].iloc[5] - df["Marks"].iloc[0]
print("Improvement:", improvement, "%")


# 8. First five records
print("\nFirst five records:")
print(df.head())


# 9. NumPy statistics
marks = np.array(df["Marks"])

print("\nMean:", np.mean(marks))
print("Median:", np.median(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))
print("Standard deviation:", np.std(marks))


# 10. Line graph
plt.plot(df["Semester"], df["Marks"], marker="o")

plt.title("Semester-wise Performance")
plt.xlabel("Semester")
plt.ylabel("Marks (%)")

# Target = 75%
plt.axhline(75, linestyle="--", label="Target 75%")

plt.legend()
plt.grid()
plt.show()


# 11. Bar graph
plt.bar(df["Semester"], df["Marks"])

plt.title("Semester-wise Marks")
plt.xlabel("Semester")
plt.ylabel("Marks (%)")

plt.show()