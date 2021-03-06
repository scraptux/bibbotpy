# noinspection PyUnresolvedReferences
from dateutil import rrule
from datetime import datetime, timedelta

from PyInquirer import prompt, Separator

from bibbot.api.request import get_soup


def choose_days(location):
    day_limit = get_day_limits(location)
    now = datetime.strptime(datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d')
    day_options = []
    for dt in rrule.rrule(rrule.DAILY, dtstart=now, until=now+timedelta(days=13)):
        if dt.weekday() > day_limit:
            continue
        day_options.append(dt.strftime("%A, %d. %B %Y"))
        if dt.weekday() == day_limit and dt != now+timedelta(days=13):
            s = f"{dt.strftime('%W')}. Kalenderwoche"
            day_options.append(Separator(f'===== {s:^20} ====='))

    question = [{
        'type': 'list',
        'name': 'date',
        'message': 'Bitte wähle ein Datum aus:',
        'choices': day_options
    }]
    answer = datetime.strptime(prompt(question)['date'], '%A, %d. %B %Y')
    location['date'] = (answer - now).days
    return location


def get_day_limits(location):
    soup = get_soup(location['location']['url'])
    day_lim = soup.select("#layouttabelle tbody tr td table tr td p")[1].get_text()
    idx = day_lim.find("Montag")
    if idx == -1:
        idx = day_lim.find("Mo.")
    day_lim = day_lim[idx:].split(" ")[2]
    day_lim = day_lim[:-1] if day_lim[-1] == ")" else day_lim
    return 6 if day_lim in ["Sonntag", "So."] else 5
