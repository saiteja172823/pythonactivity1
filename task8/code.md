

## 1. Problem Statement

Develop a Python program to calculate manufacturing costs and profitability by considering raw material costs, labour charges, material wastage, machine costs, and selling prices. The program should calculate total production cost, profit, profit percentage, and determine whether the production meets the specified profit target.

## 2. Algorithm

1. Start the program.
2. Input the number of products to manufacture.
3. For each product, input its name, production quantity, material cost per unit, labour cost per unit, wastage percentage, machine cost per unit, and selling price per unit.
4. Calculate material wastage cost.
5. Calculate total material cost, labour cost, and machine cost.
6. Calculate total production cost and total sales revenue.
7. Calculate profit and profit percentage.
8. Compare the profit percentage with the specified target.
9. Display the cost breakdown and profitability status for each product.
10. Stop.

## 3. Flowchart

```
          +----------------------+
          |        START         |
          +----------------------+
                     |
                     v
          +----------------------+
          | Input Product Details|
          | and Profit Target    |
          +----------------------+
                     |
                     v
          +----------------------+
          | Calculate Material   |
          | Wastage Cost         |
          +----------------------+
                     |
                     v
          +----------------------+
          | Calculate Labour and |
          | Machine Costs        |
          +----------------------+
                     |
                     v
          +----------------------+
          | Calculate Total      |
          | Production Cost      |
          +----------------------+
                     |
                     v
          +----------------------+
          | Calculate Sales      |
          | Revenue and Profit   |
          +----------------------+
                     |
                     v
          +----------------------+
          | Profit Percentage >= |
          | Target Percentage?   |
          +----------------------+
               /           \
             Yes            No
              |              |
              v              v
      +---------------+  +----------------+
      | Target Met    |  | Target Not Met |
      +---------------+  +----------------+
              |              |
              +-------+------+
                      |
                      v
          +----------------------+
          | Display Cost and     |
          | Profit Report        |
          +----------------------+
                      |
                      v
          +----------------------+
          |         STOP         |
          +----------------------+
```

## 4. Python Source Code

```
# Manufacturing Cost and Profitability Analysisn = int(input("Enter number of products: "))profit_target = float(input("Enter target profit percentage: "))for i in range(n):    print("\nProduct", i + 1)    name = input("Enter product name: ")    quantity = int(input("Enter production quantity: "))    material_cost = float(input("Enter material cost per unit: Rs. "))    labour_cost = float(input("Enter labour cost per unit: Rs. "))    wastage_percent = float(input("Enter wastage percentage: "))    machine_cost = float(input("Enter machine cost per unit: Rs. "))    selling_price = float(input("Enter selling price per unit: Rs. "))    if (quantity <= 0 or material_cost < 0 or labour_cost < 0            or machine_cost < 0 or selling_price < 0            or not 0 <= wastage_percent <= 100):        print("Invalid input. Product skipped.")        continue    # Calculate costs    base_material_cost = material_cost * quantity    wastage_cost = base_material_cost * wastage_percent / 100    total_material_cost = base_material_cost + wastage_cost    total_labour_cost = labour_cost * quantity    total_machine_cost = machine_cost * quantity    total_cost = (        total_material_cost        + total_labour_cost        + total_machine_cost    )
```

## 5. Sample Input

```
Enter number of products: 1
Enter target profit percentage: 20

Product 1
Enter product name: Chair
Enter production quantity: 100
Enter material cost per unit: Rs. 200
Enter labour cost per unit: Rs. 50
Enter wastage percentage: 10
Enter machine cost per unit: Rs. 30
Enter selling price per unit: Rs. 400
```

## 6. Sample Output

```
------ MANUFACTURING REPORT ------
Product Name: Chair
Production Quantity: 100
Material Cost: Rs. 20000.0
Wastage Cost: Rs. 2000.0
Total Material Cost: Rs. 22000.0
Total Labour Cost: Rs. 5000.0
Total Machine Cost: Rs. 3000.0
Total Production Cost: Rs. 30000.0
Total Sales Revenue: Rs. 40000.0
Profit/Loss: Rs. 10000.0
Profit Percentage: 33.33 %
Status: PROFIT TARGET MET

Manufacturing analysis completed.
```

Formulae used:

- Wastage cost = Material cost × Wastage percentage ÷ 100
- Total production cost = Material cost + Wastage cost + Labour cost + Machine cost
- Profit = Sales revenue − Total production cost
- Profit percentage = (Profit ÷ Total production cost) × 100
