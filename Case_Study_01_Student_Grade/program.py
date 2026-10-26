"""Case Study 01: Student Marks and Grade Calculator.

Syllabus concepts: input/output, variables, type conversion, operators,
for loop, if-elif-else, break, and lists.
"""

marks = []
total = 0
count = 0

for subject_number in range(1, 6):
    mark = int(input("Enter marks for subject " + str(subject_number) + " (0-100): "))

    if mark < 0 or mark > 100:
        print("Invalid marks. Enter a value from 0 to 100.")
        break

    marks.append(mark)
    total = total + mark
    count = count + 1

if count == 5:
    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print("\n--- Student Result ---")
    print("Marks:", marks)
    print("Total:", total, "/ 500")
    print("Percentage:", percentage, "%")
    print("Grade:", grade)
