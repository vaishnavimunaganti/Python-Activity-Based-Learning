# Case Study 1: ATM Transaction Simulation

balance = 5000
transactions = [
    ("deposit", 2000),
    ("withdraw", 1000),
    ("withdraw", 800),
    ("deposit", 500),
    ("withdraw", 700)
]

print("Initial Balance: Rs.", balance)

for transaction, amount in transactions:
    if amount <= 0:
        print("Invalid transaction amount")
    elif transaction == "deposit":
        balance = balance + amount
        print("Deposited:", amount)
    elif transaction == "withdraw":
        if amount <= balance:
            balance = balance - amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")
    else:
        print("Invalid transaction type")

print("Final Balance: Rs.", balance)
