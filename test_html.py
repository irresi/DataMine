import requests as req
from bs4 import BeautifulSoup
def check(html_text):
    f = open("test.html", "w")
    f.write(html_text)
    f.close()

check(req.get("https://news.naver.com/main/read.nhn?m_view=1&includeAllCount=true&mode=LSD&mid=shm&sid1=100&oid=277&aid=0004469887").text)