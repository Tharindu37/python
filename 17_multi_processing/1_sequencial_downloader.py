# https://picsum.photos/id/237/200/300
import requests
import time

def get_image_urls(count):
    
    if count <= 0:
        print("Invalid count")
        return
    
    for i in range(0, count):
        url = f'https://picsum.photos/id/{i}/200/300'
        yield url
        
urls = get_image_urls(20)

start = time.time_ns()

for i, url in enumerate(urls):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        r.raw.decode_content = True
        filename = f"images/{i}.png"
        with open(filename, 'wb') as f:
            f.write(r.content)
            
        print('Image sucessfully Downloaded: ', filename)
        
diff = time.time_ns() - start
print("Duration", diff/1000000)