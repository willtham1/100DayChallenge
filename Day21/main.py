print("Math Game!")
print()
multiples = int(input("Name your multiples: "))
print()
number_of_correct = 0
for i in range(1, 13, 1):
    answer = int(input(f"{i} x {multiples} = "))
    if answer == i * multiples:
        print("Correct!")
        print()
        number_of_correct += 1
    else:
        print("Incorrect!")
        print(f"The correct answer is {i * multiples}.")
        print()
print(f"You got {number_of_correct} out of 12 correct.")

# day21
# 1. Create a math game that asks the user to name their multiples (2, 3, 4, etc.).