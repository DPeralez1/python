# We need a program to determine the salary for full-time and hourly employees
# There will be 2 functions in a seperate file
# the hourly function will accept hours worked. with a rate of 25 per hourly
# Multiply their hours worked with rate, then return the value

# the full-time function will accept exp, for years worked.  They have an annual pay of 25k
# if they worked from 2 - 4 years, they get 1.5x raise and a bonus of 500
# if they worked from 4 - 10 years, they get a 2x raise and a bonus of 1000
# if they worked over 10 years, they get a 3x raise and a bonus of 1500
# anything else, they do not get a raise and their bonus is 200

# In the main program, make a loop to start and end the program
# everytime it runs, it'll ask for a name and type (salary or hourly)
# if type = hourly, ask for the number of hours worked and use the hourly function in a variable
# if type = salary, ask for years worked and use the salary function in a variableAnything else, print "You are unemployeed!"
# Once the loop breaks, print the employee name and their payrate

from challenge_functions import *

account = int(input("1 - run or 2 - quit"))
while account != 2:
    employee = input("Name of employee: ")
    employee_type = input("Salary or Hourly? ").lower()
    if employee_type == 'hourly':
        time = int(input('Hours worked this month: '))
        pay = part_time(time)
    elif employee_type == 'salary':
        exp = int(input("Years on the job: "))
        pay = full_time(exp)
    else:
        print("You dont even work here...")
    print(f"{employee}-salary of: {pay}")
    account = int(input("1 - run or 2 - quit"))
