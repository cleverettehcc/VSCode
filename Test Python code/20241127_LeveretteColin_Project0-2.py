#Changed the car models to lower case

AllowedVehicleList = ["ford f-150", "chevrolet silverado", "tesla cybertruck", "toyota tundra", "nissan titan"]

while True:
    Selection1 = input("""
    ********************************
    AutoCountry Vehicle Finder v0.1
    ********************************
    Please enter a number below from the following menu

    1. Print all authorized vehicles
    2. Search for authorized vehicles
    3. Add authorized vehicle
    4. Exit

    Enter a number: """)


    if int(Selection1) == 1:
        print(f"""The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:
    {AllowedVehicleList}""")
    
    elif int(Selection1) == 4:
        print("Thank you for using the AutoCountry Vehicle Finder, GoodBye!")
        quit()
    
    if int(Selection1) == 3:
        AddVehicle = input("Please enter the full name of the vehicle you would like to add: ") 
        AllowedVehicleList.append(AddVehicle)
        print(f"you have added '{AddVehicle}' as an authorized vehicle")

    if int(Selection1) == 2:
        print(AllowedVehicleList)
        Search = input("Please enter the full vehicle name: ")
        for vehicle in AllowedVehicleList:
            if (vehicle == Search.lower()):
                print (f"{Search} is an authorized vehicle")
                quit()
        else:
            print(f"{Search} is not an authorized vehicle. if you recieved this error, please check your spelling and try again.")
            quit()