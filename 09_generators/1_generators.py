def get_odd_numbers(upper_limit):
    # odd = []
    for i in range(0, upper_limit):
        if i % 2 == 1:
            print("Odd", i)
            yield i
    #         odd.append(i)
    # return odd

print("Start")
x = get_odd_numbers(10)
print(x)
print("End")

for i in x:
    print(i)
    
# Can't run
for i in x:
    print(i)