from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_soup(url, day=0):
    url = f"{url}/index.php?day={day}"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    # print(html)
    return BeautifulSoup(html, "html.parser")


def login():
    pass  # TODO


def logout():
    pass  # TODO
