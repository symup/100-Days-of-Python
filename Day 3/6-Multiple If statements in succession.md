# Multiple if

    if condition1:
      do A
    if condition2:
      do B
    if condition3:
      do C

## example

    print("Welcome to the rollercoaster!")
    height = int(input("What is your height in cm? "))
    bill = 0

    if height >= 120:
      print("You can ride the rollercoaster!")
      age = int(input("What is your age? "))
      if age < 12:
        bill = 5
        print("Child tickets are $5.")
      elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
      elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
      else:
        bill = 12
        print("Adult tickets are $12.")

      wants_photo = input("Do you want a photo taken? Y or N. ")
      if wants_photo == "Y":
        bill += 3

      print(f"Your final bill is ${bill}")

    else:
      print("Sorry, you have to grow taller before you can ride.")
      
output

    Welcome to the rollercoaster!
    What is your height in cm? 150
    You can ride the rollercoaster!
    What is your age? 27
    Adult tickets are $12.
    Do you want a photo taken? Y or N. Y
    Your final bill is $15
