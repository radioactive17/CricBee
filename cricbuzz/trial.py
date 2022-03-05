
from datetime import datetime,timedelta

today = datetime.today()

date_from = today.strftime('%d')
month_from = today.strftime('%b').upper()
year_from = today.strftime('%Y')
day_from = today.strftime('%a').upper()

q1 = day_from + ', ' + month_from + ' ' + date_from + ' ' + year_from
print(q1)

day3 = datetime.today() + timedelta(days=3)
date_to = day3.strftime("%d")
month_to = day3.strftime("%b").upper()
year_to = day3.strftime("%Y")
day_to = day3.strftime("%a").upper()
q2 = day_to + ', ' + month_to + ' ' + date_to + ' ' + year_to
print(q2)
