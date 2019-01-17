#Variables and Names

cars = 100
spaceInCar = 4
drivers = 30
passengers = 90
carsNotDriven = cars - drivers
carsDriven = drivers
carpoolCapacity = carsDriven * spaceInCar
averagePassengerPerCar = passengers / carsDriven


print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", carsNotDriven, "empty cars today")
print("We can transport", carpoolCapacity, "people today")
print("We have", passengers, "to carpool today")
print("WE need to put about", averagePassengerPerCar, "in each car")
