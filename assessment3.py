#Python Program for the purpose of the DevOps Assignment 3

a1 = int(input("Enter the Assessment 1 Marks:"))
a2 = int(input("Enter the Assessment 2 Marks:"))
a3 = int(input("Enter the Assessment 3 Marks:"))

if isinstance(a1, int) and isinstance(a2, int) and isinstance(a3, int):
   total_marks = (a1 * 20 + a2 * 40 + a3 *40)/100  
   grade = "F"
   if total_marks > 85 and total_marks <= 100:
      grade = "HD"
   elif total_marks > 75 and total_marks <=85:
      grade = "D"
   elif total_marks > 65 and total_marks <=75:
      grade = "C"
   elif total_marks >= 50 and total_marks <= 65:
      grade = "P"
   elif total_marks >= 0 and total_marks < 50:
      grade = "F"
   else:
      grade = "ERROR"
   return grade
else:
   return "ERROR"