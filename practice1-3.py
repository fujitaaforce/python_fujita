#課題3
weight = 50
hight = 1.7
bmi = weight/(hight**2)
msg=""
if bmi<18.5:
    msg="やせ"
if 18.5<=bmi<25:
    msg="標準"
if 25<=bmi<30:
    msg="肥満"
if 30<=bmi:
    msg="高度肥満"
print("あなたは"+msg+"です。")