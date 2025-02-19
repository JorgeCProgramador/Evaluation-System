#The system must request the student's name.
student_name = str(input('Name of the student: '))

#The system must request for 3 student grades.
grade1 = float(input('Student first grade: '))
grade2 = float(input('Student second grade: '))
grade3 = float(input('Student third grade: '))

#The system must calculate the final grade, which will be the average of the 3 grades entered (sum of the 3 grades divided by 3).
sum_grade = grade1 + grade2 + grade3
total_grade = sum_grade / 3

#The system calculates if the final grade of the student con pass the subject or it has to repeat it
def grade(total_grade):
    if total_grade < 5:
        return "SUSPENDED"
    elif 5<= total_grade <7:
        return "PASS"
    elif 7<= total_grade <9:
        return "NOTABLE"
    elif total_grade >= 9:
        return "EXCELLENT"
    else:
        return "No valid grade"

#Now the system prints out the result
calification = grade(total_grade)
print("The student", student_name, "got", calification)