farm1 = 1000
farm2 = 1700
farm3 = 2300
farm4 = 3000
wheat = farm1
for mounth in range(1, 12):
    wheat = wheat + farm2 - farm3 + farm4
    print("Месяц %s = %s" % (mounth, wheat))