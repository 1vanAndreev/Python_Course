money_capital = 0
salary = 20000
spendings = 25000
increase = 0.03
summa = 0
for i in range(10):
    if i == 0:
        increase = 0
    else:
        increase = 0.03
    spendings = spendings + spendings * increase
    money_capital = spendings - salary
    summa = summa + money_capital
    print ("Debt month",i," = ",money_capital)
print ("Необходимая подушка",summa)

