import urllib.request
from bs4 import BeautifulSoup
import re


def sq():
    html = urllib.request.urlopen("http://www.hakobus.jp/result.php?in=165&out=155").read()
    soup = BeautifulSoup(html, "html.parser")
    datas = soup.div.text
    texts = re.findall(r"\d\d:\d\d", datas)
    print(texts)


sq()
