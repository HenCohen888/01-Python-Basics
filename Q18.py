#the script will get a monthly-paymant + additions from the user, calculate it with reduction of 10% income tax, the print the salary

name = input("Enter the name:")
pay = float(input("Enter the monthly pay:"))
add = float(input("Enter the sum of the additions:"))

print(f"{name}'s salary is: {(pay*0.9+add):.0f}")
