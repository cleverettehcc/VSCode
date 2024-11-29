def Decision_1():
    print(f"""The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:
    {AllowedVehicleList}""")
    
def Decision_2():
    if int(Selection1) == 2:
        print(AllowedVehicleList)
        Search = input("Please enter the full vehicle name: ")
        for vehicle in AllowedVehicleList:
            if (vehicle == Search.lower()):
                print (f"{Search} is an authorized vehicle")
                quit()
        else:
            print(f"{Search} is not an authorized vehicle. If you recieved this error, please check your spelling and try again.")
            quit()
            
def Decision_3():
    if int(Selection1) == 3:
        AddVehicle = input("Please enter the full name of the vehicle you would like to add: ") 
        AllowedVehicleList.append (AddVehicle)
        print(f"you have added '{AddVehicle}' as an authorized vehicle")  
        
        with open("Project1.0.txt", "w") as db:
         db.write(str(AllowedVehicleList))
         db.close()

def Decision_4():
    if int(Selection1) == 4:
        print  ("Please enter the full name of the vehicle you would like to REMOVE: ")
        RemoveVehicle = input()
        Selection2 = input(f"Are you sure you want to remove '{RemoveVehicle}' from the authorized vehicle list?: ")
        if Selection2 == "yes":
            print(f"you have removed '{RemoveVehicle}' as an authorized vehicle")
            AllowedVehicleList.remove (RemoveVehicle)
            with open("Project1.0.txt", "w") as db:
                db.write(str(AllowedVehicleList))
                db.close()
        elif Selection2 == "no":

def Decision_5():
    if int(Selection1) == 5:
        print("Thank you for using the AutoCountry Vehicle Finder, GoodBye!")
        quit()