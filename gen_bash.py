import requests, os
from bs4 import BeautifulSoup

r = requests.get('https://cut-and-go.org')
soup = BeautifulSoup(r.text, 'html.parser')
for div in soup.find_all(attrs={"class": "item"}):
    href = div.find(attrs={"class": "item-main"})['href'][1:]
    title = div.h3.string
    filename = href.split('/')[1]

#     adr = div['href'][1:]
    new = href+'/index.html'
    os.makedirs(os.path.dirname(new))
    f = open(new, 'w')
    text = '''<!DOCTYPE html>
<html lang="zh-tw">
<head>
    <meta charset="UTF-8" />
    <title>{}</title>
    <meta http-equiv=”refresh” content=”0; url=https://cut-and-go.org/{}/{}.pdf” />
    </style>
</head>
</html>'''.format(title, href, filename)
    f.write(text)
