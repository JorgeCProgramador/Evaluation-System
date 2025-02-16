#The system must request the student's name.
student_name = str(input('Name of the student: '))

#The system must request for 3 student grades.
grade1 = float(input('Student first grade: '))
grade2 = float(input('Student second grade: '))
grade3 = float(input('Student third grade: '))

#The system must calculate the final grade, which will be the average of the 3 grades entered (sum of the 3 grades divided by 3).
sum_grade = grade1 + grade2 + grade3
total_grade = sum_grade / 3
#The system must display the student's name in capital letters.
student_capital = student_name.upper()
print('The student name is: ', student_capital)

#The system must display the student's final grade.
print(total_grade, 'is the finalgrade of', student_capital)