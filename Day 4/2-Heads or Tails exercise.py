#You are going to write a virtual coin toss program. 
#It will randomly tell the user "Heads" or "Tails".
# e.g.
# 1 means Heads
# 0 means Tails

#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

random_integer = random.randint(0,1)

if random_integer == 1:
        print("Heads")
else:
        print("Tails")
