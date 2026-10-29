

class_rates = {
    "Sleeper": 1.0,
    "AC3": 2.0,
    "AC2": 3.0,
    "AC1": 4.0
}

reservation_fee = {
    "Sleeper": 20,
    "AC3": 40,
    "AC2": 50,
    "AC1": 60
}

def calculate_base_fare(distance):
    if distance <= 100:
        return distance * 1.0
    elif distance <= 300:
        return 100 + (distance - 100) * 1.5
    else:
        return 100 + 200 * 1.5 + (distance - 300) * 2.0

def calculate_concession(age, fare):
    if 5 <= age <= 11:
        return fare * 0.50
    elif age >= 60:
        return fare * 0.40
    return 0

n = int(input("Enter number of passengers: "))

total_booking = 0
total_refund = 0

for i in range(n):
    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = float(input("Enter distance in km: "))

    print("Available classes: Sleeper, AC3, AC2, AC1")
    travel_class = input("Enter travel class: ").strip()

    if travel_class not in class_rates:
        print("Invalid travel class. Passenger skipped.")
        continue

    status = input("Ticket status (Booked/Cancelled): ").strip().lower()

    if distance <= 0 or age < 0:
        print("Invalid age or distance. Passenger skipped.")
        continue

    base_fare = calculate_base_fare(distance)
    class_fare = base_fare * class_rates[travel_class]
    concession = calculate_concession(age, class_fare)
    reservation = reservation_fee[travel_class]

    final_fare = class_fare - concession + reservation

    print("\n--- Fare Details ---")
    print("Passenger Name:", name)
    print("Base Fare: Rs.", round(base_fare, 2))
    print("Class Fare: Rs.", round(class_fare, 2))
    print("Age Concession: Rs.", round(concession, 2))
    print("Reservation Fee: Rs.", reservation)

    if status == "cancelled":
        penalty = final_fare * 0.25
        refund = final_fare - penalty
        total_refund += refund

        print("Cancellation Penalty: Rs.", round(penalty, 2))
        print("Refund Amount: Rs.", round(refund, 2))

    elif status == "booked":
        total_booking += final_fare
        print("Final Fare: Rs.", round(final_fare, 2))

    else:
        print("Invalid ticket status. Passenger skipped.")

print("\n===== FINAL SUMMARY =====")
print("Total Booking Amount: Rs.", round(total_booking, 2))
print("Total Refund Amount: Rs.", round(total_refund, 2))
