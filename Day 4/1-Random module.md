# Generate Random Integers
## randint(a, b)

###### Returns a random integer between a and b

     #Random module
     import random 

     #create a random integer bw 1 and 10
     random_integer = random.randint(1,10)
     print(random_integer)

output

     6

# Generating Random floating point numbers
## random.random()

###### Returns the next random floating point number between [0.0 to 1.0)

     import random 

     #range 0.000000 - 0.999999
     random_float = random.random()
     print(random_float)

     #range 0.0000000 - 4.99999
     randomFloat = random.random() * 5
     print(randomFloat)

output

     0.195191610465262
     2.9417022828539965
