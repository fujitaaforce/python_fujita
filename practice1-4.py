#課題4
debt=250000
repay=30000
i=1

while debt>0:
    if debt<30000:
        interest=(debt*0.14)/12
        if (debt+interest)>30000:
            debt+=interest
            debt-=repay
            msg="残り",debt,"円"
        else:
            debt+=interest
            repay=debt
            debt-=repay
            msg="返済完了"
    else:
        interest=(debt*0.14)/12
        debt+=interest
        debt-=repay
        msg="残り",debt,"円"
    print(i,"か月目返済額=",repay,"円,",msg)
    i+=1

