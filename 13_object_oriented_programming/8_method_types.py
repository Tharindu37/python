class Person:
    types = ["student", "teacher", "staff"] # Class variable
    
    def __init__(self, name):
        print("Person is created.")
        self.name = name
        
    def print_name(self): # Instance function
        print("Name is ", self.name)
        
    @classmethod
    def print_types(cls): # Class function
        print("Types are ", cls.types)
        
    @staticmethod # Static function
    def print_hello():
        print("Hello, world!")
        
tharindu = Person("Tharindu")
tharindu.print_name()
print(Person.types)
print(tharindu.types)
Person.print_types()    
Person.print_hello()