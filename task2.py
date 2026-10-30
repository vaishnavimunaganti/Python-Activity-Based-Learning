# Case Study 2: Student Performance Trend Analysis

marks = [65, 72, 85]
total = 0

for mark in marks:
    total = total + mark

average = total / len(marks)

print("Examination Marks:", marks)
print("Average Marks:", average)

if marks[2] > marks[0]:
    print("Performance: Improved")
elif marks[2] < marks[0]:
    print("Performance: Declined")
else:
    print("Performance: Unchanged")

if average >= 75:
    print("Classification: Excellent")
elif average >= 60:
    print("Classification: Good")
elif average >= 40:
    print("Classification: Average")
else:
    print("Classification: Needs Improvement")
