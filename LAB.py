class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"


def sort_employees(employees, sorting_parameter):
    if sorting_parameter == 1:
        employees.sort(key=lambda emp: emp.age)
    elif sorting_parameter == 2:
        employees.sort(key=lambda emp: emp.name)
    elif sorting_parameter == 3:
        employees.sort(key=lambda emp: emp.salary)
    else:
        print("Invalid sorting parameter.")
        return


def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    print("Employee Table")
    print("Employee ID Name Age Salary (PM)")
    for emp in employees:
        print(emp)

    sorting_parameter = int(input("Enter sorting parameter (1. Age, 2. Name, 3. Salary): "))
    sort_employees(employees, sorting_parameter)

    print("\nSorted Employee Table")
    print("Employee ID Name Age Salary (PM)")
    for emp in employees:
        print(emp)


if __name__ == "__main__":
    main()
