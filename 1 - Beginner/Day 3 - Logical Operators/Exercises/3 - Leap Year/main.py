# Don't change the code below
year = int(input("Which year do you want to check? "))
# Don't change the code above

#Write your code below this line
#1. Is it cleanly divisible by 4?
if year % 4 != 0: 
    print("Not leap year.")
else:
    #2. Is it cleanly divisible by 100?
    if year % 100 != 0:
        print("Leap year.")
    else:
        #2. Is it cleanly divisible by 400?
        if year % 400 != 0:
            print("Not leap year.")
        else:
            print("Leap year.")
