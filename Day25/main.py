import random

def rollDice(sides):
    return random.randint(1, sides)

def charactersHealth():
    sixSides = rollDice(6)
    eightSides = rollDice(8)
    health = sixSides * eightSides
    return health 

while True:
    warriorName = input("What is your warrior's name? ")
    print("Their health is: ", charactersHealth())
    print()
    playGame = input("Do you want to add another warrior? (yes/no) ")
    if playGame != "yes":
        print("Thanks for playing!")
        break
    else:
        print("Let's add another warrior!")
        print()


#Day25 we learned about the return funciton and how it replaces everything within it with that return.