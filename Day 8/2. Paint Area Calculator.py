Paint Area Calculator

#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    num_of_cans = math.ceil((test_h * test_w) / cover)
    print(f"You'll need {num_of_cans} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


OUTPUT:

'''
Height of wall: 3
Width of wall: 9
You'll need 6 cans of paint.
'''
