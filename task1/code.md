

## 1. Problem Statement

Develop a Python program to allocate university scholarships to students based on their academic performance and eligibility criteria. The system should evaluate each applicant using:

- Aggregate marks: Minimum 75%.
- Subject-wise minimum marks: At least 60% in every subject.
- Attendance: At least 75%.
- Family annual income: Not more than ₹2,50,000.

The program must identify eligible students, rank them according to aggregate marks in descending order, and resolve ties using attendance percentage, followed by lower family income. If all three criteria are equal, the students are ranked alphabetically by name.

The program should display the eligible students in rank order and list the students who do not qualify, along with the reasons for ineligibility.

## 2. Algorithm

1. Start the program.
2. Read the number of applicants.
3. For each applicant, input the student's name, aggregate marks, subject-wise marks, attendance percentage, and annual family income.
4. Check whether the aggregate marks are at least 75%.
5. Check whether every subject mark is at least 60%.
6. Check whether attendance is at least 75%.
7. Check whether annual family income is at most ₹2,50,000.
8. If all conditions are satisfied, add the student to the eligible list. Otherwise, record the reason for rejection.
9. Sort eligible students using:
   - Higher aggregate marks first.
   - Higher attendance first when aggregate marks are equal.
   - Lower family income first when both are equal.
   - Alphabetical name order when all previous criteria are equal.
10. Assign ranks to eligible students.
11. Display the eligible students, their ranks, and the rejected applicants with their reasons.
12. Stop.

You can build this scholarship allocation program step by step. Choose how you would like help with the Python exercise.

# FLOW CHAT


             +-------------+
             |    START    |
             +-------------+
                    |
                    v
       +-------------------------+
       | Input Student Details   |
       +-------------------------+
                    |
                    v
       +-------------------------+
       | Check Marks, Attendance |
       | and Family Income       |
       +-------------------------+
                    |
                    v
          /-------------------\
         /  All Conditions    \
         \    Satisfied?      /
          \-------------------/
              /         \
            Yes          No
             |            |
             v            v
    +----------------+  +------------------+
    | Add Student to |  | Record Rejection |
    | Eligible List  |  | Reason           |
    +----------------+  +------------------+
             |            |
             +-----+------+
                   |
                   v
       +-------------------------+
       | Rank Eligible Students  |
       +-------------------------+
                   |
                   v
       +-------------------------+
       | Display Final Results   |
       +-------------------------+
                   |
                   v
             +-------------+
             |    STOP     |
             +-------------+

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


Note: This program ranks students but does not limit the number of scholarships awarded.
