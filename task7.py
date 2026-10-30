# Case Study 7: Manufacturing Quality Control

production = [
    [100, 5],
    [200, 30],
    [150, 10],
    [80, 20]
]

limit = 10

for i in range(len(production)):

    produced = production[i][0]

    defective = production[i][1]

    percentage = defective / produced * 100

    print("Batch:", i + 1)

    print("Units Produced:", produced)

    print("Defective Units:", defective)

    print("Defect Percentage:", round(percentage, 2), "%")

    if percentage > limit:

        print("Result: Quality Check Required")

    else:

        print("Result: Quality is Acceptable")

    print()
