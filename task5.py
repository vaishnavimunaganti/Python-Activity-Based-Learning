# Case Study 5: Bus Passenger Occupancy

capacity = 40

passengers = 0

stops = [
    (15, 0),
    (10, 5),
    (20, 3),
    (5, 10)
]

for stop, (boarding, alighting) in enumerate(stops, start=1):

    if alighting > passengers:
        print("Stop", stop, ": Invalid alighting count")
        continue

    passengers = passengers - alighting
    passengers = passengers + boarding

    print("Stop:", stop)
    print("Passengers:", passengers)

    if passengers > capacity:
        print("Warning: Bus capacity exceeded")
    else:
        print("Capacity is valid")

print("Final Passengers:", passengers)
