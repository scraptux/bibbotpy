import bibbot.api.locations as loc
import bibbot.api.days as days
import bibbot.api.times as times


if __name__ == '__main__':
    location = loc.choose_location()
    location = days.choose_days(location)
    location = times.choose_times(location)
    print(location)
