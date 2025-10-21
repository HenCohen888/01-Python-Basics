#the program that reads three integers from the user, computes their squares, and prints them in a table.
#Use as few variables as possible.

print("+-----+-----+")
print(f"|{'x':^5}|{'x*x':^5}|")
print("+-----+-----+")

x = int(input("please enter the 1st intiger:"))
print(f"|{x:>5}|{(x*x):>5}|")
x = int(input("please enter the 2nd intiger:"))
print(f"|{x:>5}|{(x*x):>5}|")
c = int(input("please enter the 3rd intiger:"))
print(f"|{x:>5}|{(x*x):>5}|")
print("+-----+-----+")