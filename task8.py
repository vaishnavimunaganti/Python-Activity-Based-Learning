# Case Study 8: University Fee and Eligibility Audit

students = [
    ("S101", 10000, 10000, 85, 75),
    ("S102", 8000, 10000, 90, 80),
    ("S103", 10000, 10000, 60, 70),
    ("S104", 10000, 10000, 80, 30),
    ("S105", 10000, 10000, 90, 90)
]

for student in students:

    roll, paid, total_fee, attendance, marks = student

    reasons = []

    if paid < total_fee:
        reasons.append("Fee Pending")

    if attendance < 75:
        reasons.append("Low Attendance")

    if marks < 40:
        reasons.append("Low Internal Marks")

    print("Student:", roll)

    if reasons:
        print("Reasons:", reasons)
    else:
        print("Status: Eligible")

    print()
