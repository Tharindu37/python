class Person:
    def __init__(self, name):
        self.name = name # Public attribute
        self.__age = 20 # Private attribute
        self._school = "University of Colombo" # Protected attribute
        
    def set_age(self, age):
        self.__age = age
        
    def get_age(self):
        return self.__age
        
    def sleep(self):
        print("Sleeping...", self.name)
        

class Student(Person):
    def __init__(self, name):
        super(Student, self).__init__(name)
        
    def print_age(self):
        print("Age is ", self.get_age())
        
    def print_school(self):
        print("School is ", self._school)
        

student = Student("Tharindu")
student.print_age()
student.print_school()

tharindu = Person("Tharindu")
tharindu.sleep()
tharindu.__age = 21
print("Name is ", tharindu.name)
print("Age is ", tharindu.get_age())
tharindu.set_age(22)
print("Age is ", tharindu.get_age())
print("Age is ", tharindu.__age)