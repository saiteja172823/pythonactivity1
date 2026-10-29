

patients = []

n = int(input("Enter number of patients: "))

for i in range(n):
    print("\nEnter details for Patient", i + 1)

    name = input("Enter patient name: ")
    consultation = float(input("Consultation charges: "))
    diagnostic = float(input("Diagnostic charges: "))
    treatment = float(input("Treatment charges: "))
    age = int(input("Enter patient age: "))
    income = float(input("Enter annual family income: "))

  
    if (consultation < 0 or diagnostic < 0
            or treatment < 0 or age < 0 or income < 0):
        print("Invalid input! Charges, age and income "
              "cannot be negative.")
        continue

  

    # Apply conditional concessions
    concession = 0

    if age >= 60:
        concession = total * 0.15
    elif income <= 200000:
        concession = total * 0.10

    final_bill = total - concession

    
    if income <= 200000:
        category = "Subsidized Patient"
    elif income <= 500000:
        category = "Standard Patient"
    else:
        category = "Full Payment Patient"

    
    patients.append({
        "name": name,
        "total": total,
        "concession": concession,
        "final_bill": final_bill,
        "category": category
    })


print("\n======= HOSPITAL BILLING REPORT =======")

for p in patients:
    print("\nPatient Name:", p["name"])
    print("Total Charges: Rs.", round(p["total"], 2))
    print("Concession: Rs.", round(p["concession"], 2))
    print("Final Bill: Rs.", round(p["final_bill"], 2))
    print("Patient Classification:", p["category"])

print("\nTotal patients processed:", len(patients))

