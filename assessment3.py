#Python Program for the purpose of the DevOps Assignment 3

a1 = 89
a2 = 78
a3 = 67

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
else:
   grade = "ERROR"

print("Student Total Marks and Grade:", total_marks, grade)
