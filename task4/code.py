print("MOBILE PLAN COST OPTIMIZATION")

name = input("Enter Your Name: ")

data = float(input("Enter Required Data (GB): "))
calls = int(input("Enter Required Calling Minutes: "))
validity = int(input("Enter Required Validity Days: "))
budget = float(input("Enter Your Budget: "))

# Validate input
if data < 0 or calls < 0 or validity <= 0 or budget < 0:

    print("Invalid Input!")

else:

    # Mobile plans
    plans = [
        ["Basic", 199, 2, 500, 28],
        ["Standard", 299, 5, 1000, 28],
        ["Premium", 399, 10, 999999, 56],
        ["Unlimited", 599, 20, 999999, 84]
    ]

    best_plan = None
    lowest_cost = float('inf')

    # Check each plan
    for plan in plans:

        name_plan = plan[0]
        price = plan[1]
        plan_data = plan[2]
        plan_calls = plan[3]
        plan_validity = plan[4]

        # Check validity
        if plan_validity < validity:
            continue

        # Extra data charges
        extra_data = max(0, data - plan_data)
        data_charge = extra_data * 20

        # Extra calling charges
        extra_calls = max(0, calls - plan_calls)
        call_charge = extra_calls * 1

        # Total cost
        total = price + data_charge + call_charge

        # Check budget
        if total <= budget:

            if total < lowest_cost:

                lowest_cost = total
                best_plan = name_plan

                best_data_charge = data_charge
                best_call_charge = call_charge

    # Display result
    print("\n----- MOBILE PLAN RESULT -----")

    print("Customer Name:", name)

    if best_plan is not None:

        print("Best Plan:", best_plan)
        print("Plan Cost: Rs.", lowest_cost)
        print("Extra Data Charges: Rs.", best_data_charge)
        print("Extra Calling Charges: Rs.", best_call_charge)

        print("Total Cost: Rs.", lowest_cost)

    else:

        print("No Suitable Plan Found!")
        print("Please increase your budget or reduce usage.")

    print("\nThank You!")
