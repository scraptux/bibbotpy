from PyInquirer import prompt

from bibbot.cli import ticket

tickets_pending = []
tickets_booked = []

user = None
pswd = None
telnr = None


def get_credentials():
    global user, pswd, telnr
    questions = [
        {
            'type': 'input',
            'name': 'user',
            'message': 'Bitte den HRZ-Nutzernamen eingeben:'
        },
        {
            'type': 'password',
            'name': 'pswd',
            'message': 'Bitte das HRZ-Passwort eingeben:'
        },
        {
            'type': 'input',
            'name': 'telnr',
            'message': 'Bitte die Telefonnummer angeben:'
        }
    ]
    answers = prompt(questions)
    user = answers['user']
    pswd = answers['pswd']
    telnr = answers['telnr']


def start_cli():
    get_credentials()
    t = ticket.get_ticket()
    tickets_pending.append(t)
    print(t)
