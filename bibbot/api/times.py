from bs4 import BeautifulSoup, Comment
from datetime import datetime, timedelta
from PyInquirer import prompt, Separator

from bibbot.api.request import get_soup


# 1: BRuW, BSP, BNat, MedHB


def choose_times(t):
    time_options = get_times_1(t['location']['url'])
    question = [{
        'type': 'checkbox',
        'name': 'time',
        'message': 'Bitte wähle den gewünschten Platz aus:',
        'choices': time_options
    }]
    answers = prompt(question)['time']
    if 'time' not in t:
        t['time'] = {}
    for answer in answers:
        # location['time'][answer[-12:-1]]
        time_str = answer[-12:-1]
        if time_str not in t['time']:
            t['time'][time_str] = []
        t['time'][time_str].append(answer[:-14])


def get_times_1(url):
    # get date for complete seating chart
    now = datetime.now() + timedelta(days=1)
    now = 1 if now.weekday() != 6 else 2
    # remove comments from html
    soup = get_soup(url, now)
    for element in soup(text=lambda text: isinstance(text, Comment)):
        element.extract()
    # splice seat table out
    html = str(soup)
    idx_s = html.find('<td class="tageszeit')
    html = html[idx_s:]
    idx_r = None
    tags_opened = 1
    for tag_start_idx in [i for i, ltr in enumerate(html) if ltr == "<"]:  # check all tags
        if html[tag_start_idx+1] == "/":  # closing tag
            tags_opened -= 1
            if tags_opened == 0:  # last needed tag
                idx_r = html[tag_start_idx:].find(">")+tag_start_idx
                break
        else:  # starting or standalone tag
            tag_stop_idx = html[tag_start_idx:].find(">")
            if html[tag_start_idx+tag_stop_idx-1] == '/':  # standalone tag
                continue
            else:  # starting tag
                tags_opened += 1
    html = html[:idx_r+1]
    html = "<table><tbody>"+html+"</table>"
    soup = BeautifulSoup(html, "html.parser")
    # get headers
    seat_headers = soup.select("th")
    times = []
    levels = []
    for header in seat_headers:
        time = header.get_text()[-11:]
        level = header.get_text()[:-11]
        if time not in times:
            times.append(time)
        if level not in levels:
            levels.append(level)
    # create prompt options
    options = []
    for time in times:
        options.append(Separator(f'===== {time.replace("-"," - "):^20} ====='))
        for level in levels:
            options.append({"name": f"{level} ({time})"})
    return options
