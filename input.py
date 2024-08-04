#---------- Challenge 1 ----------
# Create 3 variables to collect information from a user
# These variables are first name, city and country
# print off their information -> ex. Bill lives in Salt Lake City, USA

first_name = input("Enter your first name: ")
country = input("Enter your country: ")
city = input("Enter your city: ")

print(f"{first_name} lives in {city}, {country}")


#---------- Challenge 2 ----------
# Create 2 variables to gather user information
# One is the car rental price for one day, the other is the number of days to rent
# Create a total variable to calculate the total cost
# print out their total cost -> ex. Total car price: 550

day_price = float(input("What is the rental price for the day?: "))
rental_days = int(input("Number of days to rent?: "))

total = day_price * rental_days
print(f"Total car price: ${total}")

#---------- Challenge 3 ----------
# Create 3 variables for shipping packages
# A user can enter the weight of 3 packages
# Create a variable to find the sum of these 3 packages
# Offer a 20% discount on the shipping weight
# Print off total cost for shipment

weight1 = float(input("What is the weight of package 1?: "))
weight2 = float(input("What is the weight of package 2?: "))
weight3 = float(input("What is the weight of package 3?: "))

total = (weight1 + weight2 + weight3) * 0.8

print(f"Total cost for shipping after 20% off: ${round(total,2)}")


#---------- Challenge 4 ----------
# Create a user ID, Their ID is 786147
# Collect the users name and age
# Print off their information
# NOTE Everything should be a string

user_id = 786147
name = input("What is your name? ")
age = input("What is your age? ")
convert_string = str(user_id)

print(f"Welcome {name}, You are {age}. Your id is: {convert_string}")


#---------- Challenge 5 Expense Tracker ----------
# Create an expense tracker
# Collect the Income from a user
# Collect their expenses for food, rent, other
# Get the total amount left after expenses
# print off the remmaining total

income = int(input("What is your income for the month? "))
food = int((input("How much do you spend on food? ")))
rent = int((input("How much is rent? ")))
gas = int((input("What do you spend on gas? ")))
total = income - (food + rent + gas)

print(f"Your remaining amount after expenses is ${total}")


#---------- Challenge 6 Overtime Tracker ----------
# Create an over-time tracker
# Collect a users monthly pay
# Collect the users extra hours worked
# Their bonus is 20% of their monthly salary * extra hours
# Print off their overtime bonus pay

monthly_pay = int(input("Enter your monthly pay: "))
overtime = int(input("Enter extra hours worked: "))
bonus = (monthly_pay*overtime) *0.2
print("Bonus Pay:",bonus)
