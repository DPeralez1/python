#---------- Challenge 1 ----------
# Create a discount program
# Ask the user which type of trip they are taking
# Ask the user for an expected trip cost
# If the trip is a business trip and the price is 1200 or over return True
# Print if the customer gets a discount or not (True or False)


trip_type = input("Taking a business or personal trip?: ").lower()
cost = int(input("Expected trip cost?: "))

if trip_type == "business" and cost >= 1200:
    print("You get the discount")
else:
    print("No discount will be applied")

# discount = trip_type == "business" and price >= 1200
# print(f"Customer receives a discount: {discount}")


#---------- Challenge 2 ----------
# Allow a user to enter a special discount code
# If the discount code is winter23 then give a 20% discount
# Otherwise say the code is invalid

code = input("Please enter discount code: ")

if code != "winter23":
    print("Code is invalid")
else:
    print("Code applied for 20% off!")



#---------- Challenge 3 ----------
# Create a program that recommends a type of trip
# Gather the trip cost from the user
# If the cost is less than 350, tell them to go on a stay-cation
# If the cost is over/equal to 350 and less than 1000, tell them to go on a road trip
# If the cost is equal/over 1000, tell them to catch a flight to the beach
# NOTE No matter the answer, print Have Fun!

# cost = int(input("Whats your total cost for the trip? "))

if cost <= 350:
    print("Go on a stay-cation")
if cost >= 350 and cost < 1000:
    print("Go on a road trip")
if cost >= 1000:
    print("Take a flight to the beach")

print("Have fun!")

#---------- Challenge 4 ----------
# Create a program that gathers bag weight in KG and also either domestic/international from a user

# If the weight is less than or equal to 18kg then the price is 25
# otherwise the price is 75

# Then check if the destination is domestic or international
# if it's domestic, add 300 to the price
# otherwise add 750 to the price
# print off estimated cost

# NOTE What is the price variable?


destination = input("Will this be a Domestic or International flight? ").lower()
bag_weight = int(input("What is the weight of your bags in Kg?: "))
price = 0

if bag_weight <= 18:
    price = 25
else:
    price = 75

if destination == "domestic":
    price += 300
else:
    price += 750

print(f"Ticket Price: {price}")
