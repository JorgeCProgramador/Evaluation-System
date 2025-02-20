def calification_system():
    for i in range(5):
        name = str(input("Name of the student: "))
        note1 = float(input("What is the first grade of the student: "))
        note2 = float(input("What is the second grade of the student: "))
        note3 = float(input("What is the third grade of the student: "))
        sum = note1 + note2 + note3
        total_grade = sum/3
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
        calification = grade(total_grade)
        print(f'The final clification of {name.upper()} is {total_grade} that is {calification}')
calification_system()