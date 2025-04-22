debt = 1000
interest_rate = 0.05
years = 10

for month in range(years):
    debt += debt * interest_rate
    print(f"Month {month + 1}: Debt = {debt:.2f}")

    # Day 19 learned about the for loop and how i can set the amount of loops compared to the while loop.