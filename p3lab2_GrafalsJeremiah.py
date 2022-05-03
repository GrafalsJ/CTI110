service = input("Enter desired auto service:\n")


if service == "Oil change":
    print("You entered:",service)
    print("Cost of oil change: $35")
elif service == "Tire rotation":
    print("You entered:",service)
    print("Cost of tire rotation: $19")
elif service == "Car wash":
    print("You entered:",service)
    print("Cost of car wash: $7")
else:
    print("You entered:",service)
    print("Error: Requested service is not recognized")