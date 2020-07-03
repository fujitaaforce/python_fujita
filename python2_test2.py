import datetime

def calcurate(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                msg = "閏年です。"
            msg = "閏年ではありません。"
        msg = "閏年です。"
    else:
        msg = "閏年ではありません。"
    return msg
now = datetime.date.today()
print("現在日は西暦{}年{}月{}日です。".format(now.year, now.month, now.day))
year = now.year
i = -1
while i<2 :
    msg = calcurate(year+i)
    i += 1
print("現在日は" + msg)
print("昨年の同じ日は" + msg)
print("来年の同じ日は" + msg)