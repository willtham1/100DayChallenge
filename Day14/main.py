from getpass import getpass as input

print("Lets play rock, paper, scissors!")
print()

player1 = input("Player 1, please enter your name: ")
player2 = input("Player 2, please enter your name: ")
player1_choice = input(player1 + ", please enter your choice (rock, paper, scissors):").lower()
player2_choice = input(player2 + ", please enter your choice (rock, paper, scissors):").lower()
print()

print(player1 + " chose " + player1_choice + ".")
print(player2 + " chose " + player2_choice + ".")
print()

if player1_choice == player2_choice:
    print("It's a tie!")
elif player1_choice == "rock":
    if player2_choice == "scissors":
        print(player1 + " wins!")
    else:
        print(player2 + " wins!")
elif player1_choice == "paper":
    if player2_choice == "rock":
        print(player1 + " wins!")
    else:
        print(player2 + " wins!")
elif player1_choice == "scissors":
    if player2_choice == "paper":
        print(player1 + " wins!")
    else:
        print(player2 + " wins!")
else:
    print("Invalid input. Please enter rock, paper, or scissors.")

## Day 14 is a rock, paper, scissors game. Our actually first "Big" project.