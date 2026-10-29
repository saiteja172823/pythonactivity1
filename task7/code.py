

MAX_DISCOUNT = 500

tax_rates = {
    "food": 5,
    "clothing": 12,
    "electronics": 18,
    "other": 10
}

products = []
subtotal = 0
total_tax = 0

n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input(
        "Enter category (food/clothing/electronics/other): "
    ).strip().lower()

    price = float(input("Enter unit price: Rs. "))
    quantity = int(input("Enter quantity: "))

    if category not in tax_rates:
        print("Invalid category. Using other category.")
        category = "other"

    if price < 0 or quantity <= 0:
        print("Invalid price or quantity. Product skipped.")
        continue

    amount = price * quantity
    subtotal += amount

    products.append({
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "amount": amount
    })


if subtotal >= 5000:
    discount_rate = 15
elif subtotal >= 3000:
    discount_rate = 10
elif subtotal >= 1000:
    discount_rate = 5
else:
    discount_rate = 0

discount = min(subtotal * discount_rate / 100, MAX_DISCOUNT)


for product in products:
    if subtotal > 0:
        item_discount = discount * product["amount"] / subtotal
    else:
        item_discount = 0

    taxable_amount = product["amount"] - item_discount
    tax_rate = tax_rates[product["category"]]
    item_tax = taxable_amount * tax_rate / 100

    product["discount"] = item_discount
    product["tax"] = item_tax
    product["total"] = taxable_amount + item_tax

    total_tax += item_tax


print("\n" + "=" * 75)
print("                     RETAIL INVOICE")
print("=" * 75)

print(
    f"{'Product':<15}{'Category':<15}{'Qty':>5}"
    f"{'Amount':>10}{'Discount':>10}{'Tax':>8}{'Total':>10}"
)

print("-" * 75)

for product in products:
    print(
        f"{product['name']:<15}"
        f"{product['category']:<15}"
        f"{product['quantity']:>5}"
        f"{product['amount']:>10.2f}"
        f"{product['discount']:>10.2f}"
        f"{product['tax']:>8.2f}"
        f"{product['total']:>10.2f}"
    )

final_amount = subtotal - discount + total_tax

print("-" * 75)
print(f"Subtotal:              Rs. {subtotal:.2f}")
print(f"Discount Rate:         {discount_rate}%")
print(f"Discount Applied:      Rs. {discount:.2f}")
print(f"Maximum Discount:      Rs. {MAX_DISCOUNT:.2f}")
print(f"Total Tax:             Rs. {total_tax:.2f}")
print(f"Final Payable Amount:  Rs. {final_amount:.2f}")
print("=" * 75)
print("Thank you for shopping!")
