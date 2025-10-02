import random

fruits = [
    "apple",
    "banana",
    "orange",
    "grape",
    "mango",
    "pineapple",
    "strawberry",
    "watermelon",
    "peach",
    "cherry"
]


chosenFruit = random.choice(fruits)

chances = len(chosenFruit) + 2


def guessWord( chosenFruit, chances) :
    print("-" * len(chosenFruit))
    
    charList = list("-" * len(chosenFruit))
    fruitInLetters = list(chosenFruit)
    
    while chances > 0:
        chances -= 1
        letter = input("input your letter : ")
       
        
        
        if letter in fruitInLetters:
            indx = fruitInLetters.index(letter)
            charList[indx] = letter
            print("".join(charList))
            fruitInLetters[indx] = "_"
           
        else:
            print(f"try again, You hva {chances}")
        
        if "-" not in charList:
            print("congratulations! You Won")
            break
        
        elif chances == 0 and "-" in charList:
            print("Out of chances! good luck next time")

guessWord(chosenFruit, chances)  
# function based for but will refactor to OOP in the future once I get there