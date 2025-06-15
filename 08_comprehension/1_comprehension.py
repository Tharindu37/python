a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a

b.append(100)
a.append(200)

print(a)
print(b)

c = list(a)
c.append(300)
print(a)
print(c)

d = []
for i in a:
    d.append(i)
    
print(a, d)

# List comprehension
e = [i for i  in a]
print(a, e)


def is_odd(number):
    return number % 2 ==1

f = [is_odd(i) for i in a]
print(a, f)