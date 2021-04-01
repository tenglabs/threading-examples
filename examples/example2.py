import os
import urllib.request
from threading import Thread
 
class DownloadThread(Thread):

    
    def __init__(self, url, name):

        Thread.__init__(self)
        self.name = name
        self.url = url
    
    def run(self):

        handle = urllib.request.urlopen(self.url)
        fname = os.path.basename(self.url)
    
        with open(fname, "wb") as f_handler:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f_handler.write(chunk)
        
        msg = "%s downloaded %s!" % (self.name, self.url)
        print(msg)
 
 
def main(urls):

    for item, url in enumerate(urls):
        name = "Поток %s" % (item+1)
        thread = DownloadThread(url, name)
        thread.start()
 
if __name__ == "__main__":
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
 
    main(urls)