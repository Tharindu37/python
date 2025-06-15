a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = [{i, value} for i, value  in enumerate(a) if i % 2 ==0]
print(a, b)