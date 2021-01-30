# Don't change the code below
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# Don't change the code above

#Write your code below this line
print("Welcome to Python Pizza Deliveries:")
total = 0
#Small Pizza: $15
if size == "S":
    total += 15
#Medium Pizza: $20
elif size == "M":
    total += 20
#Large Pizza: $25
elif size == "L":
    total += 25

if add_pepperoni == "Y":
    #Pepperoni for Small Pizza: +$2
    if size == "S":
        total += 2
    #Pepperoni for Medium or Large Pizza: +$3
    if size == "M" or size == "L":
        total += 3
#Extra cheese for any size pizza: + $1
if extra_cheese == "Y":
    total += 1
print(f"Your final bill is ${float(total)}.")