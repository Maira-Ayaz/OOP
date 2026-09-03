'''task 
=================================

Step 1

Create a class named Agent.

Step 2

Inside Agent, create a class attribute named platform and set its value to "AI Platform".

Step 3

Create an __init__() method inside Agent that accepts name and model.

Step 4

Inside __init__(), store name and model as instance attributes.

Step 5

Create a method named describe() inside Agent.

Step 6

Inside describe(), print the agent's name and model.

Step 7

Create another class named ChatAgent that inherits from Agent.

Step 8

Create an __init__() method inside ChatAgent that accepts name, model, and language.

Step 9

Use super().__init__() inside ChatAgent to initialize the name and model attributes using the parent class.

Step 10

Inside ChatAgent, initialize the language attribute directly.

Step 11

Create a describe() method inside ChatAgent.

Step 12

Inside ChatAgent.describe(), use super() to call the parent's describe() method.

Step 13

After calling the parent method, print the language.

Step 14

Create an object of ChatAgent using:

Name: Customer Support Bot
Model: Gemini
Language: English
Step 15

Call the object's describe() method.

Step 16

Print the object's platform class attribute.

Step 17

Run your program and verify that the output contains:

Agent name
Model
Language
AI Platform'''
class agent:
    platform = "AI Platform"
    def __init__(self, name ,  model):
        self.name = name
        self.model = model 
    def describe(self):
        print ("The name of the agent is : ", (self.name) , "and model is :", (self.model))
class chatagent(agent):
    def __init__(self ,name , model , language):
        super().__init__(name , model )
        self.language = language
    def describe(self):
        super().describe()
        print("the language is : ", (self.language))


chatagent1 = chatagent("Customer support bot" , "gemini" , "english")
chatagent1.describe()
print("Platform : " , chatagent1.platform)