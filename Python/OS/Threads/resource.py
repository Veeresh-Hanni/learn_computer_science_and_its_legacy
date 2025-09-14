import threading
import requests

urls = ["https://example.com", "https://google.com", "https://openai.com"]

def fetch(url):
    response = requests.get(url)
    print(f"{url} -> {len(response.text)} characters")

threads = []
for url in urls:
    t = threading.Thread(target=fetch, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All pages fetched!")
