def calcurate(year):
    if year % 4 == 0:
        msg = "閏年です。"
    else:
        msg = "閏年ではありません。"
    return msg
print("現在の年（西暦）を入力してください")
year = int(input())
print("現在日は" + calcurate(year))
print("昨年の同じ日は" + calcurate(year - 1))
print("来年の同じ日は" + calcurate(year + 1))