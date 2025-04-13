myBill = float(input("Enter the amount of your bill: "))
tip = int(input("What percent tip do you want to leave: 15, 18, or 20 percent? "))
numberOfPeople = int(input("Enter the number of people: "))

bill_with_tip = tip / 100 * myBill + myBill
bill_per_person = bill_with_tip / numberOfPeople
final_amount = round(bill_per_person, 2)

print("You all owe", final_amount)