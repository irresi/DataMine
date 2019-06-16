import requests as req
from bs4 import BeautifulSoup
import urllib
def get_img(URL, NAME):
    try:
        urllib.request.urlretrieve(URL, "images\\" + NAME + ".png")
        print("Save " + NAME + " ...")
        return True
    except:
        print("ERROR : " + NAME + " has a problem and does not save ...")
        return False
if __name__ == '__main__':
    url = "https://www.google.com/search?q="
    query = input("검색어 입력 : ")
    target = "&tbm=isch"
    html = req.get(url + query + target)
    bs = BeautifulSoup(html.text)
    divs = bs.find_all("div", {"class" : "jscontroller"})
    print(divs)
