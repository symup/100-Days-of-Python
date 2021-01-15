DAYS IN MONTH

#Step 1- First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." 
#it should return True if it is a leap year, and return False if it is not a leap year.
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        #print("Leap year.") 
        return True
      else:
        #print("Not leap year.")
        return False
    else:
      #print("Leap year.")
      return True
  else:
    #print("Not leap year.")
    return False

#step 2- create a function called days_in_month() which will take a year and a month as inputs, e.g.
#days_in_month(year=2022, month=2)

def days_in_month(year, month):

  if month > 12 or month < 1:
    return "Invalid month."

  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  #it will use this information to work out the number of days in the month, then return that as the output
  if is_leap(year) and month == 2:
    return 29
  return month_days[month-1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


output:
  '''
Enter a year: 2021
Enter a month: 2
28
  '''









