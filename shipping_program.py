#receive weight of package
#create groundShipping variable
#create droneShipping variable
#if both are > 125, recommend Premium
#if groundShipping < droneShipping, recommend
#if droneShipping < groundShipping, recommend
#if equal, say it doesn't matter
#use boolean to loop?



#not sure how to handle string inputs yet. Probably an if statement in beginning
#looking for variable input greater than zero, and if it isn't, then print 'error'
#and return to start


#ground shipping and drone shipping variables
groundCost = 0
droneCost = 0
#loop condition
exitVar = "Y"
while exitVar == "Y":
    exitVar = input("Calculate package? Y/N: ")
    if exitVar == "N":
        break
    weight = input("Package weight: ")
    if float(weight) <= 2:
        groundCost = float(weight) * 1.5 + 20
    elif float(weight) <= 6:
        groundCost = float(weight) * 3 + 20
    elif float(weight) <= 10:
        groundCost = float(weight) * 4 + 20
    else:
        groundCost = float(weight) * 4.75 + 20

    print("The Ground Shipping price is: " + str(groundCost))
    #program will print both prices regardless of which is less expensive

    if float(weight) <= 2:
        droneCost = float(weight) * 4.5
    elif float(weight) <= 6:
        droneCost = float(weight) * 9
    elif float(weight) <= 10:
        droneCost = float(weight) * 12
    else:
        droneCost = float(weight) * 14.25

    print("The Drone Shipping price is: " + str(droneCost))
    #program recommends cheapest option
    if float(groundCost) and float(droneCost) > 125:
        print("You should send this bad bitch Ground Shipping Premium - it is cheaper than either option.")
    elif float(groundCost) < float(droneCost):
        print("Ground Shipping is the cheapest option.")
    elif float(groundCost > float(droneCost)):
        print("Drone Shipping is the cheapest option.")
    else:
        print("This is a test.")



print("Program terminated.")
