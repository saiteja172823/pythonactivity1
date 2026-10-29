

budget = float(input("Enter travel budget in INR: Rs. "))
fee_rate = float(input("Enter conversion fee percentage: "))

n = int(input("Enter number of expense categories: "))

expenses = []
total_spending = 0

for i in range(n):
    print("\nExpense Category", i + 1)

    category = input("Enter category name: ")
    currency = input("Enter currency code: ").strip().upper()
    amount = float(input("Enter expense amount in foreign currency: "))
    exchange_rate = float(input("Enter exchange rate (INR per unit): "))

    if amount < 0 or exchange_rate <= 0:
        print("Invalid amount or exchange rate. Skipping category.")
        continue

    # Convert foreign currency to INR
    converted_amount = amount * exchange_rate

    # Calculate conversion fee
    conversion_fee = converted_amount * fee_rate / 100

    # Total expense including conversion fee
    total_amount = converted_amount + conversion_fee

    total_spending += total_amount

    expenses.append({
        "category": category,
        "currency": currency,
        "amount": amount,
        "converted": converted_amount,
        "fee": conversion_fee,
        "total": total_amount
    })

# Display itemized expense report
print("\n" + "=" * 75)
print("             MULTI-CURRENCY TRAVEL BUDGET REPORT")
print("=" * 75)

print(
    f"{'Category':<15}{'Currency':<10}{'Converted':>15}"
    f"{'Fee':>12}{'Total INR':>15}"
)
print("-" * 75)

for expense in expenses:
    print(
        f"{expense['category']:<15}"
        f"{expense['currency']:<10}"
        f"{expense['converted']:>15.2f}"
        f"{expense['fee']:>12.2f}"
        f"{expense['total']:>15.2f}"
    )


if expenses:
    largest = max(expenses, key=lambda x: x["total"])
    print("\nLargest Expense Category:", largest["category"])
    print("Amount: Rs.", round(largest["total"], 2))
else:
    print("\nNo valid expenses were entered.")


print("\nPlanned Budget: Rs.", round(budget, 2))
print("Total Spending: Rs.", round(total_spending, 2))

difference = budget - total_spending

if difference >= 0:
    print("Remaining Budget: Rs.", round(difference, 2))
    print("Status: WITHIN BUDGET")
else:
    print("Budget Exceeded By: Rs.", round(abs(difference), 2))
    print("Status: OVER BUDGET")

print("=" * 75)
