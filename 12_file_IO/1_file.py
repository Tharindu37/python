"""
'r' = read only
'w' = write with truncate
'x' = open for exclusive creation
'a' = append
'b' = binary
't' = text mode
'+' = updating
"""
# file = open('data.txt')
# print(type(file))
# print(file)

# print(file.read(10))
# print(file.readline())

# while True:
#     contents = file.readline()
    
#     if not contents:
#         break
    
#     print(contents)
    
# for line in file:
#     print(line)



# file = open('data.txt', 'w')

# for i in range(0, 100):
#     file.write(str(i)+'\n')
    
# file.close()

file = open('data.txt', 'w')
msg = ', '.join([str(i) for i in range(0, 100)])

file.write(msg)
    
file.close()