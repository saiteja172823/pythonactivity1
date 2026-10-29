

## 1. Problem Statement

Develop a Python program to evaluate multiple mobile plans based on the user's data requirements, call minutes, validity period, and budget. The program should calculate excess usage charges, determine the total cost of each plan, check whether each plan satisfies all the given constraints, and identify the most economical eligible plan.

Assumed rules:

- Each mobile plan has a fixed price, data allowance, call minutes, validity, and excess data charge per GB.
- Excess data charges are added to the base plan price.
- A plan is eligible only if it satisfies the data, call minutes, validity, and budget requirements.
- The eligible plan with the lowest total cost is selected.

## 2. Algorithm

1. Start.
2. Input the user's budget, required data, required call minutes, and required validity.
3. Define the available mobile plans and their details.
4. For each plan, calculate excess data usage.
5. Calculate excess data charges and total cost.
6. Check whether the plan satisfies all usage, validity, and budget constraints.
7. If eligible, add the plan to the eligible plans list.
8. Repeat for all available plans.
9. If eligible plans exist, select the plan with the lowest total cost.
10. Otherwise, display that no eligible plan is available.
11. Display the plan comparison and final recommendation.
12. Stop.

## 3. Flowchart (Copyable)

```
              +-------------+
              |    START    |
              +-------------+
                     |
                     v
        +---------------------------+
        | Input Budget, Data, Calls |
        | and Required Validity     |
        +---------------------------+
                     |
                     v
        +---------------------------+
        | Load Available Mobile     |
        | Plan Details              |
        +---------------------------+
                     |
                     v
        +---------------------------+
        | Calculate Excess Data     |
        | Charges and Total Cost    |
        +---------------------------+
                     |
                     v
          +-----------------------+
          | Calls and Validity    |
          | Sufficient and Cost   |
          | Within Budget?        |
          +-----------------------+
               /           \
             Yes            No
              |              |
              v              v
       +--------------+  +----------------+
       | Store        |  | Reject Plan    |
       | Eligible Plan|  +----------------+
       +--------------+         |
              |                 |
              +--------+--------+
                       |
                       v
           +-----------------------+
           | More Plans Remaining? |
           +-----------------------+
                /            \
              Yes             No
               |               |
               v               v
         Evaluate Next    +------------------+
              Plan        | Eligible Plans   |
               |          | Available?       |
               +          +------------------+
                              /          \
                            Yes           No
                             |             |
                             v             v
                    +----------------+  +----------------+
                    | Select Lowest  |  | Display No     |
                    | Cost Plan      |  | Eligible Plan  |
                    +----------------+  +----------------+
                             |             |
                             v             |
                    +----------------+     |
                    | Display Result |     |
                    +----------------+     |
                             |             |
                             +------+------+
                                    |
                                    v
                              +-----------+
                              |   STOP    |
                              +-----------+
```

## 4. Python Source Code

```
# Multi-Plan Telecommunications Cost Optimizationbudget = float(input("Enter your budget (Rs.): "))required_data = float(input("Enter required data (GB): "))required_calls = int(input("Enter required call minutes: "))required_validity = int(input("Enter required validity (days): "))# Plan: Name, Price, Data, Calls, Validity, Excess rate per GBplans = [    ("Basic", 199, 2, 500, 28, 20),    ("Standard", 299, 5, 1000, 56, 15),    ("Premium", 399, 10, 1500, 84, 10),    ("Unlimited", 499, 20, 2000, 90, 5)]eligible_plans = []print("\n===== MOBILE PLAN COMPARISON =====")for plan in plans:    name, price, data, calls, validity, rate = plan    excess_data = max(0, required_data - data)    excess_charge = excess_data * rate    total_cost = price + excess_charge    print("\nPlan:", name)    print("Base Price: Rs.", price)    print("Excess Data Charge: Rs.", round(excess_charge, 2))    print("Total Cost: Rs.", round(total_cost, 2))    # Check eligibility    if (calls >= required_calls and            validity >= required_validity and            total_cost <= budget):
```

## 5. Sample Input

```
Enter your budget (Rs.): 400
Enter required data (GB): 5
Enter required call minutes: 800
Enter required validity (days): 28
```

## 6. Sample Output

```
===== MOBILE PLAN COMPARISON =====

Plan: Basic
Base Price: Rs. 199
Excess Data Charge: Rs. 60.0
Total Cost: Rs. 259.0

Plan: Standard
Base Price: Rs. 299
Excess Data Charge: Rs. 0.0
Total Cost: Rs. 299.0

Plan: Premium
Base Price: Rs. 399
Excess Data Charge: Rs. 0.0
Total Cost: Rs. 399.0

Plan: Unlimited
Base Price: Rs. 499
Excess Data Charge: Rs. 0.0
Total Cost: Rs. 499.0

===== RESULT =====
Most Economical Plan: Standard
Total Cost: Rs. 299.0
Data Allowance: 5 GB
Call Minutes: 1000
Validity: 56 days
Excess Charges: Rs. 0.0
```

