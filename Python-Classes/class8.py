from datetime import date, time, datetime, timedelta


def working_with_datetime():
    current_date = datetime.now()
    print(current_date)
    print(current_date.strftime('%d/%m/%Y %H:%M:%S'))
    print(current_date.strftime('%c'))
    print(current_date.day)
    print(current_date.date())
    tuple = ('Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag')
    print(tuple[current_date.weekday()])
    created_date = datetime(2017, 0o3, 0o1, 15, 30, 20)
    print(created_date)
    print(created_date.strftime('%c'))
    data_string = '01/01/2019'
    converted_date = datetime.strptime(data_string, '%d/%m/%Y')
    print(converted_date)
    new_date = converted_date - timedelta(days=365, hours=2, minutes=15)
    # new_date = converted_date + timedelta(days=365, hours=2, minutes=15)
    print(new_date)

    data = datetime(1815, 12, 10, 00, 00, 00).strftime('%d/%m/%Y')
    hora = time(hour=13, minute=14, second=00)
    print('{} às {}'.format(data, hora))


def working_with_date():
    current_date = date.today()
    print(type(current_date))
    print(current_date.strftime('%d/%m/%Y'))
    current_date_str = current_date.strftime('%A, %B, %Y.')
    print(current_date_str)
    print(type(current_date_str))


def working_with_time():
    hour = time(hour=15, minute=18, second=30)
    print(hour)
    hour_str = hour.strftime('%H:%M:%S')
    print(hour_str)
    print(type(hour_str))


if __name__ == '__main__':
    # working_with_date()
    # working_with_time()
    working_with_datetime()
