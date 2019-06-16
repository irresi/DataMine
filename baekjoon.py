import requests as req
from bs4 import BeautifulSoup as bs

url = "https://www.acmicpc.net/login"
sess = req.Session()
response = sess.get(url)
headers = {'Date': 'Wed, 05 Jun 2019 05:14:36 GMT', 
'Content-Type': 'text/html; charset=UTF-8', 
'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 
'Set-Cookie': response.headers['Set-Cookie'],
'Cache-Control': 'no-store, no-cache, must-revalidate, no-cache="set-cookie"', 
'Expires': 'Thu, 19 Nov 1981 08:52:00 GMT', 
'Pragma': 'no-cache', 
'Referrer-Policy': 'strict-origin', 
'Vary': 'Accept-Encoding', 
'X-Content-Type-Options': 'nosniff', 
'X-Frame-Options': 'SAMEORIGIN', 
'X-XSS-Protection': '1; mode=block', 
'Strict-Transport-Security': 'max-age=15552000; includeSubDomains; preload', 
'Expect-CT': 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"', 
'Server': 'cloudflare', 'CF-RAY': '4e1fa9f48adad336-LAX', 
'Content-Encoding': 'gzip'}

data ={
    "login_user_id" : "skyblue02",
    "login_password" : ""
}

response = sess.post(url, data = data, headers = headers)
print(sess.get("https://www.acmicpc.net").text)