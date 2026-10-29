

## 1. Problem Statement

Develop a Python program to analyze travel expenses in multiple currencies. The program should convert expenses into Indian Rupees using supplied exchange rates, calculate currency conversion fees, compare total spending against a planned budget, identify the largest expense category, and display the final travel budget report.

## 2. Algorithm

1. Start the program.
2. Input the travel budget in Indian Rupees and the conversion fee percentage.
3. Input the number of expense categories.
4. For each category, input the category name, amount, currency code, and exchange rate.
5. Convert each expense into Indian Rupees.
6. Calculate the conversion fee for each expense.
7. Calculate the total expense including fees.
8. Identify the largest expense category.
9. Compare the total expense with the planned budget.
10. Display the expense report, total spending, remaining budget or excess spending, and largest category.
11. Stop.

## 3. Flowchart

```
          +----------------------+
          |        START         |
          +----------------------+
                     |
                     v
          +----------------------+
          | Input Budget and     |
          | Conversion Fee Rate  |
          +----------------------+
                     |
                     v
          +----------------------+
          | Input Expense Details|
          | and Exchange Rates   |
          +----------------------+
                     |
                     v
          +----------------------+
          | Convert Expense into |
          | Indian Rupees        |
          +----------------------+
                     |
                     v
          +----------------------+
          | Calculate Conversion |
          | Fee                  |
          +----------------------+
                     |
                     v
          +----------------------+
          | Calculate Total      |
          | Expense              |
          +----------------------+
                     |
                     v
          +----------------------+
          | More Categories?     |
          +----------------------+
              /             \
            Yes              No
             |                |
             v                v
       Input Next      +-------------------+
       Category        | Find Largest      |
             |         | Expense Category  |
             +         +-------------------+
                              |
                              v
                   +-----------------------+
                   | Compare Spending      |
                   | with Budget           |
                   +-----------------------+
                              |
                              v
                   +-----------------------+
                   | Display Travel Budget |
                   | Report                |
                   +-----------------------+
                              |
                              v
                       +-------------+
                       |    STOP     |
                       +-------------+
```

## 4. Python Source Code

```
# Multi-Currency Travel Budget Analysisbudget = float(input("Enter travel budget in INR: Rs. "))fee_rate = float(input("Enter conversion fee percentage: "))n = int(input("Enter number of expense categories: "))expenses = []total_spending = 0for i in range(n):    print("\nExpense Category", i + 1)    category = input("Enter category name: ")    currency = input("Enter currency code: ").strip().upper()    amount = float(input("Enter expense amount in foreign currency: "))    exchange_rate = float(input("Enter exchange rate (INR per unit): "))    if amount < 0 or exchange_rate <= 0:        print("Invalid amount or exchange rate. Skipping category.")        continue    # Convert foreign currency to INR    converted_amount = amount * exchange_rate    # Calculate conversion fee    conversion_fee = converted_amount * fee_rate / 100    # Total expense including conversion fee    total_amount = converted_amount + conversion_fee    total_spending += total_amount    expenses.append({        "category": category,        "currency": currency,
```

## 5. Sample Input

```
Enter travel budget in INR: Rs. 50000
Enter conversion fee percentage: 2
Enter number of expense categories: 3

Expense Category 1
Enter category name: Hotel
Enter currency code: USD
Enter expense amount in foreign currency: 100
Enter exchange rate (INR per unit): 85

Expense Category 2
Enter category name: Food
Enter currency code: EUR
Enter expense amount in foreign currency: 80
Enter exchange rate (INR per unit): 90

Expense Category 3
Enter category name: Shopping
Enter currency code: GBP
Enter expense amount in foreign currency: 150
Enter exchange rate (INR per unit): 100
```

## 6. Sample Output

```
===========================================================================
             MULTI-CURRENCY TRAVEL BUDGET REPORT
===========================================================================
Category       Currency      Converted         Fee      Total INR
---------------------------------------------------------------------------
Hotel          USD             8500.00      170.00        8670.00
Food           EUR             7200.00      144.00        7344.00
Shopping       GBP            15000.00      300.00       15300.00
---------------------------------------------------------------------------

Largest Expense Category: Shopping
Amount: Rs. 15300.0

Planned Budget: Rs. 50000.0
Total Spending: Rs. 31314.0
Remaining Budget: Rs. 18686.0
Status: WITHIN BUDGET
===========================================================================
```
