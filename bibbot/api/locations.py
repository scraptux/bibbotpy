from bs4 import BeautifulSoup
from urllib.request import urlopen

from PyInquirer import prompt, Separator


def choose_location():
    # get list of shit
    prompt_options, location_urls = get_available_locations()
    # display shit prompt
    question = [{
        'type': 'list',
        'name': 'location',
        'message': 'Bitte wähle die Bibliothek aus:',
        'choices': prompt_options
    }]
    answer = prompt(question)
    # return selected shit
    return {'location': location_urls[answer['location']]}


def get_available_locations():
    url = "https://buchung.ub.uni-frankfurt.de/zeit/index.php"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    rows = soup.select_one("div#start").select_one("table").select("tr")

    res = []
    urls = {}
    saved_urls = []
    for row in rows:
        content = row.select("td")
        if row.select_one("td").has_attr("colspan"):
            campus = row.get_text()
            res.append(Separator(f'===== {campus[1:-1]:^20} ====='))
        else:
            cols = row.select("td")
            if len(cols) < 6:
                continue

            """abbr = cols[5].select_one("a").attrs["href"]
            abbr = abbr.split("/")[-2] if abbr[-1] == '/' else abbr.split("/")[-1]"""
            name = cols[1].get_text().replace('-', '')
            name = name[:-1] if name[-1] == ' ' else name
            url = cols[5].select_one("a").attrs["href"]
            url = url[:-1] if url[-1] == '/' else url
            if url in saved_urls:
                continue
            saved_urls.append(url)
            active_locations = ['BRuW', 'BSP', 'BNat', 'MedHB']
            if name in active_locations:
                res.append(name)
            urls[name] = {'name': name, 'url': url}

    return res, urls
