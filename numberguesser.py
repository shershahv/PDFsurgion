import random

print("Welcome to number guessing game, please select your number range")

lower = input("Enter lower bound: ")
upper = input("Enter Upper bound: ")

print("You have 7 chances to guess the integer")

chanceCounter = 0
correctGuess = random.randint(int(lower),int(upper))
allowedChances = 7

while(chanceCounter < allowedChances):
    
    chanceCounter += 1
    
    choice = int(input("What is your guess: "))
    
    if choice == correctGuess  :
        print(f"Great! the correct number is {correctGuess}")
        break
    elif choice != correctGuess and chanceCounter >= allowedChances:
        print("better lcuk next timer")
    elif choice < correctGuess:
            print(f"too low")
    
    elif choice > correctGuess:
        print(f"too high")

    
