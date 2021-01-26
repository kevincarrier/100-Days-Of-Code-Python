# Don't change the code below
age = input("What is your current age?")
# Don't change the code above

#Write your code below this line

age = int(age)
years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

#There are 365 days in a year, 52 weeks in a year and 12 months in a year.
print(f"You have {days_remaining} days, {weeks_remaining}, and {months_remaining} months left")
