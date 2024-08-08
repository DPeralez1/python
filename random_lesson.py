import random

#---------- Challenge 1 ----------
# Create a mini lottery program
# Assign a variable with a winning number and another with a random number
# Show the random number with print
# If the winning number is equal to the random number print, "You win a FREE trip"
# Otherwise, "Sorry you did not win..."

# winning_num = 4
# random_number = random.randint(1,10)
# print(random_number)
# if winning_num == random_number:
#     print(f"Random number: {random_number}")
#     print("You win a FREE trip!")
# else:
#     print(f"Random number: {random_number}. Sorry you did not win..")


#---------- Challenge 2 ----------
# Create a program that assigns passengers to two different flights
# Ask the user if they want a new flight, if their answer is not "no" the program continues
# Create a variable for a random flight number
# If that random flight is equal to 1, increase the counter by 1
# If the random flight is equal to 2, increase another counter by 1
# At the end of the loop, show the number of passenegers on each flight


# user_question = input("Would you like a new flight? (Yes/No) ").lower()
# flight1 = 0
# flight2 = 0
# while user_question != "no":
#     flight_number = random.randint(1,2)
#     print(f"Flight number: {flight_number}")
#     if flight_number == 1:
#         flight1 += 1
#     else:
#         flight2 += 1
#     user_question = input("Would you like a new flight? (Yes/No) ").lower()

# print(f"Number of passengers on flight 1: {flight1}.")
# print(f"Number of passengers on flight 2: {flight2}.")


#---------- Challenge 3 ----------
# Create a guessing game. Two variables, one with a random numberm, the other with an input
# If input is too low, print off "Too low, Try again."
# If the input is too high, print "Too High, Try again."
# Otherwise, print Congrats!


# guess = int(input("Enter a number between 1-10: "))
# random = random.randint(1,10)
# if guess < random:
#     print("Too low, try again.")
# elif guess > random:
#     print("Too high, try again")
# else:
#     print("Congrats!")


#---------- Challenge 4 ----------
# Refactor your last guessing game to improve input
# We want to add the ability to continue guessing until we get the right number
# Think loops!
# Once the random number is guessed, print Congrats and the number of times it took


guess = int(input("Enter a number between 1-10: "))
random = random.randint(1,10)
while guess != random:
    x = random
    tries = 1
    while x != guess:
        if guess < x:
            print("Too low, try again.")
            tries += 1
        elif guess > x:
            print("Too high, try again")
            tries += 1
        guess = int(input("Enter a number between 1-10: "))

    print("Congrats!")
    print(f"It took you {tries} tries")
