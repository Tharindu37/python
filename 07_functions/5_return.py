    
def cal(*marks):
    sum =0
    for i in marks:
        sum += i
    return sum
    

value=cal(10, 20, 30, 40, 50)
print("sum: ", value)