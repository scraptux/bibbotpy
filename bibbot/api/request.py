from urllib import request
from bs4 import BeautifulSoup


def get_soup(url, day=0):
    url = f"{url}/index.php?day={day}"
    page = request.urlopen(url)
    # html = page.read().decode("utf-8")
    html = page.read()
    # print(html)
    return BeautifulSoup(html, "html.parser")
