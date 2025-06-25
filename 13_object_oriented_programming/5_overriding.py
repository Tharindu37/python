class Animal:
    
    def __init__(self, breed):
        self.breed = breed
        
    def talk(self):
        print("Animal is talking.")
        
    def move(self):
        print("Animal is moving.")

class Dog(Animal):
    name = ""
    age = 0
    
    # Constructor
    def __init__(self, name="Unknown"):
        super(Dog, self).__init__("Dog")
        self.name = name
    
    def set_name(self, name):
        self.name = name
    
    def bark(self, sound="Woof!"):
        print(sound)
        
    def walk(self):
        print(f"{self.name} is walking.")
        
    def talk(self):
        super(Dog, self).talk()  # Call the parent class method
        print("Dog is barking.")

dog1 = Dog()

# dog1.name = "Buddy"
dog1.set_name("Buddy")
dog1.walk()
dog1.talk()  # Inherited method from Animal
print(dog1.breed)  # Inherited attribute from Animal


dog2 = Dog("Max")
# dog2.set_name("Max")
dog2.walk()