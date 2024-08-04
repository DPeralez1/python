#---------- Challenge 1 ----------
# Create a mini bot that accepts messages
# The loop only breaks/ends once the word 'done' is entered
# Everytime the loops runs, print "We got your message"

# message = input("Enter a message (type 'done' to end): ").lower()

# while message != 'done':
#     print("We got your message!")
#     message = input("Enter a message (type 'done' to end): ").lower()
# else:
#     print("Thank you")

#---------- Challenge 2 ----------
# Create an account login
# The user has 2 passwords, either one can be entered to gain access
# Once the user enters the correct password, greet them with "Welcome to your account"

# password = input("Enter your password: ")

# while password != "tars" and password != "case":
#     password = input("INVALID PASSWORD. TRY AGAIN: ")
# print("Welcome to your account")


#---------- Challenge 3 ----------
# The first 3 people to book are gifted 20% off
# For every person, print "Congrats [name]. You saved 20%"
# Once 3 people have gotten the discount, print "All done!"

# counter = 0

# while counter < 3:
#     name = input("Enter your name: ")
#     print(f"Congrats {name}, you saved 20%!")
#     counter += 1
# print("All done!")


#---------- Challenge 4 ----------
# A user must enter a programming language, but the only get 5 tries
# If the user enters Python, print off how many tries it took them

# tries = 0
# code = ""

# while tries < 5 and code != 'python':
#     code = input("Enter a programming language: ")
#     tries += 1

# if code == 'python':
#     print(f"It took you {tries} tries")



#---------- Challenge 5 ----------
# Create a train ticket booking program
# The program begins when the user enters 0 and ends when the user enters 1
# For every new train ticket, print off the train ticket number

# tickets = input("Enter 1 - book or 2 - end booking: ")
# i = 1

# while tickets != '2':
#     if tickets == '1':
#         print(f"train ticket:{i}")
#         i += 1
#     tickets = input("Enter 1 - book or 2 - end booking: ")



#---------- Bonus Challenge 6 ----------
#BONUS
# Create a trip generator
# If the user enters 1 ask them for their ideal weather, if the user says cold, tell them to go on a ski holiday
# If the user enters anything else, tell them to go to the beach
# If the user initially enters 2, enter them in a raffle.  They only have 4 chances to guess the correct answer to a question
# If they geuss correct, print off "You get a FREE trip!"
