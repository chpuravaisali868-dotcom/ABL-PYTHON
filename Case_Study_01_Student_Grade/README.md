# Case Study 01: Student Marks and Grade Calculator

## 1. Problem Statement
Create a Python program that accepts marks for five subjects and displays the total, percentage, and grade.

## 2. Objectives
- Practice input and output operations.
- Use type conversion and arithmetic operators.
- Store marks in a list.
- Use `if`, `elif`, and `else` to decide the grade.

## 3. Assumptions
- There are five subjects.
- Each subject is marked out of 100.
- Each mark must be an integer from 0 to 100.
- Grade bands used for this example:
  - 90% and above: A
  - 75% to below 90%: B
  - 60% to below 75%: C
  - 40% to below 60%: D
  - Below 40%: Fail
- These grade bands are examples; change them if your faculty specifies different rules.

## 4. Algorithm
1. Start.
2. Create an empty list for marks.
3. Repeat five times: read a mark, validate it, and add it to the list.
4. Calculate total marks.
5. Calculate percentage by dividing total by five.
6. Select the grade using conditional statements.
7. Display marks, total, percentage, and grade.
8. Stop.

## 5. Flowchart
Draw this flowchart using standard symbols in your report:

`START → Input mark (repeat for 5 subjects) → Validate mark → Calculate total → Calculate percentage → Determine grade → Display result → STOP`

For the validation step, draw a decision diamond: if a mark is outside 0–100, display “Invalid marks” and stop.

## 6. Pseudocode
```text
START
    marks = empty list

    REPEAT 5 times
        INPUT mark
        IF mark < 0 OR mark > 100
            DISPLAY "Invalid marks"
            STOP
        END IF
        ADD mark to marks
    END REPEAT

    total = SUM(marks)
    percentage = total / 5

    IF percentage >= 90
        grade = "A"
    ELSE IF percentage >= 75
        grade = "B"
    ELSE IF percentage >= 60
        grade = "C"
    ELSE IF percentage >= 40
        grade = "D"
    ELSE
        grade = "Fail"
    END IF

    DISPLAY marks, total, percentage, grade
STOP
```

## 7. Source Code
Run `program.py` using Python 3. The code is in the same folder.

## 8. Test Cases

| Test | Input marks | Expected result |
|---|---|---|
| 1 | 80, 75, 90, 85, 70 | Total 400; percentage 80%; grade B |
| 2 | 95, 95, 95, 95, 95 | Total 475; percentage 95%; grade A |
| 3 | 20, 30, 25, 35, 40 | Total 150; percentage 30%; grade Fail |
| 4 | 110, 80, 70, 60, 50 | Invalid marks message |

## 9. Sample Output
```text
Enter marks for subject 1 (0-100): 80
Enter marks for subject 2 (0-100): 75
Enter marks for subject 3 (0-100): 90
Enter marks for subject 4 (0-100): 85
Enter marks for subject 5 (0-100): 70

--- Student Result ---
Marks: [80, 75, 90, 85, 70]
Total: 400 / 500
Percentage: 80.00%
Grade: B
```

Run the program yourself and capture a screenshot of the output for your final report.

## 10. Conclusion
This program uses input/output, integer type conversion, a list, arithmetic operators, and conditional statements to calculate and display a student's result.
