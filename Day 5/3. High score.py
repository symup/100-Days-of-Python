#You are going to write a program that calculates the highest score from a List of scores.

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#print(max(student_scores))
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")


OUTPUT:
  
  '''
Input a list of student scores 78 65 89 86 55 91 64 89
[78, 65, 89, 86, 55, 91, 64, 89]
The highest score in the class is: 91
  '''
