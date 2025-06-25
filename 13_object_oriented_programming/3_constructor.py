class Dog:
    name = ""
    age = 0
    
    # Constructor
    def __init__(self, name="Unknown"):
        self.name = name
    
    def set_name(self, name):
        self.name = name
    
    def bark(self, sound="Woof!"):
        print(sound)
        
    def walk(self):
        print(f"{self.name} is walking.")

dog1 = Dog()

# dog1.name = "Buddy"
dog1.set_name("Buddy")
dog1.walk()

dog2 = Dog("Max")
# dog2.set_name("Max")
dog2.walk()