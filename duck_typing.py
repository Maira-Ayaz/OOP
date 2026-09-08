class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


class Duck:
    def sound(self):
        print("Quack")


def make_sound(animal):
    animal.sound()


make_sound(Dog())
make_sound(Cat())
make_sound(Duck())