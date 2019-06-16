import requests

s=requests.Session()

req = s.get('https://www.benedu.co.kr/Index.aspx');

html = req.text
header = req.headers
status = req.status_code
is_ok = req.ok
print(req.text)