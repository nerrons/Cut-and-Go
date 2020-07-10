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
    <link rel="icon" type="image/x-icon" href="https://cut-and-go.org/img/icon.png" />
    <link rel="apple-touch-icon" href="https://cut-and-go.org/img/apple-touch-icon.png" />
    <title>{}</title>
    <meta name="description" content="{}" />
    <meta property="og:site_name" content="Cut-and-Go" />
    <meta property="og:title" content="Cut-and-Go" />
    <meta property="og:description" content="{}" />
    <meta property="og:image" content="https://cut-and-go.org/img/cover.png" />
    <meta name="twitter:card" content="summary" />
    <meta name="twitter:creator" content="@bufhdy" />
    <meta property="og:url" content="https://cut-and-go.org/" />
    <meta http-equiv=”refresh” content=”0;url=https://cut-and-go.org/{}/{}.pdf” />
    </style>
</head>
<body>
    <img src="to-be-continue.svg" id="text" />
</body>
</html>'''.format(title, title, title, href, filename)
    f.write(text)
