# marks=[
#     [60,85,95],
#     [85,75,90],
#     [70,80,70]
# ]
# column:p|C|M
# you have to plot a dashboard of 2*2
# 1-create a bar graph to display the total marks by each student
# create a line graph showing the comparision of each subject marks get by students.
# 3-create a bar graph showing the maximum and minimum marks of each subject
# 4-create a line graph showing comparision of student marks vs average marks

import numpy as np
import matplotlib.pyplot as plt

marks = np.array([
    [60, 85, 95],
    [85, 75, 90],
    [70, 80, 70]
])

students = ["Student 1", "Student 2", "Student 3"]
subjects = ["P", "C", "M"]


# Total marks
total = np.sum(marks, axis=1)

# Average marks
average = np.mean(marks, axis=1)

# Maximum marks
maximum = np.max(marks, axis=0)

# Minimum marks
minimum = np.min(marks, axis=0)


# Dashboard 2 x 2
plt.figure(figsize=(10, 8))


# 1. Total marks
plt.subplot(2, 2, 1)
plt.bar(students, total)
plt.title("Total Marks")
plt.xlabel("Students")
plt.ylabel("Marks")


# 2. Subject comparison
plt.subplot(2, 2, 2)

plt.plot(subjects, marks[0], marker="o", label="Student 1")
plt.plot(subjects, marks[1], marker="o", label="Student 2")
plt.plot(subjects, marks[2], marker="o", label="Student 3")

plt.title("Subject Marks Comparison")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()


# 3. Maximum and minimum
plt.subplot(2, 2, 3)

plt.bar(subjects, maximum, label="Maximum")
plt.bar(subjects, minimum, label="Minimum")

plt.title("Maximum and Minimum")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()


# 4. Total vs Average
plt.subplot(2, 2, 4)

plt.plot(students, total, marker="o", label="Total")
plt.plot(students, average, marker="o", label="Average")

plt.title("Total Marks vs Average")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()


plt.tight_layout()
plt.show()