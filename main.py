import json
import os


#function to load data from file
def loadfile(filename):
#try to open the file
  try:
    with open(filename, 'r') as f:
      return json.load(f)
  except FileNotFoundError:
    #if file doesn't exist, create it and populate it with AllowedVehiclesList
    data = {"vehicles": AllowedVehiclesList}
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
      json.dump(data, f, ensure_ascii=False, indent=4)
    return data


#function to save data to file
def savedata(filename, data):
  with open(filename, 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


#file paths
datadir = 'data'
datafile = os.path.join(datadir, 'authorizedvehiclelist.json')
mainfile = 'main.py'

#list of available vehicles for sale
AllowedVehiclesList = [
    'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 
    'Rivian R1T', 'Ram 1500'
]


#function to add a vehicle
def addvehicle(vehiclename, vehicles):
  if vehiclename not in vehicles:
    vehicles.append(vehiclename)
    print(f"You have added {vehiclename} as an authorized vehicle")
  else:
    print(f"Invalid entry, {vehiclename} already exists.")


#function to REMOVE a vehicle
def removevehicle(vehiclename, vehicles):
  confirm = input(
      f"Are you sure you want to remove \"{vehiclename}\" from the Authorized Vehicles List?\n"
  )
  if confirm.lower() == 'yes':
    if vehiclename in vehicles:
      vehicles.remove(vehiclename)
      print(
          f"You have REMOVED {vehiclename} as an authorized vehicle")
  elif confirm.lower() == 'no':
    return
  else:
    print("Invalid input. Please enter 'yes' or 'no'.")


#function to PRINT all Authorized Vehicles
def print_vehicles(data):
    print(
        "The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: "
    )
    for model in data["vehicles"]:
        print(model)


#function to SEARCH for Authorized Vehicle
def search_vehicle(data):
    query = input("Please enter the full Vehicle name: ")
    found = False
    for model in data["vehicles"]:
        if query.lower() == model.lower():
            print(model, "is an authorized vehicle")
            found = True
            break
    if not found:
        print(
            query,
            "is not an authorized vehicle, if you received this in error please check the spelling and try again"
        )


#function to ADD Authorized Vehicle
def add_vehicle(data):
    vehiclename = input(
        "Please Enter the full Vehicle name you would like to ADD: ")
    addvehicle(vehiclename, data["vehicles"])
    savedata(datafile, data)


#function to DELETE Authorized Vehicle
def delete_vehicle(data):
    vehiclename = input(
        "Please Enter the full Vehicle name you would like to REMOVE: ")
    removevehicle(vehiclename, data["vehicles"])
    savedata(datafile, data)


#while loop
while True:
  #load authorizedvehiclelist.json file
  data = loadfile(datafile)
  #formatting of prompt
  print("********************************")
  print("AutoCountry Vehicle Finder v0.4")
  print("********************************")
  print("Please enter the following number below from the following menu:\n")

  #client response options
  userInput = input(
      "1. PRINT all Authorized Vehicles\n2. SEARCH for Authorized Vehicles\n3. ADD Authorized Vehicle\n4. DELETE Authorized Vehicle\n5. Exit\n********************************\n"
  )

  #output
  #if user typed "1"
  if userInput == '1':
      print_vehicles(data)

  #if user typed "2"
  elif userInput == '2':
      search_vehicle(data)

  #if user typed "3"
  elif userInput == '3':
      add_vehicle(data)

  #if user typed "4"
  elif userInput == '4':
      delete_vehicle(data)

  #if user typed "5"
  elif userInput == '5':
      savedata(datafile, data)
      print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
      break
  else:
    print("Invalid choice. Please enter a number from 1 to 5.")
