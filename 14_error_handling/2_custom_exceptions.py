class InvalidNameException(Exception):
    def __init__(self, message):
        self.message = message
        super(InvalidNameException, self).__init__(self.message)
        self.status_code = 400

class Person:
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age
        
    @staticmethod
    def get_person(name, age):
        if not name:
            print("Name is required")
            raise InvalidNameException("Name is required")
            
        if age< 0 or age > 120:
            print("Age is required")
            raise Exception("Age is required")
        
        return Person(name, age)
        
try:
    person = Person.get_person("", -10)
    print(person)
except Exception as e:
    print(e.status_code)