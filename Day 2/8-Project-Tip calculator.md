# project

## If the bill was $150.00, split between 5 people, with 12% tip. 
## Each person should pay (150.00 / 5) * 1.12 = 33.6
## Format the result to 2 decimal places = 33.60
## Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

###### HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
###### HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

# Angela answer

    print("Welcome to the tip calculator.")

    bill = float(input("What was the total bill? $"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15? " ))
    people = int(input("How many people to split the bill? "))

    #calculate bill per person
    last_amount = (bill / people) * ((tip / 100 ) + 1)
    last_amount_float = float(last_amount)

    print(f"Each person should pay: $ {round(last_amount_float,2)}" )

output

    Welcome to the tip calculator.
    What was the total bill? $124.56
    How much tip would you like to give? 10, 12, or 15? 12
    How many people to split the bill? 7
    Each person should pay: $ 19.93

# My answer

    print("Welcome to the tip calculator.")

    #input money
    total_bill = input("What was the total bill? $")

    #input percentage
    percentage = input("What percentage tip would you like to give? 10, 12, or 15? " )

    #input number of people
    total_people = input("How many people to split the bill? ")

    #calculate

    last_amount = (float(total_bill) / int(total_people)) * ((int(percentage) / 100 ) + 1)
    last_amount_float = float(last_amount)
    print(f"Each person should pay: $ {round(last_amount_float,2)}" )
    
output

    What was the total bill? $124.56
    What percentage tip would you like to give? 10, 12, or 15? 12
    How many people to split the bill? 7
    Each person should pay: $ 19.93

# How to round float number with 2 decimals digits
$34.5 to $34.50

        Welcome to the tip calculator.
        What was the total bill? $150
        How much tip would you like to give? 10, 12, or 15? 15
        How many people to split the bill? 5
        Each person should pay: $ 34.5
        
## Solve:
# Format function "{:.2f}".formart()

    print("Welcome to the tip calculator.")

    bill = float(input("What was the total bill? $"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15? " ))
    people = int(input("How many people to split the bill? "))

    #calculate bill per person
    last_amount = (bill / people) * ((tip / 100 ) + 1)

    last_amount_float = round(float(last_amount),2)
    #using format function to pass in last_amount
    last_amount_float = "{:.2f}".format(last_amount)

    print(f"Each person should pay: $ {last_amount_float}" )

output

    Welcome to the tip calculator.
    What was the total bill? $150
    How much tip would you like to give? 10, 12, or 15? 15
    How many people to split the bill? 5
    Each person should pay: $ 34.50
