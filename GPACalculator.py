Rutgers = ["A", "BP", "B", "CP", "C", "D", "F"]
Reference = {"A":4, "B plus":3.5, "B":3, "C plus":2.5, "C":2, "D":1, "F":0}

Semesters = input('Enter number of completed semesters: ')

totalSemGP = 0
totalHours = 0
j = 1

while j <= float(Semesters):
    print('Semester ' + str(j))
    semesterGPA = input('Enter Semester GPA: ')
    Hours = input('Enter number of credit hours: ')

    semesterGradePoint = float(semesterGPA)*float(Hours)
    totalSemGP += semesterGradePoint
    totalHours += float(Hours)
    j += 1

Classes = input('Enter Number of Classes: ')

totalGrade = 0
totalCredits = 0
i = 1
print('Options: A, B plus, B, C plus, C, D, F')

while i <= float(Classes):
    print('Class ' + str(i))
    Grade = input('Enter Letter Grade: ')
    Credits = input('Enter Credits Earned: ')

    number = Reference[Grade]
    totalGrade += number*float(Credits)
    totalCredits += float(Credits)
    i += 1

GPA = (totalGrade + totalSemGP)/(totalCredits + totalHours)
print('GPA calculated: ',GPA)
