x = {"Hello", "World", "Hello", "1", "1","2"}
print(x)
x.add("World") # hash function
print(x)
x.add("world")
print(x)
x.remove("1")
print(x)

y={"x", "y", "z", "2"}
print(x.union(y))
print(x | y)

print(x-y)
print(y-x)

print("1" in y)