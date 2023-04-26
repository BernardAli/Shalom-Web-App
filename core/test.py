from datetime import date, datetime, timedelta

today = datetime.now()

my_birthdate = datetime(1992, 6, 6)
my_birthdate = my_birthdate.replace(year=today.year)
print(my_birthdate.isoweekday())
diff = my_birthdate - datetime(2022, 12, 31)
print(diff.days)


def this_week(birth_date):
    today = datetime.now()
    birth_date = birth_date.replace(year=today.year)
    return birth_date.weekday() if today.isocalendar()[1] == birth_date.isocalendar()[1] else None


birthday = [{'name': 'b', 'date': datetime(1992, 4, 26)}, {'name': 'a', 'date': datetime(1992, 4, 26)}]

print(this_week(datetime(1992, 4, 29)))

birthdays = [this_week(bb['date']) for bb in birthday]
print(birthdays)

# for a in birthday:
#     print(a['name'])
