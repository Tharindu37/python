x = [12, 33, 44, 55, 643, 3, 4]


# count = 0
# while True:
#     if count==10:
#         break
#     print(count)
#     count+=1
    
    
count = 0
while True:
    count+=1
    if count%2==0:
        continue
    
    if count>10:
        break
    print(count)
    