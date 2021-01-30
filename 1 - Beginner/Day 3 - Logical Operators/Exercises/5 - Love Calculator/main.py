# Don't change the code below
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above

#Write your code below this line

#For Love Scores less than 10 or greater than 90, the message should be:
#"Your score is **x**, you go together like coke and mentos."
#For Love Scores between 40 and 50, the message should be:
#"Your score is **y**, you are alright together."
#Otherwise, the message will just be their score. e.g.:
#"Your score is **z**."

#name1 = "Angela Yu"
#name2 = "Jack Bauer"

combined_name = name1.lower() + name2.lower()

#true
#love
true_word = "true"

total_true = 0
for i in true_word:
    total_true += combined_name.count(i)

love_word = "love"

total_love = 0
for i in love_word:
    total_love += combined_name.count(i)

true_love = str(total_true) + str(total_love)
print(true_love)
true_love = int(true_love)

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love > 40 and true_love < 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}")
