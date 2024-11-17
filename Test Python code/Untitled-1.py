AllowedVehicleList = ["Ford F-150", "Chevrolet Silverado", "Tesla CyberTruck", "Toyota Tundra", "Nissan Titan"]

Selection1 = input("""
********************************
AutoCountry Vehicle Finder v0.1
********************************
Please enter the following number below from the following menu

1. Print all authorized vehicles
2. Exit

Enter a number: """)


if int(Selection1) == 1:
    print(f"""The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:
 {AllowedVehicleList}""")
elif int(Selection1) == 2:
    print("Thank you for using the AutoCountry Vehicle Finder, GoodBye!")
    quit()
elif int(Selection1) <= 0:
    print("Invalid input")
    quit()
elif int(Selection1) >= 3:
    print("Invalid input")
    quit()