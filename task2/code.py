

months = int(input("Enter number of months: "))
bills = []

for i in range(months):
    print("\nMonth", i + 1)
    units = float(input("Enter units consumed: "))

    
    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    else:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5

    fixed_charge = 50

    
    if units > 200:
        surcharge = energy * 0.05
    else:
        surcharge = 0

  
    if units <= 100:
        rebate = energy * 0.10
    else:
        rebate = 0

    total = energy + fixed_charge + surcharge - rebate
    bills.append(total)

    print("Energy Charge: Rs.", round(energy, 2))
    print("Fixed Charge: Rs.", fixed_charge)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", round(rebate, 2))
    print("Total Bill: Rs.", round(total, 2))


print("\n--- Monthly Bill Comparison ---")

for i in range(1, months):
    previous = bills[i - 1]
    current = bills[i]

    if previous == 0:
        if current > 0:
            print("Month", i + 1,
                  ": Unusual increase from zero bill")
        else:
            print("Month", i + 1, ": No increase")
    else:
        increase = ((current - previous) / previous) * 100

        print("Month", i + 1,
              ": Bill change =", round(increase, 2), "%")

        if increase > 30:
            print("Unusual increase detected!")
        else:
            print("No unusual increase.")

