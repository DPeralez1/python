#---------- Challenge 1 ----------
# Create a function that accepts a score as a parameter
# if the score is 0 - 50, print "Below passing, Improve"
# if the score is 50-70, print "Barely passing"
# if the score is 70-90 print, You are passing!
# otherwise print, "You are in the top of the class"
# use an input to collect the score then call the function

def grade(score):
    print("Your score is: ")
    if score > 0 and score <= 50:
        print("Below passing, Improve!")
    elif score > 50 and score <=70:
        print("Barley passing")
    elif score > 70 and score <= 90:
        print("You're passing!")
    else:
        print("You're top of the class!")


score = int(input("Enter your score: "))
grade(score)


#---------- Challenge 2 ----------
# Create a function to add on extra flight charges
# the function takes a base fare then asks if you want to upgrade.  If yes add 99 to the base fare
# then it'll ask if you have baggage, if yes add 35 to the base fare
# before returing the price you need to add tax of 0.08%, then return the price
# print off the grand total after extras and tax

def flight_cost(base_fare):
    upgrade = input("Do you want to upgrade: (y/n)").lower()
    if upgrade == 'y':
        base_fare += 99
    baggage = input("Will you have bags? (y/n)").lower()
    if baggage == 'y':
       base_fare += 35

    tax = (base_fare * 0.08) + base_fare
    return tax


base_fare = int(input("Enter the base fare:"))
grand_total = flight_cost(base_fare)
print(f"Grand total after tax: {grand_total:.2f}")




#---------- Challenge 3 ----------
# Create a bank balance function, it will accept a balance
# If the balance is >= 500, return True otherwise return False
# Outside the function, ask for the number of bank customers & loop through depending on number of customers
# Ask for each first name and their current balance, print off if they have enough funds (true/false)
# if the function returns True, print off "no need to worry" else print "Your account is low"


def total(balance):
    if balance >= 500:
        return True
    else:
        return False

customers = int(input("Number of customers? "))
for i in range(customers):
    name = input("What is your first name? ")
    balance = float(input("What is your current balance? "))
    res = total(balance)

    print(f"Enough funds in {name}'s account: ", res)
    if res == True:
        print("Don't worry you have enough funds")
    else:
        print("Your account is getting low!")



#---------- Challenge 4 ----------
# Create a mortage function that accepts a number to determine if someone is eligible
# if they have 50k or more, print "Instant approval"
# if between 20k-50k, print "You need approval" otherwise print "Not apprived!"
# Outside create a loop that ends with "0". The input asks for a deposit amount
# Everytime a deposit is entered this is stored in a total variable and the funciton is called

def mortgage(saved):
    if saved >= 50000:
        print("Instant approval!")
    elif saved >= 20000 and saved < 50000:
        print("You need approval")
    else:
        print("Not approved")

saved = int(input("Deposit amount: "))
total_balance = 0
while saved != 0:
    total_balance += saved
    mortgage(saved)
    saved = int(input("Deposit amount: "))
print(f"Total money requested: {total_balance}")

#---------- Bonus Challange ----------
# create 4 functions, the first 3 will be terminal_1, terminal_2, terminal_3
# When one of those functions are called, print off which terminal to go to the call the main function again
# the main function should ask "is your flight budget/domestic or international" when called
# budget - terminal 1 , domestic - terminal 2, international - terminal 3

def terminal_1():
    print("Departing from terminal 1 - Budget")
    flight_check()

def terminal_2():
    print("Departing from terminal 2 - Domestic")
    flight_check()

def terminal_3():
    print("Departing from terminal 3 - International")
    flight_check()


def flight_check():
    answer = input("Budget/Domestic or International: ").lower()
    if answer == "budget":
        terminal_1()
    elif answer == "domestic":
        terminal_2()
    elif answer == "international":
        terminal_3()
    else:
        print("There is no other terminal!")

flight_check()



#---------- Bonus Challange  ----------
# POPULAR - Create a BMI calculator using 2 functions
# one function calculates and returns the BMI (BMI = weight / (height * height))
# the second function takes the bmi results and tells you if you are underweight, normal weight or overweight
# Create a loop to run for a number of people
# pass the weight and height into one of the functions which will call the first function


def calculate_bmi(weight, height):
    calculation = weight / (height * height)
    return calculation

def show_results(weight, height):
    calculate = calculate_bmi(weight, height)
    if calculate <= 18.5:
        print("Underweight")
    elif calculate > 18.5 and calculate <= 25:
        print("Normal")
    else:
        print("Overweight")

people = int(input("Enter number of people: "))
for i in range(people):
    weight = float(input("Enter weight: "))
    height = float(input("Enter height: "))
    show_results(weight, height)
