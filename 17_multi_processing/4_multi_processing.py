# https://picsum.photos/id/237/200/300
from concurrent.futures import thread
import requests
import time
from threading import Thread
import requests
from multiprocessing import Process
from multiprocessing import Queue

class ImageDownloader(Process):
    def __init__(self, thread_id, name, urls, results):
        super(ImageDownloader, self).__init__()
        self.id = thread_id
        self.urls = urls
        self.name = name
        self.success_count = 0
        self.results = results
        
    def run(self):
        print(self.name)
        for i, url in enumerate(self.urls):
            if self.downlaod_image(url, f"{self.id}-{i}"):
                self.success_count += 1
        # results.append(self.success_count)
        results.put(self.success_count)
        
    def downlaod_image(self, url, i):
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            r.raw.decode_content = True
            filename = f"images/{i}.png"
            with open(filename, 'wb') as f:
                f.write(r.content)
                
            print('Image sucessfully Downloaded: ', filename)
            return True
        else:
            print("Image Couldn't be retreived")
            return False

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
results = Queue()

for i in range(0, len(urls), num_threads):
    l = urls[i: i+num_threads]
    urls_list.append(l)
    

if __name__ == '__main__':
    
    start = time.time_ns()

    # for i, url in enumerate(urls):
    #     downlaod_image(url, i)
            
    for i in range(0, num_threads):
        thread = ImageDownloader(i, f"Thread-{i}", urls_list[i], results)
        thread.start()
        threads.append(thread)
        
    for thread in threads:
        thread.join()
        
    # for result in results:
    #     print(result)
        
    diff = time.time_ns() - start
    print("Duration", diff/1000000)