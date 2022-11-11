import datetime
import pytz

tday = datetime.date.today()
print(tday)

# print(tday.weekday())
# Monday 0 Sunday 1

# print(tday.isoweekday())
# Monday 0 Sunday 1

tdelta = datetime.timedelta(days=7)

print(tday + tdelta)


bday = datetime.date(2023, 1, 11)

till_bday = bday - tday
print(till_bday)
print(till_bday.days)


dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)


dz = datetime.datetime(2022, 11, 11, 11, 33, 54, tzinfo=pytz.UTC)
print(dz)

dz_now = datetime.datetime.now(tz=pytz.UTC)
print(dz_now)

dz_ind = dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))
print(dz_ind)


# strftime = Datetime to String
# strptime = String to Datetime
print(dz_ind.strftime('%B %d, %Y'))


dt_str = 'November 11, 2022'
dn = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dn)

# for tz in pytz.all_timezones:
#     print(tz)
