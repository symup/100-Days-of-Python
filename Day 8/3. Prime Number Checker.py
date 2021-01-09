PRIME NUMBER CHECKER

#Prime numbers are numbers that can only be cleanly divided by itself and 1.

#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            #not prime
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


OUTPUT:
  
'''
Check this number: 75
It's not a prime number.
'''
