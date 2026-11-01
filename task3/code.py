print("EMPLOYEE PAYROLL SYSTEM")

# Employee details
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")

basic = float(input("Enter Basic Salary: "))
hours = float(input("Enter Overtime Hours: "))

incentive = 1000

# Validate inputs
if basic < 0 or hours < 0:
    print("Invalid Input!")

else:

    # Calculate allowances
    allowance = basic * 0.20

    # Calculate overtime
    overtime = hours * 200

    # Calculate gross salary
    gross = basic + allowance + overtime + incentive

    # Progressive deductions
    if gross <= 20000:
        deduction = gross * 0.05

    elif gross <= 40000:
        deduction = gross * 0.10

    else:
        deduction = gross * 0.15

    # Calculate net salary
    net = gross - deduction

    # Salary statement
    print("\n----- SALARY STATEMENT -----")

    print("Employee Name:", name)
    print("Employee ID:", emp_id)
    print("Basic Salary: Rs.", basic)
    print("Allowances: Rs.", allowance)
    print("Overtime Payment: Rs.", overtime)
    print("Incentives: Rs.", incentive)

    print("----------------------------")
    print("Gross Salary: Rs.", gross)
    print("Deduction: Rs.", deduction)
    print("Net Salary: Rs.", net)

    print("----------------------------")
    print("Salary Calculated Successfully!")
