with open('data.txt', 'a') as file:
    x = [str(i*2) for i in range(0, 100)]
    msg = '\n'.join(x)
    file.write(msg)