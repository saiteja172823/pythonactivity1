

print("===== CAMPUS EVENT FINANCIAL PLANNING =====")

venue_cost = float(input("Enter venue cost: Rs. "))
equipment_cost = float(input("Enter equipment cost: Rs. "))
catering_cost = float(input("Enter catering cost per participant: Rs. "))
transport_cost = float(input("Enter transport cost per participant: Rs. "))
certificate_cost = float(input("Enter certificate cost per participant: Rs. "))

participants = int(input("Enter expected number of participants: "))
registration_fee = float(input("Enter registration fee per participant: Rs. "))
sponsorship = float(input("Enter sponsorship amount: Rs. "))

if (venue_cost < 0 or equipment_cost < 0 or catering_cost < 0
        or transport_cost
