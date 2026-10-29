# University Scholarship Allocation System

## 3. Flowchart

START

Input number of applicants and student details

Check aggregate ≥ 75%, all subjects ≥ 60%, attendance ≥ 75%, and income ≤ ₹2,50,000

YES

Add student to eligible list

NO

Record rejection reasons

Sort eligible students by marks, attendance, income, and name

Assign ranks and display results

STOP

## 4. Python Source Code

The following program uses lists, loops, conditional statements, and sorting.

```
# University Scholarship Allocation SystemMIN_AGGREGATE = 75MIN_SUBJECT_MARK = 60MIN_ATTENDANCE = 75MAX_INCOME = 250000eligible_students = []rejected_students = []n = int(input("Enter number of applicants: "))for i in range(n):    print(f"\nEnter details of student {i + 1}")    name = input("Student name: ")    aggregate = float(input("Aggregate marks (%): "))    subject_count = int(input("Number of subjects: "))    subject_marks = []    for j in range(subject_count):        mark = float(input(f"Subject {j + 1} marks (%): "))        subject_marks.append(mark)    attendance = float(input("Attendance (%): "))    income = float(input("Annual family income (Rs.): "))    reasons = []    if aggregate < MIN_AGGREGATE:        reasons.append("Aggregate below 75%")    if any(mark < MIN_SUBJECT_MARK for mark in subject_marks):        reasons.append("Subject mark below 60%")
```

## 5. Sample Input

```
Enter number of applicants: 4

Enter details of student 1
Student name: Asha
Aggregate marks (%): 90
Number of subjects: 3
Subject 1 marks (%): 85
Subject 2 marks (%): 90
Subject 3 marks (%): 95
Attendance (%): 90
Annual family income (Rs.): 180000

Enter details of student 2
Student name: Ravi
Aggregate marks (%): 90
Number of subjects: 3
Subject 1 marks (%): 88
Subject 2 marks (%): 92
Subject 3 marks (%): 90
Attendance (%): 95
Annual family income (Rs.): 200000

Enter details of student 3
Student name: Meena
Aggregate marks (%): 82
Number of subjects: 3
Subject 1 marks (%): 80
Subject 2 marks (%): 85
Subject 3 marks (%): 81
Attendance (%): 85
Annual family income (Rs.): 150000

Enter details of student 4
Student name: Kiran
Aggregate marks (%): 78
Number of subjects: 3
Subject 1 marks (%): 75
Subject 2 marks (%): 55
Subject 3 marks (%): 80
Attendance (%): 90
Annual family income (Rs.): 100000
```

## 6. Sample Output

```
===== ELIGIBLE STUDENTS =====
Rank | Name | Aggregate | Attendance | Income (Rs.)
1 | Ravi | 90.00% | 95.00% | 200000.00
2 | Asha | 90.00% | 90.00% | 180000.00
3 | Meena | 82.00% | 85.00% | 150000.00

===== REJECTED STUDENTS =====
Kiran: Subject mark below 60%
```

## 7. Result

The University Scholarship Allocation System successfully checks student eligibility using aggregate marks, subject-wise minimum marks, attendance, and family income. It ranks eligible students according to the predefined tie-breaking rules and displays rejection reasons for ineligible applicants.

Note: This program ranks students but does not limit the number of scholarships awarded.
