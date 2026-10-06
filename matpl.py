import matplotlib.pyplot as plt
# names = ["Alice", "Bob", "Charlie"]
# names = [50000, 60000, 75000]
# # plt.bar(names, salary)
# # plt.axes(names,salary)
# plt.bar(names,salary)
# plt.show()

subjects = ["Math", "Science", "English"]
marks = [85, 90, 78]

# plt.bar(subjects, marks)
# plt.show()

# attendance = [80, 90, 75, 95, 60]
# marks = [65, 85, 70, 92, 55]

# plt.scatter(attendance, marks)
# plt.show()

grades = ["A", "B", "C", "D"]
students = [10, 15, 8, 3]

# plt.pie(students, labels=grades, autopct="%1.1f%%")
# plt.show()

# marks = [45, 55, 60, 65, 70, 72, 75, 80, 85, 90, 95]

# plt.hist(marks, bins=5)
# plt.show()

# plt.title("Student Marks Analysis")

plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.plot([70, 80, 90], label="Student A")
plt.plot([60, 75, 85], label="Student B")

plt.legend()
plt.show()

plt.grid(True)

plt.figure(figsize=(8, 5))

plt.xticks(rotation=45)
