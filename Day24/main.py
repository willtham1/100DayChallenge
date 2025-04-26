import random
print("Infinity Dice 🎲")
  
sides = int(input("How many sides?: "))
playGame = "yes"
  
def rollDice(sides):
  print("You rolled ", random.randint(1,sides))
while playGame == "yes":
    rollDice(sides)
    playGame = input("Roll again?")


# Day24 we learned about parameters and arguments. We created a function called rollDice that takes a parameter called sides. The function generates a random number between 1 and the number of sides on the die. We also learned about while loops and how to use them to repeat a block of code until a certain condition is met. In this case, we used a while loop to keep rolling the dice until the user decides to stop.