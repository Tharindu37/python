import requests

response=requests.get('https://jsonplaceholder.typicode.com/posts')
print(response)
content = response.json()
print(len(content))