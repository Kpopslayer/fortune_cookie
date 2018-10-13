# Fortune Cookie Program
# random number between 1 and 5
# each number is assigned to a fortune cookie
# Each time the program is run, the user gets a random number,
# thus a random fortune cookie is displayed
# Quotes from www.horoscope.com

import random

print("\tFortune Cookie Program")

print("\n\nNeed a little bit of sage advice or a quick pick-me-up?")
print("Get the wisdom of your fortune cookie without the calories!")

input("\nPress the enter key to crack open your fortune cookie.\n\n")

number = random.randint(1, 5)

if number == 1:
    print("Everything has beauty, but not everyone can see it.")

elif number == 2:
    print("Tomorrow is another day.")

elif number == 3:
    print("Don't wait for success to come - go find it!")

elif number == 4:
    print("Love is right around the corner.")

elif number == 5:
    print("Things may seem much worse than they are.")

input("\n\nPress the enter key to exit.")
