# Nested if / else

    if condition:
      if another condition: #nested block
        do this
       else:
        do this

    else: 
      do this

## Example 

    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))

    #if/else 
    if height >= 120:
            print("you can ride the rollercoaster!")
            #Nested if/else
            age = int(input("What is your age? "))
            if age <= 18:
                    print("Please pay $7.")
            else:
                    print("Please pay $12.")
    else:
            print("Sorry, you have to grow taller before you cna ride!")
            
output

    Welcome to the rollercoaster!
    What is your height in cm? 150
    you can ride the rollercoaster!
    What is your age? 27
    Please pay $12.
    
    
# if / elif / else    

    if condition1:
        do A
    elif condition2:
        do B
    else:
        do this
        
## Example

    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))

    #if/else 
    if height >= 120:
            print("you can ride the rollercoaster!")
            #if/elif/else
            age = int(input("What is your age? "))
            if age < 12:
                    print("Please pay $5.")
            elif age <= 18:
                    print("Please pay $7.")
            else:
                    print("Please pay $12.")
    else:
            print("Sorry, you have to grow taller before you cna ride!")
            
output

    Welcome to the rollercoaster!
    What is your height in cm? 150
    you can ride the rollercoaster!
    What is your age? 13
    Please pay $7.
