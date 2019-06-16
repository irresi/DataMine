
from bs4 import BeautifulSoup
import requests as req
import urllib.request
import html.parser
# socket < urllib < requests

def get_img(URL, NAME):
    
    urllib.request.urlretrieve(URL, "images\\" + NAME + ".png")
    print("Save " + NAME + " ...")
    return True
    #except:
    #    print("ERROR : " + NAME + " has a problem and does not save ...")
    #    return False

if __name__ == "__main__":
    url = "https://search.naver.com/search.naver?where=image&query="
    data = input("검색할 내용 입력 : ")
    html = req.get(url + data)
    bs = BeautifulSoup(html.text)
    div = bs.find("div", {"class" : "photo_grid _box"})
    imgs = div.find_all("img")
    
    cnt = 0
    for img in imgs:
        data = str(img)
        data = data.split("data-source=")
        url = data[1].split("\"")[1]
        print(url)
        get_img(url, str(cnt) + "번 이미지")
        cnt += 1