drivers = {
    1: "Engaged: Pune → Hyderabad",
    2: "Available",
    3: "Engaged: Delhi → Jaipur",
    4: "Available",
    5: "Engaged: Bangalore → Chennai",
    6: "Available",
    7: "Available",
    8: "Available",
    9: "Available",
    10: "Available"
}

def assign_route(driver_id):
    if driver_id not in drivers:
        return "Invalid Driver ID. Please choose between 1–10."
    if "Available" in drivers[driver_id]:
        drivers[driver_id] = "Assigned: Mumbai → Delhi "
        return (f"Driver {driver_id} assigned to NEW ROUTE: Mumbai → Delhi.\n"
                f" Congratulations! You are eligible for a Secret Message "
                f"and Salary Increment.")
    else:
        return f" Driver {driver_id} is already {drivers[driver_id]}"

def check_status():
    print("\n=== Driver Status ===")
    for d_id, status in drivers.items():
        print(f"Driver {d_id}: {status}")
    print("=====================\n")

while True:
    print("=== XYZ Travel Agency ===")
    print("1. Assign New Route (Mumbai → Delhi)")
    print("2. Check Status of All Drivers")
    print("3. Exit")

    choice = int(input("Enter your choice (1–3): "))
    match choice:
        case 1:
            driver_id = int(input("Enter Driver ID (1–10): "))
            print(assign_route(driver_id))
        case 2:
            check_status()
        case 3:
            print("Exiting program... Thank you!")
            print(" === Visit Again === ")
            break
        case _:
            print("Invalid choice. Please select 1–3.")
