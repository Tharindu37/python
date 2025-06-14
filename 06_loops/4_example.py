x = [1, 2, 3, 4, 5, 10, -9,11, 8]

sum = 0
avg = 0
for i in x:
    sum+=i
print("Sum: ", sum)
print("Avg: ", sum/len(x))

max = x[0]
for i in range(1, len(x)):
    if x[i]>max:
        max = x[i]
        
print("Max: ", max)

min = x[0]
for i in range(1, len(x)):
    if x[i]< min:
        min = x[i]
        
print("Min: ", min)


y = [1, 2, 3, 4, 5, 1, 3]

z = []
for i in y:
    if i not in z:
        z.append(i)
print("Y: ",y)       
print("Z: ",z)

count = 0
sum = 0
while count < len(z):
    sum += z[count]
    count +=1
    
print(sum)