#---------- Challenge 1 ----------
#Similar to our slides, create a passcode checker
#If the passcode contains an invalid character, print invalid letter

password = input("Enter password: ")
invalid = "!@#$%^&*()-_=+"

for letter in password:
    if letter in invalid:
        print(f"This character is not allowed: {letter}")

print("Access Granted.")



#---------- Challenge 2 ----------
# Create a program that counts vowels in a word
# the program takes an input for a single word.
# Loops through the word and checks for vowels
# at the end, print off the number of vowels in the word

word = input("Enter a word: ").lower()
vowel = "aeiou"
counter = 0

for letter in word:
    if letter in vowel:
        counter += 1

print(f"Number of vowels: {counter} in {word}")


#---------- Challenge 3 ----------
# Create a program that checks for a valid phone number
# If the input contains anything besides a number
# print off, invalid phone number and end the loop

phone_num = input("Enter a phone number: ")
numbers = "1234567890-+()"

for number in phone_num:
    if number not in numbers:
        print("Not a valid number")
        break

#---------- Challenge 4 ----------
# Create a program that takes the number of guests
# For each guest ask their name and age
# if the guest is 18 or older, welcome the user
# otherwise, tell them they must be 18

guests = int(input("Number of guests: "))

for i in range(guests):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    if age >= 18:
        print(f"Welcome {name}")
    else:
        print("Must be older than 18.")

#---------- Challenge 5 ----------
# A user has 5 chances to login into an account
# their username is 'admin' and their password is '12345'
# print off how many tries it takes them
# if they are wrong 5 times, print off You are not the admin!

for i in range(5):
    username = input("Enter username: ")
    passcode = input("Enter passcode: ")
    if username == 'admin' and passcode == '12345':
        print("Welcome admin!")
        break
if username != 'admin' or passcode != "12345":
    print("You are not the admin!")
