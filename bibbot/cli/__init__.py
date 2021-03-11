from bibbot.cli import ticket

tickets_pending = []
tickets_booked = []

user = None
pswd = None
telnr = None


def get_credentials():
    pass  # TODO


def start_cli():
    get_credentials()
    t = ticket.get_ticket()
    tickets_pending.append(t)
    print(t)
