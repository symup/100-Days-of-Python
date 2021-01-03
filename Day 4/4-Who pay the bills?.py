# You are going to write a program which will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#get total input items
num_items = len(names)

#random_int = random.randint(0,x) FIND X?
random_choice = random.randint(0, num_items - 1)
print(random_choice)

#person_who_will_pay = random.choice(names)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to pay the meal today.")



# output

'''
Give me everybody's names, separated by a comma. Jeff, Angela, Jack, Phoebe
1
Angela is going to pay the meal today.
'''
