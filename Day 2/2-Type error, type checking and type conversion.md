# Type error

## Example 1:

    len(1234)

output:

    TypeError: object of type 'int' has no len()


## Example 2:

    num_char = len(input("What is your name? "))
    print("Your name has " + num_char + " characters")
    
output:

    What is your name? Phoebe

        print("Your name has " + num_char + " characters")
    TypeError: can only concatenate str (not "int") to str
    
 We were concatenating a string to an integer, we end up with an error.
 
 ## How can we prevent these type errors and how can we see the data type that we're working with?
 
 # Type checking
 ## type()
 
 - We could use a function called **type()**
 - It will check whatever you put between the parentheses and give you the type of data that it is.
 
         num_char = len(input("What is your name? "))
        # print("Your name has " + num_char + " characters")

        #type of data
        print(type(num_char))
 
 output:
 
     What is your name? phoebe
    <class 'int'>


# Type Conversion (type casting)
where we change a piece of data from one particular data type to another.

    num_char = len(input("What is your name? "))

    #converted num_char into a string
    #str(num_char)

    #the stored it under a new name 
    new_num_char = str(num_char)

    #print("Your name has " + num_char + " characters")
    print("Your name has " + new_num_char + " characters")
    
output:

    What is your name? phoebe
    Your name has 6 characters
    
# Exercise

## EX1

    a = 123

    #type check
    print(type(a))
    
output

    <class 'int'>
    
## EX2

    a = str(123)

    #type check
    print(type(a))
    
 output
 
    <class 'str'>
    
## EX3

    a = float(123)

    #type check
    print(type(a))
    
output

    <class 'float'>
    
## EX4

    # float()
    print(70 + float("100.5"))

    # str()
    print(str(70)+str(100))

output

    170.5
    70100

# Conclusion

- We can use type function to investigate the data type we're working with.
- We can use functions like string, int or float to convert to that data type
