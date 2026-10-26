"""Case Study 01: Student Marks and Grade Calculator.

Concepts: input/output, type conversion, operators, lists, and if-elif-else.
"""

marks = []

for subject_number in range(1, 6):
    mark = int(input(f"Enter marks for subject {subject_number} (0-100): "))

    if mark < 0 or mark > 100:
        print("Invalid marks. Enter a value from 0 to 100.")
        raise SystemExit

    marks.append(mark)

total = sum(marks)
percentage = total / len(marks)

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
print(f"Percentage: {percentage:.2f}%")
print("Grade:", grade)
