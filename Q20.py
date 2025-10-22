#This progeam solves a system of two linear equations
# Solve:
#   a1*x + b1*y = c1
#   a2*x + b2*y = c2
# using:
#   x = (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
#   y = (a1*c2 - a2*c1) / (a1*b2 - a2*b1)

a1, b1, c1 = map(float, input("Enter the coeffitients of the first equation (a1, b1, c1) :").split())
a2, b2, c2 = map(float, input("Enter the coeffitients of the second equation (a2, b2, c2):").split())

den = a1*b2 - a2*b1  # determinant

if den == 0:
    print("No unique solution (a1*b2 - a2*b1 = 0). Lines are parallel or identical.")
else:
    x = (c1*b2 - c2*b1) / den
    y = (a1*c2 - a2*c1) / den

print(f"The solution is: x={x}, y={y}")