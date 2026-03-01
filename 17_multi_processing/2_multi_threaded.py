# https://picsum.photos/id/237/200/300
from concurrent.futures import thread
import requests
import time
from my_thread import ImageDownloader

def get_image_urls(count):
    
    if count <= 0:
        print("Invalid count")
        return
    
    for i in range(0, count):
        url = f'https://picsum.photos/id/{i}/200/300'
        yield url
        
# def downlaod_image(url, i):
#     r = requests.get(url, stream=True)
#     if r.status_code == 200:
#         r.raw.decode_content = True
#         filename = f"images/{i}.png"
#         with open(filename, 'wb') as f:
#             f.write(r.content)
            
#         print('Image sucessfully Downloaded: ', filename)

urls = list(get_image_urls(100))

urls_list = []
num_threads = 10 
threads = []

for i in range(0, len(urls), num_threads):
    l = urls[i: i+num_threads]
    urls_list.append(l)
    
start = time.time_ns()

# for i, url in enumerate(urls):
#     downlaod_image(url, i)
        
for i in range(0, num_threads):
    thread = ImageDownloader(i, f"Thread-{i}", urls_list[i])
    thread.start()
    threads.append(thread)
    
for thread in threads:
    thread.join()
    
diff = time.time_ns() - start
print("Duration", diff/1000000)