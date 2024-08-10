#---------- Challenge 1 ----------
# Create an empty list, then ask the user for an input "Enter the name of a fruit:"
# While the input is not 'quit, add the input to your list and ask again
# Once the user enters 'quit', ask the user to guess a fruit
# If the guess is in your list, print "Congrats!"
# Other wise print "Sorry, that is not in the list"

answers = []
fruit = input("Enter name of a fruit: ").lower()
while fruit != "quit":
    answers.append(fruit)
    fruit = input("Enter name of a fruit: ")

guess = input("Guess a fruit: ").lower()
for answer in answers:
    if guess == answer:
        print("Congrats you guessed it")
        break
    else:
        print("Sorry, not on the list. ")
        break


# #---------- Challenge 2 ----------
# Create an empty list for capital cities
# Ask the user to enter a city, as long as the user doesn't enter 0, the program continues
# Check to see if the input is already in the list, if so print, "You already have that city"
# Otherwise add the new city to your list, when the loop ends, sort your list
# print off your sorted list of capital cities


cities = list()
city = input("Enter a capital city: ").lower()
while city != '0':
    if city in cities:
        print("You have already said that city")
    else:
        cities.append(city)
        city = input("Enter a capital city: ").lower()
cities.sort()
print(f"List of capital cities: {cities}")


#---------- Challenge 3 ----------
# Enter all the basketball players in one input with a space, create a list from this
# create a variable to find the length of the list
# declare a new list for teams
# Loop through each player, and assign them to a random team from 1 - 3
# End with looping through the number of players and show their name and team number

from random import *

players = input("Enter each player: ").split(" ")
player_amt = len(players)
team = list()
for player in players:
    random_team = randint(1,3)
    team.append(random_team)

for i in range(player_amt):
    print(f"{players[i]} - {team[i]}")


#---------- Challenge 4 ----------
# Here is your list -> scores = ["Billy - 5","Sarah - 4","Leo - 3","John - 3","Anna - 4"]
# Create a counter variable (used to find the average)
# You need to loop through your list and get the score from each person (5,4,3,3,4)
# Increase the counter by this score
# Calculate the average score
# Print off the average group score


scores = ["Billy - 5","Sarah - 4","Leo - 5","John - 3","Anna - 5"]
average = 0

for score in scores:
    x = int(score[len(score) -1])
    average += x

average /= len(scores)
print(f"The average score: {average}")


#---------- BONUS Challenge 5 ----------
# Create a function that takes a list as a parameter, if the list is 0, return None
# Otherwise the function calculates the average of the numbers from the list

# Create a loop to run the length of the list
# Generate a new list everytime the loop runs with the current index of your list
# NOTE -> We haven't studied this, here is a clue -> sublist = numbers_list[:i+1]
# Call your function and give it the sublist
# Print off the average og the sublist

def calc_avg(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) /len(numbers)


number_list = [2,5,4,3,7,6,5]
for i in range(len(number_list)):
    sublist = number_list[:i+1]
    average = calc_avg(sublist)
    print(f"The average of {sublist} is {average}")
