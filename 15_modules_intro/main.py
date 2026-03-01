from frontend.validators import is_valid_age
from backend.models import Person

age = "hi10"
print(is_valid_age(age))

person = Person("Tharindu", 24)
print(person.get_name())
print(person.get_age())