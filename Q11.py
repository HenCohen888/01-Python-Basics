#the script will get 5 intigers a,b,c,d,e and calculate (a+b-c)*d/e
#this time using ONLY two variables in the code 

total = 0   # will hold the running expression value
n = int(input("Enter a (int): "))  # read a
total = n                          # total = a

n = int(input("Enter b (int): "))  # read b
total = total + n                  # total = a + b

n = int(input("Enter c (int): "))  # read c
total = total - n                  # total = a + b - c

n = int(input("Enter d (int): "))  # read d
total = total * n                  # total = (a + b - c) * d

n = int(input("Enter e (int, not 0): "))  # read e
while n == 0:                              # avoid division by zero
    print("e cannot be 0 because we divide by e.")
    n = int(input("Enter e (int, not 0): "))

print("\nExpression: (a + b - c) * d / e")

# print results without creating new variables
print("exact value      =", total / n)         # true division (float)
print("integer part     =", int(total / n))    # truncates toward 0