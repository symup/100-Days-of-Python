# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Combined/Concatenate two strings together
combined_string = name1 + name2

#lowercase
lower_case_string = combined_string.lower()

#Count TRUE
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e

#Count LOVE
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l + o + v + e


love_score = int(str(true) + str(love))

#print(love_score)

#if/else loop
if (love_score < 10) or (love_score > 90):
        print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
        print(f"Your score is {love_score}, you are alright together.")
else:
        print(f"Your score is {love_score}.")

# output below

"""
Welcome to the Love Calculator!
What is your name? 
Kanye West
What is their name? 
Kin Kardashian
Your score is 42, you are alright together.
"""
