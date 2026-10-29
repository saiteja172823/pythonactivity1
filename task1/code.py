

MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 60
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

eligible_students = []
rejected_students = []

n = int(input("Enter number of applicants: "))

for i in range(n):
    print(f"\nEnter details of student {i + 1}")

    name = input("Student name: ")
    aggregate = float(input("Aggregate marks (%): "))

    subject_count = int(input("Number of subjects: "))
    subject_marks = []

    for j in range(subject_count):
        mark = float(input(f"Subject {j + 1} marks (%): "))
        subject_marks.append(mark)

    attendance = float(input("Attendance (%): "))
    income = float(input("Annual family income (Rs.): "))

    reasons = []

    if aggregate < MIN_AGGREGATE:
        reasons.append("Aggregate below 75%")

    if any(mark < MIN_SUBJECT_MARK for mark in subject_marks):
        reasons.append("Subject mark below 60%")

    if attendance < MIN_ATTENDANCE:
        reasons.append("Attendance below 75%")

    if income > MAX_INCOME:
        reasons.append("Income above Rs. 250000")

    student = {
        "name": name,
        "aggregate": aggregate,
        "attendance": attendance,
        "income": income
    }

    if not reasons:
        eligible_students.append(student)
    else:
        rejected_students.append((name, reasons))


eligible_students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        s["name"].lower()
    )
)

print("\n===== ELIGIBLE STUDENTS =====")

if eligible_students:
    print("Rank | Name | Aggregate | Attendance | Income (Rs.)")

    for rank, s in enumerate(eligible_students, start=1):
        print(
            f"{rank} | {s['name']} | "
            f"{s['aggregate']:.2f}% | "
            f"{s['attendance']:.2f}% | "
            f"{s['income']:.2f}"
        )
else:
    print("No eligible students found.")

print("\n===== REJECTED STUDENTS =====")

if rejected_students:
    for name, reasons in rejected_students:
        print(f"{name}: {', '.join(reasons)}")
else:
    print("No rejected students.")

