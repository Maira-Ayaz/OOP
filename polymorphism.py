'Create a class named Flyer with a method fly'
'Create a class named Swimmer with a method swim'
'Create a class named Superhero that inherits from both Flyer and Swimmer and overrides both methods.' 
'Create an object of the Superhero class and call both methods'

class flyer:
    def fly(self):
        return "it flies"

class swimmer :
    def swim(self):
        return "it swims"

class superhero(flyer,swimmer):
    def fly(self):
        return "superhero can fly"

    def swim(self):
        return "superhero can swim"

superhero1 = superhero()
print(superhero1.swim())
print(superhero1.fly())
