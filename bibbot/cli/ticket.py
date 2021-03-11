import bibbot.api.locations as loc
import bibbot.api.days as days
import bibbot.api.times as times

import bibbot.api.auth as auth

from bibbot.cli import user, pswd


def book_ticket(ticket):
    auth.login(ticket, user, pswd)
    # TODO
    auth.logout()


def get_ticket():
    ticket = {}
    loc.choose_location(ticket)
    days.choose_days(ticket)
    times.choose_times(ticket)
    return ticket
