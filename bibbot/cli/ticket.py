import bibbot.api.locations as loc
import bibbot.api.days as days
import bibbot.api.times as times

import bibbot.api.auth as auth


def book_ticket(ticket, user, pswd):
    auth.login(ticket, user, pswd)
    # TODO
    auth.logout(ticket)


def get_ticket():
    ticket = {}
    loc.choose_location(ticket)
    days.choose_days(ticket)
    times.choose_times(ticket)
    return ticket
