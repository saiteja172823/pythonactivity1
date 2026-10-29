

## 1. Problem Statement

Develop a Python program to calculate household electricity bills based on monthly electricity consumption using a progressive slab tariff system. The program should apply different rates for different consumption slabs, add fixed charges, calculate surcharges, and apply rebates when applicable.

The system should also compare electricity bills across multiple months and identify unusual increases in the bill amount.

Assumed billing rules for this program:

| Electricity consumption  | Rate per unit |
| ------------------------ | ------------- |
| First 100 units          | ₹2.00         |
| Next 100 units (101–200) | ₹3.00         |
| Above 200 units          | ₹5.00         |

- Fixed charge: ₹50 per month.
- Surcharge: 5% of the energy charge if consumption exceeds 200 units.
- Rebate: 10% of the energy charge if consumption is at most 100 units.
- An unusual increase is identified when the bill rises by more than 30% compared with the previous month.

These are example rates for an academic program, not actual electricity tariffs.

## 2. Algorithm

1. Start.
2. Input the number of months.
3. For each month, input the household's electricity consumption in units.
4. Calculate the energy charge using progressive slabs:
   - First 100 units at ₹2 per unit.
   - Next 100 units at ₹3 per unit.
   - Remaining units at ₹5 per unit.
5. Add the fixed charge of ₹50.
6. If consumption exceeds 200 units, add a 5% surcharge on the energy charge.
7. If consumption is at most 100 units, apply a 10% rebate on the energy charge.
8. Calculate the final bill.
9. Compare each month's bill with the previous month's bill.
10. If the increase exceeds 30%, mark it as an unusual increase.
11. Display monthly consumption, energy charges, surcharges, rebates, and final bills.
12. Stop.

## 3. Flowchart

Copy the following flowchart directly into your assignment. It uses plain text so the alignment is preserved when copied.

```
             +-------------+
             |    START    |
             +-------------+
                    |
                    v
       +-------------------------+
       | Input Number of Months  |
       +-------------------------+
                    |
                    v
       +-------------------------+
       | Input Monthly Units     |
       +-------------------------+
                    |
                    v
       +-------------------------+
       | Calculate Energy Charge |
       | Using Progressive Slabs|
       +-------------------------+
                    |
                    v
       +-------------------------+
       | Add Fixed Charges       |
       +-------------------------+
                    |
                    v
       +-------------------------+
       | Calculate Surcharge     |
       | and Rebate              |
       +-------------------------+
                    |
                    v
       +-------------------------+
       | Calculate Final Bill    |
       +-------------------------+
                    |
                    v
       +-------------------------+
       | Compare with Previous    |
       | Month's Bill             |
       +-------------------------+
                    |
                    v
          /-------------------\
         / Bill Increase > 30%?\
         \                     /
          \-------------------/
              /         \
            Yes          No
             |            |
             v            v
    +----------------+  +----------------+
    | Mark Unusual   |  | Normal Increase|
    | Increase       |  | or No Increase |
    +----------------+  +----------------+
             |            |
             +-----+------+
                   |
                   v
       +-------------------------+
       | More Months Remaining?  |
       +-------------------------+
              |             |
             Yes            No
              |             |
              v             v
       Input Next Month  Display All Bills
              |             |
              +---> Repeat  v
                       +----------+
                       |   STOP   |
                       +----------+
```

## 4. Python Source Code

```
        surcharge = energy * SURCHARGE_RATE    else:        surcharge = 0    if units <= 100:        rebate = energy * REBATE_RATE    else:        rebate = 0    # Calculate final bill    total_bill = energy + FIXED_CHARGE + surcharge - rebate    consumptions.append(units)    energy_charges.append(energy)    surcharges.append(surcharge)    rebates.append(rebate)    bills.append(total_bill)# Display monthly bill detailsprint("\n========== BILL DETAILS ==========")print("Month | Units | Energy | Surcharge | Rebate | Total")for i in range(months):    print(        f"{i + 1:5} | {consumptions[i]:5.0f} | "        f"{energy_charges[i]:6.2f} | "        f"{surcharges[i]:9.2f} | "        f"{rebates[i]:6.2f} | {bills[i]:7.2f}"    )# Compare consecutive monthly billsprint("\n========== BILL COMPARISON ==========")if months < 2:    print("At least two months are needed for comparison.")for i in range(1, months):    previous_bill = bills[i - 1]    current_bill = bills[i]    if previous_bill > 0:        increase = (            (current_bill - previous_bill)            / previous_bill        ) * 100    else:        increase = 0 if current_bill == 0 else float("inf")    print(f"Month {i + 1}: Change = ", end="")    if increase == float("inf"):        print("New bill after a zero previous bill")        print("Unusual increase detected.")    else:        print(f"{increase:.2f}%")        if increase > INCREASE_LIMIT:            print("Unusual increase detected!")        else:            print("No unusual increase.")
```

## 5. Sample Input

```
Enter number of months: 3

Month 1
Enter electricity units consumed: 80

Month 2
Enter electricity units consumed: 150

Month 3
Enter electricity units consumed: 250
```

## 6. Sample Output

```
========== BILL DETAILS ==========
Month | Units | Energy | Surcharge | Rebate | Total
    1 |    80 | 160.00 |      0.00 |  16.00 |  194.00
    2 |   150 | 350.00 |      0.00 |   0.00 |  400.00
    3 |   250 | 750.00 |     37.50 |   0.00 |  837.50

========== BILL COMPARISON ==========
Month 2: Change = 106.19%
Unusual increase detected!
Month 3: Change = 109.38%
Unusual increase detected!
``
