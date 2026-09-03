class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("name is", self.name, "age", self.age)


class employee(person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        super().info()
        print("employee-id:", self.employee_id, "salary:", self.salary)


class manager(employee):
    def __init__(self, name, age, employee_id, salary, team_size, department):
        super().__init__(name, age, employee_id, salary)
        self.team_size = team_size
        self.department = department

    def display_manager_info(self):
        super().display_employee_info()
        print("team size:", self.team_size, "department:", self.department)

    def calculate_bonus(self):
        print("bonus:", self.team_size * 1000)


person1 = person("Maira", 21)
person1.info()

employee1 = employee("Ali", 30, 3215, 50000)
employee1.display_employee_info()

manager1 = manager("Sara", 35, 101, 80000, 10, "CS")
manager1.display_manager_info()
manager1.calculate_bonus()