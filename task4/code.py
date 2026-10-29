

n = int(input("Enter number of employees: "))

for i in range(n):
    print("\nEmployee", i + 1)

    name = input("Enter employee name: ")
    basic = float(input("Enter basic pay: "))
    overtime = float(input("Enter overtime hours: "))
    incentives = float(input("Enter incentives: "))

    if basic < 0 or overtime < 0 or incentives < 0:
        print("Invalid input! Values cannot be negative.")
        continue

  
    allowances = basic * 0.20
    overtime_pay = overtime * 200

    gross = basic + allowances + overtime_pay + incentives

    
    if gross <= 10000:
        deduction = 0
    elif gross <= 20000:
        deduction = (gross - 10000) * 0.05
    else:
        deduction = 500 + (gross - 20000) * 0.10

    net_salary = gross - deduction

    
    print("\n===== SALARY STATEMENT =====")
    print("Employee Name:", name)
    print("Basic Pay: Rs.", round(basic, 2))
    print("Allowances: Rs.", round(allowances, 2))
    print("Overtime Pay: Rs.", round(overtime_pay, 2))
    print("Incentives: Rs.", round(incentives, 2))
    print("Gross Salary: Rs.", round(gross, 2))
    print("Deductions: Rs.", round(deduction, 2))
    print("Net Salary: Rs.", round(net_salary, 2))
    print("============================")

