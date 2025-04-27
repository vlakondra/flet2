import requests

#main.py
def main(page: ft.Page):
    breeds = getBreeds()
    lv = ft.ListView(expand=False, spacing=10, width=202,height=400, horizontal=False)
    for breed in breeds:
        img = ft.Image(
            ...

#cats_api.py
def getBreeds():
    url = "https://api.thecatapi.com/v1/breeds?limit=20";
    res = requests.get(url)
    return res.json()
