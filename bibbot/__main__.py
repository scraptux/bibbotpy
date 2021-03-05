import bibbot.api.locations as loc
import bibbot.api.days as days
import bibbot.api.seatings as seats


if __name__ == '__main__':
    location = loc.choose_location()
    location = days.choose_days(location)
    # seatings = seats.get_seats_1(location)
    print(location)
