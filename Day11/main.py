print("How many seconds are in a year?")
leap = input("Is it a leap year? (yes or no) ")

dayInYear = 365
dayInLeapYear = 366
hoursInDay = 24
minutesInHour = 60
secondsInMinute = 60


if leap == "yes":
    seconds = dayInLeapYear * hoursInDay * minutesInHour * secondsInMinute
else:
    seconds = dayInYear * hoursInDay * minutesInHour * secondsInMinute

print("There are", seconds, "seconds in a year.")

## Day 11 was an exercise using the types of operators we learned.