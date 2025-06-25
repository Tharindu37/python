# class Dog:
#     pass

class Dog:
    name = ""
    age = 0
    
    def bark(self, sound="Woof!"):
        print(sound)

dog1 = Dog()
print(type(dog1))  

dog1.name = "Buddy"
dog1.age = 5
dog1.bark("Woof Woof!")
print(dog1.name, dog1.age)

dog2 = Dog()
print(dog2.name, dog2.age)

Dog.bark(dog2)