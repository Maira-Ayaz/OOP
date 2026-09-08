class Calculator:

    def add(self, a, b, c=0):
        print("Sum =", a + b + c)
    def add(self, a, b,c=0):# latest function is call as python doesnt support method overloading
        print(a-b-c)


c = Calculator()

c.add(5, 10)       # 2 arguments
c.add(5, 10, 15)   # 3 arguments