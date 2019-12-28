from datetime import datetime
import docx

repairDict = {
    "Mustang": 709,
    "Accord": 400,
    "Camry": 388,
    "Civic": 368,
    "Wrangler": 694,
    "Cherokee": 520,
    "Charger": 652,
    "Grand Cherokee": 666,
    "CR-V": 407,
    "F150": 775,
    "Outback": 607,
    "Explorer": 732,
    "Altima": 483,
    "Silverado": 714,
    "Tacoma": 478,
    "Escalade": 1007,
    "Malibu": 532,
    "Tundra": 606,
    "A7": 987,
    "A6": 913,
    "Prius": 408,
    "Tahoe": 744,
    "Highlander": 489,
    "LaCrosse": 569,
    "Model S": 600,
    "CTS": 663,
    "Rogue": 467,
    "Equinox": 537,
    "Gallardo": 24000,
    "Camaro": 585,
    "STS": 669,
    "Bolt": 290,
    "Volt": 650,
    "Pilot": 542,
    "MDX": 501,
    "XT5": 854,
    "ATS": 741,
    "Corvette": 737,
}

def car_calculator():
    while again == "Y":
        make = input('What is the make of this car? ')
        model = input('What is the model of this car? ')
        if model in repairDict:
            repairDictBoolean = True
            print("Your car has an annual repair cost of:")
            print(repairDict[model])
        else:
            repairDictBoolean = False
            repairGuess = input(
                "The repair cost of your car could not be found. How much do you want to estimate for annual repairs? $")
        makeModel = make + ' ' + model
        year = float(input('What is the year of this car? '))
        usaMilesPerYear = 13476  # Number of miles people drive
        thisYear = datetime.now().year
        miles = float(input('How many miles does this car have? '))
        price = float(input('What is the price of this car? '))
        mpg = float(input('How many miles per gallon does this car get? '))
        milesPerYear = round(miles / (thisYear - year), 1)
        lifeLeft = round(carDeath - miles)
        gasppm = gasPrice / mpg
        if (repairDictBoolean == True):
            repairCost = repairDict[model] / usaMilesPerYear
        else:
            repairCost = int(repairGuess) / usaMilesPerYear

        costPerMile = round((price / lifeLeft) + (gasppm / lifeLeft) + (repairCost / lifeLeft), 2)

        print("---------------------------------------------------------------------")
        print('Your ' + makeModel + ' has been driven', milesPerYear, 'miles per year')
        print('Your ' + makeModel + ' has', lifeLeft, 'miles of life left')
        print('Based on miles driven, the true year of your car is ', round(thisYear - (miles / usaMilesPerYear)))
        print('For each mile of life left, your ' + makeModel + ' will cost you: ', costPerMile)
        print("---------------------------------------------------------------------")
        again_2 = input("Do you want to calculate another car? (Y/N)")
        again_2 = again


print('Welcome to the car cost calculator. First we will get some parameters set up.')
gasPrice = float(input("What's the average price per gallon of gas in your area? $"))
carDeath = float(input("How long (in miles) do you drive cars before they die? "))
print("Next, we will talk about specific cars.")
again = "Y"
car_calculator()
