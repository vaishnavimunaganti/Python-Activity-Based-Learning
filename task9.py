# Case Study 9: Event Registration and Budget Management

registrations = [
    ("R101", 500),
    ("R102", 500),
    ("R103", 500),
    ("R101", 500)
]

sponsorship = 5000

expenses = 4000

registration_ids = []
total_fees = 0

for registration in registrations:

    reg_id, fee = registration

    if reg_id in registration_ids:
        print("Duplicate Registration:", reg_id)

    else:
        registration_ids.append(reg_id)

        total_fees = total_fees + fee

income = total_fees + sponsorship

balance = income - expenses

print("Total Registrations:", len(registration_ids))
print("Total Registration Fees:", total_fees)
print("Sponsorship:", sponsorship)
print("Total Income:", income)
print("Expenses:", expenses)
print("Remaining Balance:", balance)
