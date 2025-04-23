import requests

def getBreeds():
    url = "https://api.thecatapi.com/v1/breeds?limit=20";

    proxies = {
        "http": "http://user:pass@223.254.253.4:80",
        "https": "http://user:pass@223.254.253.4:80",
    }
    res = requests.get(url)
    # requests.get(url, proxies=proxies)
    return res.json()

def getCatsByBreed(breed):
    '''breed - id породы'''

    url = f"https://api.thecatapi.com/v1/images/search?limit=5&breed_ids={breed}"
    proxies = {
        "http": "http://user:pass@223.254.253.4:80",
        "https": "http://user:pass@223.254.253.4:80"
        }

    res = requests.get(url)
    # # requests.get(url, proxies=proxies)
    return res.json()



