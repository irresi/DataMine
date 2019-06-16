
from bs4 import BeautifulSoup
import requests as req
import urllib.request
#def 
if __name__ == '__main__':
    url = "http://www.weather.go.kr/weather/observation/currentweather.jsp"
    html = req.get(url)
    #print(html.text)
    bs = BeautifulSoup(html.text)   
    """tds = bs.find_all("td")
    lib = []
    for td in tds:
        print(td.text + 'EEE') #한글과 스페이스가 연속으로 or 한글과 한글이 연속
        if len(td.text)>1 and '가'<=td.text[1] and td.text[1]<='힣':
            lib.append(td.text)
    print(lib)"""
    trs = bs.find_all("tr")
    #trs 2부터
    print(trs[2])
    