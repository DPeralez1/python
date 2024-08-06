# Suggest Oasis albums based on mood or fan status
# Once album is suggested, offer 1-2 song recommendations
#  If they like the music and want to know more suggest Documentary. Oasis: Supersonic 2021

# Input statement ot start the system
# Main While Loop (Repeat until an event)
# Conditional Statements (if/elif/else)
# print()
# Try adding the for loop
# 5 or more main actions
# Nesting is key!


print("Welcome to Madferit 2.0. Lets get you listening to Oasis!")
enter = int(input(" 1 - Start. 2 - Quit: "))

if enter == 1:
    albums = (
        "1994 - Definitely Maybe",
        "1995 - (What's the Story) Morning Glory?",
        "1997 - Be Here Now",
        "2000 - Standing on the Shoulder of Giants",
        "2002 - Heathen Chemistry",
        "2005 - Don't Believe the Truth",
        "2008 - Dig Out Your Soul",
        "2010 - Time Flies..."
    )

    while True:
        new_listener = input("Are you a new fan? (Y/N):").lower()
        if new_listener == "y":
            print("Great, lets get started")
            while True:
                your_mood = input("Are you feeling Raw/Iconic, Bombastic/Experimental,  Mature/Psychedelic or Greatest Hits? ").lower()
                if your_mood == "raw/iconic":
                    print("Nice here are the first two albums to get you goin!")
                    for album in albums[:2]:
                        print(album)
                elif your_mood == "bombastic/experimental":
                    print("Loads of class A drugs and new people around added to the sound of these two albums")
                    for album in albums[2:4]:
                        print(album)
                elif your_mood == "mature/psychedelic":
                    print("Other members wrote songs during this time and the high of 90's was truly gone. 2008 would be the last album.")
                    for album in albums[4:7]:
                        print(album)
                elif your_mood == "greatest hits":
                    print("I get it. Give me the hits and lets see what they have to offer. ")
                    for album in albums[7:8]:
                        print(album)
                else:
                    print("You can try their greatest B-side album ever. The Masterplan")

                another_mood = int(input("Would you like to pick another mood? 1 - Yes, 2 - Quit: "))
                if another_mood == 2:
                    break

        else:
            print("Well I dont need to tell you whats good. ")
            movie_doc = input("Have you seen any of the documentries (Y/N)?: ").lower()
            if movie_doc == 'n':
                print("The Oasis: Supersonic documentary from 2016 is a really good watch. See the unrepeatable rise of the greatest band of the 90's")
            elif movie_doc == 'y':
                print("Well...No better time like the present to re-listen to albums again.")
        break

print("Enjoy the listening experience!")
