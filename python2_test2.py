import datetime

def calcurate(year):
    if year % 4 == 0:
        msg = "閏年です。"
    else:
        msg = "閏年ではありません。"
    return msg
now = datetime.date.today()
print("現在日は西暦{}年{}月{}日です。".format(now.year, now.month, now.day))
year = now.year
print("現在日は" + calcurate(year))
print("昨年の同じ日は" + calcurate(year - 1))
print("来年の同じ日は" + calcurate(year + 1))