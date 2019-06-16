import requests as req
from bs4 import BeautifulSoup
def Main(query):
    url = "https://ko.wikipedia.org/wiki/"
    #query=input("검색할 대상 : ")

    html = req.get(url + query)

    bs = BeautifulSoup(html.text)

    table = bs.find("table",{"class" : "infobox"})
    trs = table.find_all("tr")
    #print(trs)
    for tr in trs:
        if "교장" in str(tr):
            td = tr.find("td")
            #print(td.text)
            return td.text

if __name__ == '__main__':
    url ="https://ko.wikipedia.org/wiki/경기도의_고등학교_목록"
    html = req.get(url)
    bs = BeautifulSoup(html.text)
    div = bs.find("div", {"class" : "mw-parser-output"})
    ps = div.find_all("p");
    data =[]
    for p in ps:
        a = p.find_all("a")
        data+=a
    results = []
    for s in data:
        results.append(s.text)
    
    principal = {}
    for school in results:    
        try:
            re=Main(school)
            if re is not None:
                principal[school]=re.strip()
        except:
            pass
    print(principal)