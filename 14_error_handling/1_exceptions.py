from os import path

file_name = "example.txt"

if path.exists(file_name):
    with open(file_name) as file:
        print(file.readline())
else:
    print("File does not exist")
    

x = 10
y = 10

try:
    result = x / y
    
    with open(file_name) as file:
        print(file.readline())
except ZeroDivisionError:
    print("Error: Division by zero")
except FileNotFoundError:
    print("Error: File not found")
except Exception as e:
    print("Error: ", e)
else:
    print("Result: ", result)
finally:
    print("Finally block")