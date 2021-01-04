#You are going to write a program that automatically prints the solution to the FizzBuzz game.

#Write your code below this row 👇

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
         #divisible by 3 and 5
        print("FizzBuzz")
    elif num % 3 == 0:
        #divisible by 3
        print ("Fizz")
    elif num % 5 == 0:
         #divisible by 5
        print ("Buzz")
    else:
        print(num)
        
        
Output:

'''
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
.
.
.
97
98
Fizz
Buzz

'''
