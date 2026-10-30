# Case Study 4: Student Marks Matrix Analysis

marks = [
    [80, 75, 90],
    [70, 85, 78],
    [95, 92, 88]
]

student_totals = []

for student in marks:
    total = 0

    for mark in student:
        total = total + mark

    student_totals.append(total)

    average = total / len(student)

    print("Marks:", student)
    print("Total:", total)
    print("Average:", round(average, 2))

top_student = student_totals.index(max(student_totals)) + 1

print("Top Student: Student", top_student)
print("Highest Total:", max(student_totals))
