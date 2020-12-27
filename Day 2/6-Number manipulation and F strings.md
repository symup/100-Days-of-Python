# Round the number
## round()

    print(round(8/3))

output

    3
    
# Round number to a given precision in decimal digits
## round( , )

    print(round(8/3, 2))

output

    2.67
    
# Floor division
Instead of using / , we could also use //, to get an integer result without convert it into an integer.

    print ( 8 / 3 )
    print ( 8 // 3 )

output

    2.0
    2

We can use type function to check data type.

# Continue performing calculation

## Example 1:

    result = 4 / 2

    # result divide by 2 again
    result /= 2

    print(result)

output

    1.0
    
## Example 2

    score = 0

    #user scores a point
    # score = score + 1

    score += 1

    print(score)

output

    1

# F Strings

    score = 0
    height = 1.8
    isWinning = True

    #f-string 
    print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
    
output

    your score is 0, your height is 1.8, you are winning is True
    
All of this data types gor combined into a string by using an **f** in fornt of the string, and then using these **curly braces** to place our variables into this strings
