x = [12, 432, 564, 55, 66, 76]
print(x)
print(x[0])
print(x[1])
print(x[-1])
# print(x[10])
y  = x[0]
print(y)
x[0] = 2000
print(x)

x.append(300)
print(x)
x.clear()
print(x)
x.insert(2, 500)
print(x)
x.insert(2, 1000)
print(x)
x.insert(2, 2000)
print(x)
x.insert(2, 3000)
print(x)
x.remove(1000)
print(x)
x.pop(2)
print(x)

y = [1,2,3,4, 5]

print(x+y)
# print(x-y)

print(10 in x)
print(10 not in x)
print(not 10 in x)