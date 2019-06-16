import requests as req

sess = req.Session()

page = sess.get("https://dimigo.in")
print(page.text)
