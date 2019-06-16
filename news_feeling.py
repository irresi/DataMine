import requests as req
from bs4 import BeautifulSoup

def get_comments(url):
    html = req.get(url)
    req.
    bs = BeautifulSoup(html.text)
    print(html.text)
    spans = bs.find_all("span", {"class" : "u_cbox_contents"})
    print(spans)
    for span in spans:
        print(span)

get_comments("https://news.naver.com/main/read.nhn?m_view=1&includeAllCount=true&mode=LSD&mid=shm&sid1=100&oid=277&aid=0004469887")