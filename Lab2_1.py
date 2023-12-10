money_capital = 40000
salary = 20000
summa = money_capital
spendings = 25000
increase = 0.05
count = 0
while summa > 0:
    if count == 0:
        increase = 0
    else:
        increase = 0.05
    summa = summa + salary
    print("summa nomer",count,"=",summa)
    spendings = spendings + spendings * increase
    print("spendings nomer", count, "=", spendings)
    summa = summa - spendings
    count = count + 1
print("Месяцев без долгов -",count - 1)



