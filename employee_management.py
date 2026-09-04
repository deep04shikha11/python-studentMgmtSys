def add_employee():
    employee_id = len(employee_list) + 101
    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ")
    salary = float(input("Enter Employee Salary: "))

    employee = {
        "id": employee_id,
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }

    employee_list.append(employee)
    print("Employee added successfully!")


def view_employees(selected):
    print(f"Employee name : {employee_list[selected]['name']}")
    print(f"Employee age: {employee_list[selected]['age']}")
    print(f"Employee department: {employee_list[selected]['department']}")
    print(f"Employee salary: {employee_list[selected]['salary']}")


def search_employee(Id):
    for i in range(len(employee_list)):
        if Id == employee_list[i]["id"]:
            view_employees(i)
            return

    print("Employee ID not found")


def updated_employee(Id, data):
    for i in range(len(employee_list)):
        if Id == employee_list[i]["id"]:
            employee_list[i]["name"] = data["name"]
            employee_list[i]["age"] = data["age"]
            employee_list[i]["department"] = data["department"]
            employee_list[i]["salary"] = data["salary"]

            print("Employee details updated successfully!")
            return

    print("Wrong Employee ID")


def delete_employee(id):
    for i in range(len(employee_list)):
        if id == employee_list[i]["id"]:
            employee_list.remove(employee_list[i])
            print("Employee removed successfully")
            break		

employee_list = []

while True:
    print("\n1-Add, 2-View, 3-Search, 4-Update, 5-Delete, 6-Exit")
    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        if len(employee_list) > 0:
            selected = int(input(f"Select which index you want to show out of total {len(employee_list)}: "))
            view_employees(selected)
        else:
            print("No Employee exist")

    elif choice == "3":
        if len(employee_list) > 0:
            selected_id = int(input("Enter Employee ID to be searched: "))
            search_employee(selected_id)
        else:
            print("No Employee exist")

    elif choice == "4":
        if len(employee_list) > 0:
            select_id = int(input("Enter Employee ID to update: "))

            name = input("Enter Employee Name: ")
            age = int(input("Enter Employee Age: "))
            department = input("Enter Employee Department: ")
            salary = float(input("Enter Employee Salary: "))

            employee = {
                "name": name,
                "age": age,
                "department": department,
                "salary": salary
            }

            updated_employee(select_id, employee)

        else:
            print("No Employee exist")

    elif choice == "5":
        if len(employee_list) > 0:
            select_id = int(input("Enter Employee ID to delete: "))
            delete_employee(select_id)
        else:
            print("No Employee exist")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
