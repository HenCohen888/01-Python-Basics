#Change program #5 as follows: this time you may use only one result variable named c (besides a and b).
#Assign one result at a time into c, print it immediately, then assign the next result.
#Do not use any other result variables, and print the results only via c.
#(Keep the table style from Q5; assume every value fits in 5 characters.)

a = int(input("please enter 1st intiger, it will be 'a' intiger:"))
b = int(input("please enter 2nd intiger (not a zero), it will be 'b' intiger:"))

while b == 0:
    print("b cannot be a zero because it need to be devided by b")
    b = int(input("please enter 2nd intiger again (not a zero)"))

print("\ncalculating using only variable c...\n")

# top border (6 columns, width 5 each)
print("+" + "+".join(["-" * 5] * 6) + "+")

# header row (centered)
print(f"|{'a':^5}|{'b':^5}|{'c=a+b':^5}|{'d=a-b':^5}|{'e=a*b':^5}|{'f=a/b':^5}|")

# separator after header
print("+" + "+".join(["-" * 5] * 6) + "+")

# data row – build the line step by step, printing via c only
print("|", end="")

# a and b (printed directly)
print(f"{a:>5}|", end="")
print(f"{b:>5}|", end="")

# c = a + b
c = a + b
print(f"{c:>5}|", end="")

# c = a - b
c = a - b
print(f"{c:>5}|", end="")

# c = a * b
c = a * b
print(f"{c:>5}|", end="")

# c = a / b  (truncate toward 0 to match Q5's example: -81/10 -> -8)
c = int(a / b)
print(f"{c:>5}|")

# bottom border
print("+" + "+".join(["-" * 5] * 6) + "+")