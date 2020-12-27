# problem
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of some's weight taking into account their height. e.g. 
If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

BMI = weight / (height x height)

## Hint
- Check the data type of the inputs.
- Try to use the exponent operator in your code.
- Remember PEMDAS.
- Remember to convert your result to a whole number (int).

      # Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

      # 🚨 Don't change the code below 👇
      height = input("enter your height in m: ")
      weight = input("enter your weight in kg: ")
      # 🚨 Don't change the code above 👆

      #Write your code below this line 👇

      BMI = int(weight) / float(height) ** 2
      print(BMI)

      bmi_as_int = int(BMI)
      print(bmi_as_int)

output

    enter your height in m: 1.8
    enter your weight in kg: 63
    19.444444444444443
    19

## my answer

    # 🚨 Don't change the code below 👇
    height = input("enter your height in m: ")
    weight = input("enter your weight in kg: ")
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇

    #check data type of input
    print(type(height))
    print(type(weight))

    new_height = float(height)
    new_weight = int(weight)

    bmi = (new_weight / new_height ** 2)
    print(int(bmi))
    
output

    enter your height in m: 1.8
    enter your weight in kg: 63
    <class 'str'>
    <class 'str'>
    19
