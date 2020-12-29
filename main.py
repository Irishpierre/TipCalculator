# Tip Calculator

#Create a greeting
print("Welcome to the Tip Calculator!")

#Ask the user what the total was!
bill = float(input("What was the total bill? $"))

#Ask how much of a tip
tip = int(input("How much would you like to tip? 12, 15, 18, or 20? "))

#How many people are in the part?
people = int(input("How many people split the bill? "))

#Calculate the bill with tip
tipPercent = tip / 100
totalTip = bill * tipPercent
totalBill = bill + totalTip

#Bill per person
billPerPerson = totalBill / people
finalAmount = round(billPerPerson, 2)
print(f"Each person should pay: ${finalAmount}")
