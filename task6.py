# Case Study 6: Food Waste Monitoring

prepared = [100, 120, 80, 150, 200]

served = [90, 100, 70, 120, 150]

limit = 20

for i in range(len(prepared)):

    waste = prepared[i] - served[i]

    percentage = waste / prepared[i] * 100

    print("Day:", i + 1)

    print("Meals Wasted:", waste)

    print("Waste Percentage:", round(percentage, 2), "%")

    if percentage > limit:

        print("Warning: Excessive Food Waste")

    else:

        print("Food Waste is Within Limit")

    print()
