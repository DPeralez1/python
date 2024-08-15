# Create a module for the multi function terminal challenege we did last lesson
# All the functions should be stored in a seperate file
# Use any of the 3 methods we learned to import

# Create a loop to run your flight_Check()
# Ask the user if they want to check their flight
# if yes, call the needed function
# The loop stops when the user enters quit

from terminal import *

question = input("Would you like to check your flight: ").lower()
while question != 'quit':
    if question == 'yes':
        flight_check()
    else:
        print("You did not say yes.")
    question = input("Would you like to check your flight: ").lower()
