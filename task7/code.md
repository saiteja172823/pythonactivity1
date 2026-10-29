

## 1. Problem Statement

Develop a Python program to generate a retail invoice for multiple products. The program should calculate product costs based on quantity, apply category-specific taxes, provide discounts when the purchase amount reaches specified thresholds, enforce a maximum discount limit, and display an itemized invoice with the final payable amount.

## 2. Algorithm

1. Start the program.
2. Input the number of products.
3. For each product, input its name, category, price, and quantity.
4. Calculate the subtotal for each product.
5. Apply a discount based on the total purchase amount.
6. Limit the discount to the maximum permitted concession.
7. Calculate category-specific taxes.
8. Calculate the final payable amount.
9. Display the itemized invoice.
10. Display the subtotal, discount, tax, and final bill.
11. Stop.

## 3. Flowchart

```
             +-------------+
             |    START    |
             +-------------+
                    |
                    v
        +------------------------+
        | Input Number of        |
        | Products               |
        +------------------------+
                    |
                    v
        +------------------------+
        | Input Product Name,    |
        | Category, Price, Qty   |
        +------------------------+
                    |
                    v
        +------------------------+
        | Calculate Item         |
        | Subtotal               |
        +------------------------+
                    |
                    v
        +------------------------+
        | More Products?         |
        +------------------------+
              /           \
            Yes            No
             |              |
             v              v
       Input Next    +-------------------+
       Product       | Calculate Total   |
             |       | Subtotal          |
             +       +-------------------+
                             |
                             v
                  +----------------------+
                  | Apply Threshold      |
                  | Discount             |
                  +----------------------+
                             |
                             v
                  +----------------------+
                  | Apply Maximum        |
                  | Discount Limit       |
                  +----------------------+
                             |
                             v
                  +----------------------+
                  | Calculate Category   |
                  | Taxes                |
                  +----------------------+
                             |
                             v
                  +----------------------+
                  | Print Itemized       |
                  | Invoice              |
                  +----------------------+
                             |
                             v
                       +----------+
                       |   STOP   |
                       +----------+
```

## 4. Python Source Code

```
# Retail Billing with Multiple Discount RulesMAX_DISCOUNT = 500tax_rates = {    "food": 5,    "clothing": 12,    "electronics": 18,    "other": 10}products = []subtotal = 0total_tax = 0n = int(input("Enter number of products: "))# Input product detailsfor i in range(n):    print("\nProduct", i + 1)    name = input("Enter product name: ")    category = input(        "Enter category (food/clothing/electronics/other): "    ).strip().lower()    price = float(input("Enter unit price: Rs. "))    quantity = int(input("Enter quantity: "))    if category not in tax_rates:        print("Invalid category. Using 'other'.")        category = "other"    if price < 0 or quantity <= 0:        print("Invalid price or quantity. Product skipped.")        continue
```

## 5. Sample Input

```
Enter number of products: 3

Product 1
Enter product name: Rice
Enter category (food/clothing/electronics/other): food
Enter unit price: Rs. 1000
Enter quantity: 2

Product 2
Enter product name: Shirt
Enter category (food/clothing/electronics/other): clothing
Enter unit price: Rs. 800
Enter quantity: 2

Product 3
Enter product name: Headphones
Enter category (food/clothing/electronics/other): electronics
Enter unit price: Rs. 2000
Enter quantity: 1
```

## 6. Sample Output

```
===========================================================================
                       RETAIL INVOICE
===========================================================================
Product        Category          Qty    Amount  Discount     Tax     Total
---------------------------------------------------------------------------
Rice           food                2   2000.00    166.67   91.67   1925.00
Shirt          clothing            2   1600.00    133.33  176.00   1642.67
Headphones     electronics         1   2000.00    200.00  324.00   2124.00
---------------------------------------------------------------------------
Subtotal:              Rs. 5600.00
Discount (15%):         Rs. 500.00
Maximum Discount Limit: Rs. 500.00
Total Tax:              Rs. 591.67
Final Payable Amount:   Rs. 5691.67
===========================================================================
Thank you for shopping!
```


