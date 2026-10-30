# Case Study 3: Examination Seating Generator

rows = 3
columns = 4

reserved_seats = [(1, 2), (3, 4)]

for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if (i, j) in reserved_seats:
            print("R", end=" ")
        else:
            print("S", end=" ")
    print()
