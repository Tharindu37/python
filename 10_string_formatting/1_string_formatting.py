height = 176
name = "Tharindu"
message = "Hello "+ name + "! Your height is " + str(height)
print(message)

# 1
message = "Hello %s! Your height is %d" % (name, height)
print(message)

# 2
message = "Hello {}! Your height is {}".format(name, height)
print(message)

message = "Hello {0}! Your height is {0}".format(name, height)
print(message)

message = "Hello {}! Your height is {:05d}".format(name, height)
print(message)

# 3
message = f"Hello {name}! Your height is {height:05d}"