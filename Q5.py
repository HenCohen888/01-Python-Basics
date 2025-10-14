#Change the previous program so that the output is shown in a table.
#Assume that no value is wider than 5 characters.

a = int(input("please enter 1st intiger, it will be 'a' intiger:"))
b = int(input("please enter 2nd intiger (not a zero), it will be 'b' intiger:"))

#if b = zero, the script will ask again for non zero intiger
while b == 0:
    print("b cannot be a zero because it need to be devided by b")
    b = int(input("please enter 2nd intiger again (not a zero)"))

#compute c,d,e,f as integers
c = a + b      # addition
d = a - b      # subtraction
e = a * b      # multiplication
f = int(a / b)     # integer division so f is an int

print("\ncalculating c,d,e,f...\n")

#print a simple table (each column width = 5)
w = 5
sep = "+" + "+".join(["-" * w] * 6) + "+"  # +-----+-----+-----+-----+-----+-----+

print(sep)
print(f"|{'a':^{w}}|{'b':^{w}}|{'c=a+b':^{w}}|{'d=a-b':^{w}}|{'e=a*b':{w}}|{'f=a/b':{w}}|")
print(sep)

# row with the solutions (right-aligned)
print(f"|{a:>{w}}|{b:>{w}}|{c:>{w}}|{d:>{w}}|{e:>{w}}|{f:>{w}}|")
print(sep)

