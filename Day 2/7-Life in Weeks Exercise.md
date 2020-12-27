# Problem
https://waitbutwhy.com/2014/05/life-weeks.html

Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left.
Where x, y and z are replaced with the actual calculated numbers.

## Hint
- There are 365 days in a year, 52 weeks in a year and 12 months in a year.
- Try copying the example output into your code and replace the relevant parts so that the sentence is formated the same way.

## code
      # 🚨 Don't change the code below 👇
      age = input("What is your current age? ")
      # 🚨 Don't change the code above 👆

      #Write your code below this line 👇

      age_as_int = int(age)

      years_remaining = 90 - age_as_int
      x = years_remaining * 365
      y = years_remaining * 52
      z = years_remaining * 12

      #You have 12410 days, 1768 weeks, and 408 months left.
      print(f"You have {x} days, {y} weeks, and {z} months left")

output

    What is your current age? 67
    You have 8395 days, 1196 weeks, and 276 months left

## My answer

    # 🚨 Don't change the code below 👇
    age = input("What is your current age? ")
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇

    x = (90 - int(age)) * 365
    y = (90 - int(age)) * 52
    z = (90 - int(age)) * 12

    #You have 12410 days, 1768 weeks, and 408 months left.
    print(f"You have {x} days, {y} weeks, and {z} months left")
    
output

    What is your current age? 27
    You have 22995 days, 3276 weeks, and 756 months left
    
    
