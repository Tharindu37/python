x = {"name":"tharindu", "age":20, "address":"galgamuwa"}
print(x)
print(x['name'])
x['school']='meegalewa'
print(x)
print('name' in x)
print('name' in x)
print('tharindu' in x)
print(x.keys())
print(x.values())
x['la']=['java', 'c', 'python']
print(x)
x['user']={'name':'ruwan', 'marks':22}
print(x)

y = x.get(3, 0)
print(y)


y = x.get('name', 0)
print(y)

del x['age']
print(x)

x.clear
print(x)

z = {
    "a": ['10', '20'],
    "b": [100, 200],
    "c": 20
}

a = z['a']
a.append('append data')
print(z)
