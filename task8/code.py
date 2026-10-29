

n = int(input("Enter number of products: "))
profit_target = float(input("Enter target profit percentage: "))

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    quantity = int(input("Enter production quantity: "))
    material_cost = float(input("Enter material cost per unit: Rs. "))
    labour_cost = float(input("Enter labour cost per unit: Rs. "))
    wastage_percent = float(input("Enter wastage percentage: "))
    machine_cost = float(input("Enter machine cost per unit: Rs. "))
    selling_price = float(input("Enter selling price per unit: Rs. "))

    if (quantity <= 0 or material_cost < 0 or labour_cost < 0
            or machine_cost < 0 or selling_price < 0
            or not 0 <= wastage_percent <= 100
            or profit_target < 0):
        print("Invalid input. Product skipped.")
        continue

  
    base_material_cost = material_cost * quantity
    wastage_cost = base_material_cost * wastage_percent / 100
    total_material_cost = base_material_cost + wastage_cost

    
    total_labour_cost = labour_cost * quantity
    total_machine_cost = machine_cost * quantity

    
    total_cost = (
        total_material_cost
        + total_labour_cost
        + total_machine_cost
    )

    
    revenue = selling_price * quantity
    profit = revenue - total_cost

    if total_cost > 0:
        profit_percentage = (profit / total_cost) * 100
    else:
        profit_percentage = 0

    # Display report
    print("\n------ MANUFACTURING REPORT ------")
    print("Product Name:", name)
    print("Production Quantity:", quantity)
    print("Material Cost: Rs.", round(base_material_cost, 2))
    print("Wastage Cost: Rs.", round(wastage_cost, 2))
    print("Total Material Cost: Rs.", round(total_material_cost, 2))
    print("Total Labour Cost: Rs.", round(total_labour_cost, 2))
    print("Total Machine Cost: Rs.", round(total_machine_cost, 2))
    print("Total Production Cost: Rs.", round(total_cost, 2))
    print("Total Sales Revenue: Rs.", round(revenue, 2))
    print("Profit/Loss: Rs.", round(profit, 2))
    print("Profit Percentage:", round(profit_percentage, 2), "%")

    if profit_percentage >= profit_target:
        print("Status: PROFIT TARGET MET")
    else:
        print("Status: PROFIT TARGET NOT MET")

print("\nManufacturing analysis completed.")
