print("Welcome to the Guess the Number game!")
print("I have picked a number between 0 and 1,000,000. Can you guess it?")
print("If you want to exit the game, type a negative number.")
print("Good luck!")

# Initialize attempts counter
attempts = 0
# You can change this number to any number between 0 and 1,000,000
correct_number = 10

while True:
    # Pick a number between 0 and 1,000,000
    guess = int(input("Enter your guess: "))

    # Check if the user wants to exit the game
    if guess < 0:
        print("Exiting the game. Goodbye!")
        break

    # Check if the guess is too low, too high, or correct
    if guess < correct_number:
        attempts += 1
        print("Too low! Try again.")
    elif guess > correct_number:
        attempts += 1
        print("Too high! Try again.")
    else:
        print(f"Congratulations! 🎉 You guessed the correct number {correct_number} in {attempts} attempts.")
        break

## Day 18 - Guess the Number Game excercise 