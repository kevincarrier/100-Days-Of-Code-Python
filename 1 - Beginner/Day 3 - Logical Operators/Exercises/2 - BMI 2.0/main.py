# Don't change the code below
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# Don't change the code above

#Write your code below this line

#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they are slightly overweight
#Over 30 but below 35 they are obese
#Above 35 they are clinically obese.
result = int(weight) / (float(height) ** 2)
message = ""
if result < 18.5:
    message = "you are underweight"
elif result < 25:
    message = "you have a normal weight"
elif result < 30:
    message = "you are slightly overweight"
elif result < 35:
    message = "you are obese"
else:
    message = "you are clinically obese"

print(f"Your BMI is {int(result)}, {message}.")