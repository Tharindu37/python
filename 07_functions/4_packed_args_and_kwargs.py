    
def cal(*marks):
    sum =0
    for i in marks:
        sum += i
    print("Sum", sum)
    

cal(10, 20, 30, 40, 50)


def my_form(**params):
    for key, value in params.items():
        print(key, value)

my_form(name="Tharindu", height=123, city="kurunegala")
my_form(name="Lakshan", height=125)


def my_fun(name, height):
    print(name, height)
    
args = {
    'name':"Tharindu",
    'height': 234
}
my_fun(name="Lakshan", height=333)
my_fun(**args)