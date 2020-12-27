# Modula Operation
The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

    7 % 2 
    = 2 + 2 + 2 + 1 
    = 1 (Remainder of 1)

# Problem
Write a program that works out whether if a given number is an odd or even number.

## Code

    # 🚨 Don't change the code below 👇
    number = int(input("Which number do you want to check? "))
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇

    if number % 2  == 0 :
            print("This is an even number.")
    else:
            print("This is an odd number.")

output

    Which number do you want to check? 6
    This is an even number.

# My code

    # 🚨 Don't change the code below 👇
    number = int(input("Which number do you want to check? "))
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇

    if ( number % 2 ) == 1:
            print("This is an odd number.")
    else:
            print("This is an even number.")

my output

    Which number do you want to check? 43
    This is an odd number.
