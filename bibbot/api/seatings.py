from bs4 import BeautifulSoup
from urllib.request import urlopen

# 1: BRuW, BSP, BNat, MedHB


def get_seats_1(location):
    # print(location)
    soup = get_soup(location['location']['url'])
    # weeklist = soup.select_one("table#raumbuchung").select_one("table.weeklist").select("tr")[1:]
    day_lim = soup.select("#layouttabelle tbody tr td table tr td p")[1].get_text()
    idx = day_lim.find("Montag")
    if idx == -1:
        idx = day_lim.find("Mo.")
    day_lim = day_lim[idx:].split(" ")[2]
    day_lim = day_lim[:-1] if day_lim[-1] == ")" else day_lim
    print(day_lim)


def get_soup(url, day=0):
    url = f"{url}/index.php?day={day}"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    return BeautifulSoup(html, "html.parser")
