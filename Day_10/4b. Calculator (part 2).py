CALCULATOR - PART 2

#Calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

#Step 3: when type 'n', we need to use recursion: function call itself to start a new calc
def calculator():

  #Ask for num1
  num1 = int(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)

  #step 1: Set a flag called should_continue.
  should_continue = True

  while should_continue:

    #Here we select "+"
    operation_symbol = input("Pick an operation: ") 
    num2 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    #step 2: if user input "y"
    if input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()


output:
'''
What's the first number?: 1
+
-
*
/
Pick an operation: +
What's the next number?: 2
1 + 2 = 3
Type 'y' to continue calculating with 3, or 'n' to start a new calculation: y
Pick an operation: -
What's the next number?: 3
3 - 3 = 0
Type 'y' to continue calculating with 0, or 'n' to start a new calculation: n
What's the first number?: 
'''
