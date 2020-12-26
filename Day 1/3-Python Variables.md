# VARIABLE

**james = 0123456789**

in the futrure, if we need this piece of data, we can just refer to it by its name.

## Example 1

    name = "jack"
    print(name)
    name = "angela"
    print(name)
    
Output:

    jack 
    angela
    
## Example 2

    #print(len(input("What is your name?")))

    name = input("What is your name?")
    length = len(name)
    print(length)
    
output:

    What is your name?phung
    5
    
# Variable Exercise

    # 🚨 Don't change the code below 👇
    a = input("a: ")
    b = input("b: ")
    # 🚨 Don't change the code above 👆

    ####################################
    #Write your code below this line 👇

    # key1 = a

    # key2 = b
    # a = key2

    # b = key1

    key = a
    a = b
    b = key

    #Write your code above this line 👆
    ####################################

    # 🚨 Don't change the code below 👇
    print("a: " + a)
    print("b: " + b) 

output:

    a: 5
    b: 100
    a: 100
    b: 5


# VARIABLE NAMING
## Rule
- Make your code readable
- One single unit: user_name, length1, ...
- not use function name as a variable name: input, print, ...
