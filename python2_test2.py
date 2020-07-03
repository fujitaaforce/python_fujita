import datetime

def year_calcurate(year):
    if year % 4 != 0 & (year % 100 == 0 & year % 400 != 0):
        return False
    else:
        return True

now = datetime.date.today()
print("現在日は西暦{}年{}月{}日です。".format(now.year, now.month, now.day))
years = (now.year, now.year - 1, now.year +1)
for year in years :
    if year_calcurate(year):
        print(str(year) + "年は閏年です。")
    else:
        print(str(year) + "年は閏年ではありません。")