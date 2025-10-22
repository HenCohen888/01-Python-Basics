#The script will get 4 types of fabric: "yellow"," red", "blue" and "green"
#costs per unit: red = 75$ , yellow = 80$ , green = 100$ , blue = 120$
#the user will enter the amount (units), the script will calculate the total sum to pay

red = 75
yellow = 80
green = 100
blue = 120

r = int(input("enter the amount of red fabric units:"))
y = int(input("enter the amount of yellow fabric units:"))
g = int(input("enter the amount of green fabric units:"))
b = int(input("enter the amount of blue fabric units:"))

total = r*red+y*yellow+g*green+b*blue

print(f"the total price to pay is: {total}$")