#ASSOCIATION(HAS A / INDEPENDENT)
class Laptop:
    def __init__(self, brand):
        self.brand = brand

    def show_laptop(self):
        print("Laptop:", self.brand)


class Student:
    def __init__(self, name):
        self.name = name
        self.laptop = Laptop("Dell")   # Object of Laptop class

    def show_student(self):
        print("Student:", self.name)
        self.laptop.show_laptop()


s1 = Student("Maira")

s1.show_student()