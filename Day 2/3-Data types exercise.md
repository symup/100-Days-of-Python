# Problem
Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

## Hint
- Try to find out the data type of two_digit_number.
- Think about what you learnt about subscripting.
- Think about type conversion.

      # 🚨 Don't change the code below 👇
      two_digit_number = input("Type a two digit number: ")
      # 🚨 Don't change the code above 👆

      ####################################
      #Write your code below this line 👇

      #check type
      print(type(two_digit_number))

      first_digit = two_digit_number[0]
      second_digit = two_digit_number[1]

      # print(first_digit)
      # print(second_digit)

      result = int(first_digit) + int(second_digit)
      print(result)

output

      Type a two digit number: 26
      <class 'str'>
      8


# My answer:

      # 🚨 Don't change the code below 👇
      two_digit_number = input("Type a two digit number: ")
      # 🚨 Don't change the code above 👆

      ####################################
      #Write your code below this line 👇

      print(int(two_digit_number[0])+int(two_digit_number[1]))
      
output

    Type a two digit number: 26
    8
