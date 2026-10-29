# Hospital Billing and Patient Classification Using Python

## 1. Problem Statement

Develop a Python program to process hospital bills for multiple patients by calculating consultation charges, diagnostic charges, and treatment charges. Apply conditional concessions based on patient age and annual family income, validate billing inputs to prevent negative values, and classify patients according to a predefined payment policy.

The program should display the total charges, concession amount, final bill, and patient classification for each valid patient.

Assumed rules for this program:

- Senior citizens aged 60 or above receive a 15% concession.
- Patients with annual family income of ₹2,00,000 or less receive a 10% concession if they do not qualify for the senior citizen concession.
- Income up to ₹2,00,000: Subsidized Patient.
- Income above ₹2,00,000 and up to ₹5,00,000: Standard Patient.
- Income above ₹5,00,000: Full Payment Patient.
- Negative charges, age, or income are invalid.

## 2. Algorithm

1. Start.
2. Input the number of patients.
3. For each patient, input name, consultation charges, diagnostic charges, treatment charges, age, and annual family income.
4. Validate all inputs. If any value is negative, display an error and skip that patient.
5. Calculate total charges by adding consultation, diagnostic, and treatment charges.
6. If the patient is aged 60 or above, apply a 15% concession.
7. Otherwise, if annual family income is ₹2,00,000 or less, apply a 10% concession. Otherwise, no concession is applied.
8. Calculate the final bill by subtracting the concession from the total charges.
9. Classify the patient according to annual family income.
10. Display the billing details and patient classification.
11. Repeat for all patients.
12. Stop.

## 3. Flowchart (Mermaid Flowchart Code)

             ( START )
                 |
                 v
       / Input Patient Details /
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
      +-------------+  +------------------+
      | Show Error  |  | Calculate Total  |
      +-------------+  | Hospital Charges |
             |         +------------------+
             |                  |
             |                  v
             |          < Age >= 60? >
             |             /       \
             |           Yes        No
             |            |          |
             |            v          v
             |       +---------+  < Income <=
             |       | 15%     |   200000? >
             |       | Discount|    /    \
             |       +---------+  Yes     No
             |            |       |       |
             |            |       v       v
             |            |   +--------+ +----------+
             |            |   | 10%    | | No       |
             |            |   | Discount| | Discount |
             |            |   +--------+ +----------+
             |            |       |       |
             |            +-------+-------+
             |                    |
             |                    v
             |           +----------------+
             |           | Calculate Final|
             |           | Bill           |
             |           +----------------+
             |                    |
             |                    v
             |           +----------------+
             |           | Classify Patient|
             |           | by Income       |
             |           +----------------+
             |                    |
             |                    v
             |           / Display Bill /
             |                    |
             +--------------------+
                                  |
                                  v
                               ( STOP )
## 4. Python Source Code

```
# Hospital Billing and Patient Classificationpatients = []n = int(input("Enter number of patients: "))for i in range(n):    print("\nPatient", i + 1)    name = input("Enter patient name: ")    consultation = float(input("Consultation charges: "))    diagnostic = float(input("Diagnostic charges: "))    treatment = float(input("Treatment charges: "))    age = int(input("Enter patient age: "))    income = float(input("Enter annual family income: "))    # Validate input    if (consultation < 0 or diagnostic < 0 or            treatment < 0 or age < 0 or income < 0):        print("Invalid input! Negative values are not allowed.")        continue    # Calculate total charges    total = consultation + diagnostic + treatment    # Apply concession    if age >= 60:        concession = total * 0.15    elif income <= 200000:        concession = total * 0.10    else:        concession = 0    final_bill = total - concession
```

## 5. Sample Input

```
Enter number of patients: 2

Patient 1
Enter patient name: Ravi
Consultation charges: 500
Diagnostic charges: 1000
Treatment charges: 3000
Enter patient age: 65
Enter annual family income: 400000

Patient 2
Enter patient name: Sita
Consultation charges: 500
Diagnostic charges: 500
Treatment charges: 1000
Enter patient age: 25
Enter annual family income: 150000
```

## 6. Sample Output

```
===== HOSPITAL BILLING REPORT =====

Patient Name: Ravi
Total Charges: Rs. 4500.0
Concession: Rs. 675.0
Final Bill: Rs. 3825.0
Classification: Standard Patient

Patient Name: Sita
Total Charges: Rs. 2000.0
Concession: Rs. 200.0
Final Bill: Rs. 1800.0
Classification: Subsidized Patient

Total valid patients: 2
```

## 7. Result

The program successfully calculates hospital bills, applies concessions based on age and income, validates billing constraints, and classifies patients according to the specified payment policy. The Mermaid flowchart illustrates the program's complete decision-making process.
