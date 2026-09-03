
def add_employee():
    employee_id = len(employee_list) + 101
    name = input("Enter Emmployee Name:")
    age = int(input("Enter Employee Age:"))
    department = input("Enter Employee Department")
    salary = float(input("Enter Employee Salary:"))
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
    print(f"Employee age:  {employee_list[selected]['age']}")
    print(f"Employee salary:  {employee_list[selected]['salary']}")


def search_employee(employee_id):
    found = False
    for i in range(len(employee_list)):
        if employee_id == employee_list[i]["id"]:
            view_employees(i)
            found = True
            break
    if not found:
        print("Employee ID not found")

employee_list = []

while True:
    print("1-Add, 2-View, 3-Search, 4-exit")
    choice = input("\n Enter your choice (1-4): ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        if len(employee_list) > 0:
            selected = int(input(f"Select which employee want to show out of total {len(employee_list)}: "))
            view_employees(selected)
        else:
            print("No Employee exist")

    elif choice == "3":
        if len(employee_list) > 0:
            search_employee(101)
        else:
            print("No Employee exist")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
