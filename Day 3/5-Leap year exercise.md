## 💪This is a Difficult Challenge 💪

# Instructions
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. 
The reason why we have leap years is really fascinating, this video does it more justice:

https://www.youtube.com/watch?v=xX96xng7sAE

This is how you work out whether if a particular year is a leap year.

    on every year that is evenly divisible by 4 
      except every year that is evenly divisible by 100 
        unless the year is also evenly divisible by 400
        
###### Example 1

    e.g. The year 2000:

    2000 ÷ 4 = 500 (Leap)
    2000 ÷ 100 = 20 (Not Leap)
    2000 ÷ 400 = 5 (Leap!)

    So the year 2000 is a leap year.


###### Exaample 2

    But the year 2100 is not a leap year because:

    2100 ÷ 4 = 525 (Leap)
    2100 ÷ 100 = 21 (Not Leap)
    2100 ÷ 400 = 5.25 (Not Leap)
    
## Code

    # 🚨 Don't change the code below 👇
    year = int(input("Which year do you want to check? "))
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇

    # on every year that is evenly divisible by 4 
    #   except every year that is evenly divisible by 100 
    #     unless the year is also evenly divisible by 400

    if year % 4 == 0:
            #print("Leap year")  
            if year % 100 == 0:
                    #print("not Leap year.")
                    if year % 400 == 0:
                            print("leap year.")
                    else: 
                            print("not leap year.")
            else:
                    print("leap year.")
    else:
            print("not leap year.") 

output

    Which year do you want to check? 2100
    not leap year.


## My code

    # 🚨 Don't change the code below 👇
    year = int(input("Which year do you want to check? "))
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇

    # on every year that is evenly divisible by 4 
    #   except every year that is evenly divisible by 100 
    #     unless the year is also evenly divisible by 400
    if year % 4 == 0:
            print("Leap year")  
            if year % 100 == 0:
                    print("not Leap year.")

                    if year % 400 == 0:
                            print("leap year.")
                    else:
                            print("not leap year")
            else:
                    print("leap year.")
    else:
            print("not leap year.")    


my output

    Which year do you want to check? 2020
    Leap year
    leap year
