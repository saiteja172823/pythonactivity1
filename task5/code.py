

budget = float(input("Enter your budget (Rs.): "))
required_data = float(input("Enter required data (GB): "))
required_calls = int(input("Enter required call minutes: "))
required_validity = int(input("Enter required validity (days): "))

plan details: Name, Price, Data, Calls, Validity, Excess charge per GB
plans = [
    ("Basic", 199, 2, 500, 28, 20),
    ("Standard", 299, 5, 1000, 56, 15),
    ("Premium", 399, 10, 1500, 84, 10),
    ("Unlimited", 499, 20, 2000, 90, 5)
]

eligible_plans = []

print("\n===== MOBILE PLAN COMPARISON =====")

for plan in plans:
    name, price, data, calls, validity, rate = plan

    excess_data = max(0, required_data - data)
    excess_charge = excess_data * rate
    total_cost = price + excess_charge

    print("\nPlan:", name)
    print("Base Price: Rs.", price)
    print("Excess Data Charge: Rs.", round(excess_charge, 2))
    print("Total Cost: Rs.", round(total_cost, 2))

    if (calls >= required_calls and
            validity >= required_validity and
            total_cost <= budget):
        eligible_plans.append(
            (total_cost, name, data, calls, validity, excess_charge)
        )

print("\n===== FINAL RESULT =====")

if eligible_plans:
    eligible_plans.sort()

    cost, name, data, calls, validity, excess = eligible_plans[0]

    print("Most Economical Plan:", name)
    print("Total Cost: Rs.", round(cost, 2))
    print("Data Allowance:", data, "GB")
    print("Call Minutes:", calls)
    print("Validity:", validity, "days")
    print("Excess Charges: Rs.", round(excess, 2))
else:
    print("No eligible plan satisfies all constraints.")
