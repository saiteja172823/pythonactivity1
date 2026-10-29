

## 1. Problem Statement

Develop a Python program to calculate an employee's gross salary based on basic pay, allowances, overtime, and incentives. Apply progressive deductions according to salary slabs, calculate the net salary, and generate a formatted salary statement for each employee.

Assumed rules for this program:

- Allowances = 20% of basic pay.
- Overtime pay = overtime hours × ₹200 per hour.
- Incentives are entered by the user.
- Progressive deductions:
  - First ₹10,000: 0%
  - Next ₹10,000: 5%
  - Remaining amount above ₹20,000: 10%
- Net salary = gross salary − deductions.

These are sample rules for an academic exercise, not official payroll or tax rates.

## 2. Algorithm

1. Start.
2. Input the number of employees.
3. For each employee, input name, basic pay, overtime hours, and incentives.
4. Validate that all numeric inputs are non-negative.
5. Calculate allowances as 20% of basic pay.
6. Calculate overtime pay at ₹200 per hour.
7. Calculate gross salary by adding basic pay, allowances, overtime pay, and incentives.
8. Calculate progressive deductions:
   - No deduction on the first ₹10,000.
   - 5% on the next ₹10,000.
   - 10% on the amount above ₹20,000.
9. Calculate net salary by subtracting deductions from gross salary.
10. Display the formatted salary statement.
11. Repeat for all employees.
12. Stop.

## 3. Flowchart — Copyable Format

```
             ( START )
                 |
                 v
       / Input Employee Details /
                 |
                 v
       +----------------------+
       | Validate Input Data  |
       +----------------------+
                 |
                 v
          < Invalid Input? >
             /         \
           Yes          No
            |            |
            v            v
      +------------+  +------------------+
      | Display    |  | Calculate        |
      | Error      |  | Allowances       |
      +------------+  +------------------+
            |                  |
            |                  v
            |         +------------------+
            |         | Calculate Overtime|
            |         | Pay               |
            |         +------------------+
            |                  |
            |                  v
            |         +------------------+
            |         | Calculate Gross  |
            |         | Salary           |
            |         +------------------+
            |                  |
            |                  v
            |         +------------------+
            |         | Calculate         |
            |         | Progressive       |
            |         | Deductions        |
            |         +------------------+
            |                  |
            |                  v
            |         +------------------+
            |         | Calculate Net    |
            |         | Salary            |
            |         +------------------+
            |                  |
            |                  v
            |         / Print Salary /
            |           Statement
            |                  |
            +------------------+
                               |
                               v
                            ( STOP )
```

To copy it, select the text inside the code block and press `Ctrl + C`. Paste into Word or Notepad and use the Consolas font to preserve alignment.

## 4. Python Source Code

```
# Employee Payroll and Deduction Analysisn = int(input("Enter number of employees: "))for i in range(n):    print("\nEnter details for Employee", i + 1)    name = input("Employee name: ")    basic = float(input("Basic pay: Rs. "))    overtime_hours = float(input("Overtime hours: "))    incentives = float(input("Incentives: Rs. "))    # Validate inputs    if basic < 0 or overtime_hours < 0 or incentives < 0:        print("Invalid input! Values cannot be negative.")        continue    # Calculate allowances and overtime    allowances = basic * 0.20    overtime_pay = overtime_hours * 200    # Calculate gross salary    gross = basic + allowances + overtime_pay + incentives    # Calculate progressive deductions    if gross <= 10000:        deduction = 0    elif gross <= 20000:        deduction = (gross - 10000) * 0.05    else:        deduction = (10000 * 0.05) + ((gross - 20000) * 0.10)    # Calculate net salary    net_salary = gross - deduction
```

## 5. Sample Input

```
Enter number of employees: 2

Enter details for Employee 1
Employee name: Ravi
Basic pay: Rs. 25000
Overtime hours: 5
Incentives: Rs. 2000

Enter details for Employee 2
Employee name: Sita
Basic pay: Rs. 8000
Overtime hours: 2
Incentives: Rs. 500
```

## 6. Sample Output

```
========== SALARY STATEMENT ==========
Employee Name   : Ravi
Basic Pay       : Rs. 25000.0
Allowances      : Rs. 5000.0
Overtime Pay    : Rs. 1000.0
Incentives      : Rs. 2000.0
--------------------------------------
Gross Salary    : Rs. 33000.0
Deductions      : Rs. 1800.0
Net Salary      : Rs. 31200.0
======================================

========== SALARY STATEMENT ==========
Employee Name   : Sita
Basic Pay       : Rs. 8000.0
Allowances      : Rs. 1600.0
Overtime Pay    : Rs. 400.0
Incentives      : Rs. 500.0
--------------------------------------
Gross Salary    : Rs. 10500.0
Deductions      : Rs. 25.0
Net Salary      : Rs. 10475.0
======================================
``
