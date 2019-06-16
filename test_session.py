import requests

s = requests.Session()

req = s.get('https://www.clien.net/service')

html = req.text
header = req.headers
status = req.status_code
is_ok = req.ok

with requests.Session() as s:
    req = s.get('https://www.clien.net/service/')
    html = req.text
    header = req.headers
    status = req.status_code
    is_ok = req.ok