# 課題4
debt = 250000
repay = 30000
i = 1

while debt > 0:
    debt = debt * (1+(0.14 / 12))
    if debt <= 30000:
        repay = debt
        msg = "返済完了"
    else:
        msg = "残り" + str(debt) + "円"
    debt -= repay
    print(str(i) + "か月目：返済額=" + str(repay) + "円,"+ msg)
    i += 1