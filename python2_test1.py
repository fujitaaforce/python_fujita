def calculate(speed, distance):
    hour = distance / speed
    return hour
print("速度を入力してください（Km/h）")
speed = int(input())
print("距離を入力してください（Km）")
distance = int(input())
print("走行時間は" + str(calculate(speed,distance)) + "時間です")
