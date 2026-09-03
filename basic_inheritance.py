''' Student & Graduate

Description:

Create a parent class Student

with attributes: name and age
method show_details().
Create a child class GraduateStudent that inherits from Student

adds an attribute degree.
Override the show_details() method to also print the degree.

Create objects of both classes and show their details'''


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(self.name, self.age)


class GraduateStudent(Student):
    def __init__(self, name, age, degree):
        #super().__init__(name, age)
        Student.__init__(self, name, age)
        self.degree = degree

    def show_details(self):
        print(self.name, self.age, self.degree)


student1 = Student("Maira", 21)
gs1 = GraduateStudent("Maira", 21, "BSCS")

student1.show_details()
gs1.show_details()