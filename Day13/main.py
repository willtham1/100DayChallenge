print("Grade Generator")
print()
test_name = input("Enter a name of a test. ")
maximum_score = int(input("Enter the maximum score you can recieve on that test. "))
score = int(input("Out of " + str(maximum_score) + ", what did you get? "))
percentage = (score / maximum_score) * 100
print()
print("You got " + str(percentage) + "% on " + test_name + ".")
if percentage >= 90:
    print("You got an A!")
elif percentage >= 80:
    print("You got a B!")
elif percentage >= 70:
    print("You got a C!")
elif percentage >= 60:
    print("You got a D!")
elif percentage >= 50:
    print("You got an E!")
else:
    print("You got an F!")

## Day 13 is a grade generator. It takes the name of a test, the maximum score, and 
# the score you got, and then it calculates the percentage and prints out the grade. 