# 課題4
from decimal import Decimal, ROUND_HALF_UP
debt = 250000
repay = 30000
i = 1
while debt > 0:
    if debt < 30000:
        interest = Decimal(str(debt * (0.14 / 12))).quantize(Decimal('0.0000000001'), ROUND_HALF_UP)
        debt += interest
        if debt > 30000:
            debt -= repay
            msg = "残り" + str(debt) + "円"
        else: 
            repay = debt
            debt -= repay
            msg = "返済完了"
    else:
        interest = Decimal(str(debt * (0.14 / 12))).quantize(Decimal('0.0000000001'), ROUND_HALF_UP)
        debt += interest
        debt -= repay
        msg = "残り" + str(debt) + "円"
    print(str(i) + "か月目：返済額=" + str(repay) + "円,"+ msg)
    i += 1