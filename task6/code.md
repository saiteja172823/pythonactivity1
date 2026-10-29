

## 1. Problem Statement

Develop a Python program to calculate railway fares for multiple passengers based on distance travelled, travel class, age-based concessions, reservation fees, and cancellation penalties. The program should calculate the final fare for each passenger and display the total amount payable or the refund amount if a ticket is cancelled.

## 2. Algorithm

1. Start the program.
2. Input the number of passengers.
3. For each passenger, input name, age, distance, travel class, and ticket status.
4. Calculate the base fare according to distance slabs.
5. Apply the travel class multiplier.
6. Apply age-based concessions:
   - Children aged 5–11: 50% concession.
   - Senior citizens aged 60 or above: 40% concession.
   - Other passengers: no concession.
7. Add the reservation fee.
8. If the ticket is cancelled, calculate the cancellation penalty and refund amount.
9. Display each passenger's fare, penalty, and refund or payable amount.
10. Calculate and display the total amount.
11. Stop.

## 3. Flowchart

Copyable text flowchart:

```
          +------------------+
          |      START       |
          +------------------+
                   |
                   v
          +------------------+
          | Input Number of  |
          | Passengers       |
          +------------------+
                   |
                   v
          +------------------+
          | Input Passenger  |
          | Details          |
          +------------------+
                   |
                   v
          +------------------+
          | Calculate Base   |
          | Fare by Distance |
          +------------------+
                   |
                   v
          +------------------+
          | Apply Class      |
          | Multiplier       |
          +------------------+
                   |
                   v
          +------------------+
          | Apply Age        |
          | Concession       |
          +------------------+
                   |
                   v
          +------------------+
          | Add Reservation  |
          | Fee              |
          +------------------+
                   |
                   v
          +------------------+
          | Is Ticket        |
          | Cancelled?       |
          +------------------+
             /          \
           Yes           No
            |             |
            v             v
    +---------------+  +---------------+
    | Calculate     |  | Calculate     |
    | Penalty and   |  | Final Fare    |
    | Refund        |  +---------------+
    +---------------+         |
            |                 |
            +--------+--------+
                     |
                     v
          +------------------+
          | Display Passenger|
          | Fare Details     |
          +------------------+
                   |
                   v
          +------------------+
          | More Passengers? |
          +------------------+
             /          \
           Yes           No
            |             |
            v             v
      Input Next    +------------------+
      Passenger     | Display Total    |
            |       | Amount           |
            +       +------------------+
                            |
                            v
                   +------------------+
                   |       STOP       |
                   +------------------+
```

## 4. Python Source Code

```
# Railway Fare and Reservation Calculatorclass_rates = {    "Sleeper": 1.0,    "AC3": 2.0,    "AC2": 3.0,    "AC1": 4.0}reservation_fee = {    "Sleeper": 20,    "AC3": 40,    "AC2": 50,    "AC1": 60}def calculate_base_fare(distance):    if distance <= 100:        return distance * 1.0    elif distance <= 300:        return 100 * 1.0 + (distance - 100) * 1.5    else:        return 100 * 1.0 + 200 * 1.5 + (distance - 300) * 2.0def calculate_concession(age, fare):    if 5 <= age <= 11:        return fare * 0.50    elif age >= 60:        return fare * 0.40    else:        return 0def main():    n = int(input("Enter number of passengers: "))    total_payable = 0
```

## 5. Sample Input

```
Enter number of passengers: 2

Passenger 1
Enter passenger name: Ravi
Enter age: 30
Enter distance (km): 200
Enter travel class: Sleeper
Ticket status (Booked/Cancelled): Booked

Passenger 2
Enter passenger name: Sita
Enter age: 65
Enter distance (km): 150
Enter travel class: AC3
Ticket status (Booked/Cancelled): Cancelled
```

## 6. Sample Output

```
--- Passenger Fare Details ---
Name: Ravi
Base Fare: 250.0
Class Fare: 250.0
Age Concession: 0
Reservation Fee: 20
Final Fare: 270.0

--- Passenger Fare Details ---
Name: Sita
Base Fare: 175.0
Class Fare: 350.0
Age Concession: 140.0
Reservation Fee: 40
Cancellation Penalty: 62.5
Refund Amount: 187.5

======= FINAL SUMMARY =======
Total Booking Amount: Rs. 270.0
Total Refund Amount: Rs. 187.5
```


