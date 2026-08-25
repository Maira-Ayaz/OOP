

class car:
    def __init__(self,name):
        self._name = name
    def method(self):
        return self._name

car1 = car("toyota")
print(car1._name)
        
