#the script Create six integer variables a, b, c, d, e, f.
#Read values for a and b from the user.
#Put into c, d, e, f the results of addition, subtraction, multiplication, and division of a and b.

a = int(input("please enter 1st intiger, it will be 'a' intiger:"))
b = int(input("please enter 2nd intiger (not a zero), it will be 'b' intiger:"))

#if b = zero, the script will ask again for non zero intiger
while b == 0:
    print("b cannot be a zero because it need to be devided by b")
    b = int(input("please enter 2nd intiger again (not a zero)"))

#the calculations
c = a + b      # addition
d = a - b      # subtraction
e = a * b      # multiplication
f = a // b     # integer division so f is an int

# the results
print("a =", a)
print("b =", b)
print("a + b =", c)
print("a - b =", d)
print("a * b =", e)
print("a // b =", f)




