import requests
import threading

def getCats(n = 10, test = False):
    response = requests.get(f"https://api.thecatapi.com/v1/images/search?limit={n}")
    cats = response.json()

    for cat in cats:
        url = cat["url"]
        filename = str(url).split("/")[-1]

        if test:
            file = open(f"data/test/cat/{filename}", "wb")
        else:
             file = open(f"data/train/cat/{filename}", "wb")
        file.write(requests.get(url).content)
        file.close()

def getDogs(n = 10, test = False):
    response = requests.get(f"https://dog.ceo/api/breeds/image/random/{n}")
    dogs = response.json()["message"]

    for url in dogs:
        filename = str(url).split("/")[-1]

        if test:
            file = open(f"data/test/dog/{filename}", "wb")
        else:
             file = open(f"data/train/dog/{filename}", "wb")
        file.write(requests.get(url).content)
        file.close()

nImagesTrain = 1000
nImagesTest = 200

for i in range(int(nImagesTrain/50)):
    cats = threading.Thread(target=getCats, args=(50,))    
    dogs = threading.Thread(target=getDogs, args=(50,))
    cats.start()
    dogs.start()

for i in range(int(nImagesTest/50)):
    cats = threading.Thread(target=getCats, args=(50,True,))    
    dogs = threading.Thread(target=getDogs, args=(50,True,))
    cats.start()
    dogs.start()

while threading.activeCount() > 0:
    pass