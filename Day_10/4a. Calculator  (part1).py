CALCULATOR - PART 1 

#atep 1: calculator (+ - * /)

#Add
def add(n1, n2):
  """Take 2 inputs, n1 and n2, simple return sum"""
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

#step 2: create a dictionary named operations.
#The keys are symbols, the values are the names of the fuctions
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}

#step 3: create num1 & num2 where we ask the user for an input "What's the first/second number?: "
num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

#step 4: we ask for which operation they wanna use.
#Loop through dictionary and print out each key. (for loop)
#Then ask user to type out one of them.
for symbol in operations:
  print(symbol)
operation_symbol = input("Pick an operation from the line above? ")

#step 5: take operation_symbol to pick out the value that's associated with it. 
calculator_function = operations[operation_symbol]
answer = calculator_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")


output:
  '''
What's the first number?: 23
What's the second number?: 55
+
-
*
/
Pick an operation from the line above? *
23 * 55 = 1265
  '''
