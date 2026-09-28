import matplotlib.pyplot  as plt
students = ["A", "B", "C", "D", "E"]
marks = [70, 85, 60, 90, 75]
study_hours = [2, 4, 1, 5, 3]
plt.subplot(2, 2, 1)
plt.plot(students, marks, marker="o")
plt.title("Students Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.subplot(2, 2, 2)
plt.bar(students, marks)
plt.title("Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.subplot(2, 2, 3)
plt.scatter(study_hours, marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.subplot(2, 2, 4)
plt.pie(marks, labels=students, autopct="%1.1f%%")
plt.title("Marks Comparison")
plt.tight_layout()
plt.show()

