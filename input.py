#---------- Challenge 1 ----------

first_name = input("Enter your first name: ")
country = input("Enter your country: ")
city = input("Enter your city: ")

print(f"{first_name} lives in {city}, {country}")


#---------- Challenge 2 ----------

day_price = float(input("What is the rental price for the day?: "))
rental_days = int(input("Number of days to rent?: "))

total = day_price * rental_days
print(f"Total car price: ${total}")

#---------- Challenge 3 ----------

weight1 = float(input("What is the weight of package 1?: "))
weight2 = float(input("What is the weight of package 2?: "))
weight3 = float(input("What is the weight of package 3?: "))

total = (weight1 + weight2 + weight3) * 0.8

print(f"Total cost for shipping after 20% off: ${round(total,2)}")


#---------- Challenge 4 ----------

user_id = 786147
name = input("What is your name? ")
age = input("What is your age? ")
convert_string = str(user_id)

print(f"Welcome {name}, You are {age}. Your id is: {convert_string}")


#---------- Challenge 5 Expense Tracker ----------

income = int(input("What is your income for the month? "))
food = int((input("How much do you spend on food? ")))
rent = int((input("How much is rent? ")))
gas = int((input("What do you spend on gas? ")))
total = income - (food + rent + gas)

print(f"Your remaining amount after expenses is ${total}")


#---------- Challenge 6 Overtime Tracker ----------

monthly_pay = int(input("Enter your monthly pay: "))
overtime = int(input("Enter extra hours worked: "))
bonus = (monthly_pay*overtime) *0.2
print("Bonus Pay:",bonus)
