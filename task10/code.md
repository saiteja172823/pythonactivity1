


## 1. Problem Statement

Develop a Python program to calculate the total cost of organizing a campus event, including venue, equipment, catering, transport, and certificates. The program should calculate the participant contribution, determine any sponsorship shortfall, and identify the minimum number of registrations required to break even.

## 2. Algorithm

1. Start the program.
2. Input venue, equipment, catering, transport, and certificate costs.
3. Input the expected number of participants, registration fee per participant, and sponsorship amount.
4. Calculate the total event cost.
5. Calculate the total registration income.
6. Calculate the total available funds from registrations and sponsorships.
7. Determine the surplus or sponsorship shortfall.
8. Calculate the minimum registrations needed to break even.
9. Display the complete financial report.
10. Stop.

## 3. Flowchart

```
          +----------------------+
          |        START         |
          +----------------------+
                     |
                     v
          +----------------------+
          | Input Event Costs    |
          | and Funding Details  |
          +----------------------+
                     |
                     v
          +----------------------+
          | Calculate Total      |
          | Event Cost           |
          +----------------------+
                     |
                     v
          +----------------------+
          | Calculate Registration|
          | Income               |
          +----------------------+
                     |
                     v
          +----------------------+
          | Calculate Total      |
          | Available Funds      |
          +----------------------+
                     |
                     v
          +----------------------+
          | Funds >= Event Cost? |
          +----------------------+
               /           \
             Yes            No
              |              |
              v              v
       +-------------+  +----------------+
       | Calculate   |  | Calculate      |
       | Surplus     |  | Shortfall      |
       +-------------+  +----------------+
              |              |
              +-------+------+
                      |
                      v
          +----------------------+
          | Calculate Minimum    |
          | Registrations Needed |
          +----------------------+
                      |
                      v
          +----------------------+
          | Display Financial    |
          | Report               |
          +----------------------+
                      |
                      v
          +----------------------+
          |         STOP         |
          +----------------------+
```

## 4. Python Source Code

```
# Campus Event Financial Planningprint("===== CAMPUS EVENT FINANCIAL PLANNING =====")venue_cost = float(input("Enter venue cost: Rs. "))equipment_cost = float(input("Enter equipment cost: Rs. "))catering_cost = float(input("Enter catering cost per participant: Rs. "))transport_cost = float(input("Enter transport cost per participant: Rs. "))certificate_cost = float(input("Enter certificate cost per participant: Rs. "))participants = int(input("Enter expected number of participants: "))registration_fee = float(input("Enter registration fee per participant: Rs. "))sponsorship = float(input("Enter sponsorship amount: Rs. "))if (venue_cost < 0 or equipment_cost < 0 or catering_cost < 0        or transport_cost < 0 or certificate_cost < 0        or participants < 0 or registration_fee < 0        or sponsorship < 0):    print("Invalid input. Costs and amounts cannot be negative.")else:    # Fixed costs    fixed_cost = venue_cost + equipment_cost    # Variable cost per participant    variable_cost = catering_cost + transport_cost + certificate_cost    # Total event cost    total_cost = fixed_cost + variable_cost * participants    # Participant contributions    registration_income = participants * registration_fee    # Total available funds    total_funds = registration_income + sponsorship
```

## 5. Sample Input

```
Enter venue cost: Rs. 10000
Enter equipment cost: Rs. 5000
Enter catering cost per participant: Rs. 200
Enter transport cost per participant: Rs. 50
Enter certificate cost per participant: Rs. 20
Enter expected number of participants: 100
Enter registration fee per participant: Rs. 400
Enter sponsorship amount: Rs. 10000
```

## 6. Sample Output

```
========== EVENT FINANCIAL REPORT ==========
Venue Cost: Rs. 10000.0
Equipment Cost: Rs. 5000.0
Catering Cost: Rs. 20000.0
Transport Cost: Rs. 5000.0
Certificate Cost: Rs. 2000.0
Total Event Cost: Rs. 42000.0
Registration Income: Rs. 40000.0
Sponsorship: Rs. 10000.0
Total Available Funds: Rs. 50000.0
Surplus Amount: Rs. 8000.0
Status: EVENT IS FINANCIALLY VIABLE
Minimum Registrations to Break Even: 20
============================================
```

