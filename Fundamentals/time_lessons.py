from time import *

#---------- Challenge 1 ----------
# Create a timer similar to the one from the lesson
# The user can enter 1 - begin or 2 - stop
# Once the timer is complete, print off the time passed rounded down to one decimal

# Then check if it was less than 10 seconds, award them 3 points
# between 10 - 15 seconds, award them 2 points
# Anything else, they get 1 points
# Show the number of points they were awarded

timer = int(input("1 - start, 2 - stop: "))
while timer != 2:
    if timer == 1:
        start_timer = time()
    timer = int(input("2 - stop"))

end_timer = time()
total = end_timer - start_timer
print(f"Total time: {round(total, 1)}")

points = 0
if total < 10:
    points += 3
elif total >=10 and total < 15:
    points += 2
else:
    points += 1

print(f"Total points: {points}")


#---------- Challenge 2 ----------
# You need to create a countdown clock
# For this consider using a loop with a counter variable
# Every second, print off the current second
# Print "Your countdown finished after: ____ seconds" once it completes

countdown_start = int(input("Enter a starting number: "))
countdown = countdown_start

while countdown > 0:
    print(countdown)
    countdown -= 1
    sleep(1)
print(f"Your countdown finished after: {countdown_start} sec")


#---------- Challenge 3 ----------
# We want to create a program to calculate the time it takes to download a file
# We ask the user 2 questions. File size in Megabytes and internet speed in megabits/second
# Convert the file to megabits (1 Megabyte = 8 megabits), then calculates the download time
# Display the number of seconds the download will take
# Use the countdown timer to display the download process taking place
# End with printing "Download complete"

file_size = int(input("What is the file size in megabytes? "))
internet_speed = int(input("What is your internet speed megabits/seconds? "))

file_size *= 8
download_time = file_size / internet_speed

print(f"Time to complete download: {round(download_time, 1)} sec")

countdown = round(download_time)
while countdown > 0:
    print(countdown)
    countdown -= 1
    sleep(1)
print("Download completed")
