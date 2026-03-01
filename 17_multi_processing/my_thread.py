from threading import Thread
import requests

class ImageDownloader(Thread):
    def __init__(self, thread_id, name, urls):
        super(ImageDownloader, self).__init__()
        self.id = thread_id
        self.urls = urls
        self.name = name
        
    def run(self):
        print(self.name)
        for i, url in enumerate(self.urls):
            self.downlaod_image(url, f"{self.id}-{i}")
        
    def downlaod_image(self, url, i):
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            r.raw.decode_content = True
            filename = f"images/{i}.png"
            with open(filename, 'wb') as f:
                f.write(r.content)
                
            print('Image sucessfully Downloaded: ', filename)