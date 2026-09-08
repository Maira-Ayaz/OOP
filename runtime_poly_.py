class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


class Cow(Animal):
    def sound(self):
        print("Cow moos")


# One common function
def make_sound(animal):
    animal.sound()


# Calling the same function with different objects
make_sound(Dog())
make_sound(Cat())
make_sound(Cow())
make_sound(Animal())