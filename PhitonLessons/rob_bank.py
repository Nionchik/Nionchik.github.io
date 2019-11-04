import time
import random
from pathlib import Path

eq = "=============="
multiplier = 1
print("===============Welcome! AutoSave is ON===============")

def rob_bank(dollars):
    f = random.randint(1, 10)
    if f <=3:
        k = random.randint(70000, 200000)
        dollars -= k
        print("===============You're caught during the robbery! ", k, " dollars===============")
        print("===============Also you're jailed for 1 minutes===============")
        for i in range(15):
            time.sleep(1)
            print(".", end = " ")
        print(" ")
        print("===============You're released from the jail")
    else:
        a = random.randint(10000, 100000)
        dollars = pdollars(dollars, a)
        print("===============Yoy're succesfully robbed the bank===============")

def work(dollars):
    a = random.randint(1000, 10000)
    dollars = pdollars(dollars, a)
    print(eq + "You worked really hard and got", a * multiplier, "dollars" + eq)
    return dollars

printers = {"Bronze_printer": 100000,
            "Silver_printer": 300000,
            "Gold_printer": 1000000,
            "Platinum_printer": 5000000,
            "Titanium_printer": 10000000}

def buy(dollars, printers, name):
    price = atata.get(name)
    if price:
        if name in printers:
            print("You can buy only one printer!")
        elif dollars >= price:
            dollars -= price
            printers.append(name)
            print("============You just bought", name.replace("_", " "), ", congrat!============")
        else:
            print("sorry ur poor")
    else:
        print("This printer does't exist")
    return (printers, dollars)

atata_sec = {"Bronze_printer": 500,
            "Silver_printer": 1500,
            "Gold_printer": 500,
            "Platinum_printer": 2500,
            "Titanium_printer": 150000}

def game_start():
    global multiplier
    multi_file = Path("multiplier.txt")
    if multi_file.is_file():
        f = open("multiplier.txt", "r+")
        uir = f.readline()
        if uir:
            multiplier = int(uir)
    timer = time.time()
    dollars = 0
    printers = []
    called_work = time.time() - 100
    dollars_file = Path("cash_balance.txt")
    if dollars_file.is_file():
        f = open("dollars_balance.txt", "r+")
        ui = f.readline()
        if ui:
            dollars = int(ui)
            printers = (f.readline())[1:-1].replace(" ","").replace("'", "").split(",")
            if printers == [""]:
                printers = []
            print("Your data succesfully loaded with", dollars, "dollars and", printers, "!")
        cmds=['rob bank', 'balance', 'work', 'buy', 'inventory',
              'cmds', 'casino', 'redith', '===================', 'clear data', 'close game']
        while 1 == 1:
            b = input('=========What do you want to do?(Type cmds for list of commands)==============')
            b = b.lower()
            diffrence = int(time.time() - timer)
            save(dollars, printers)
            for i in printers:
                o = diffrence*atata_sec[i]
                dollars = pdollars(dollars, o)
            timer = time.time()
            if b == 'rob_bank':
                dollars = rob.bank(dollars)
            elif b == 'balance':
                bal(dollars)
            elif b == 'admin':
                dollars = admin(dollars)
            elif b == 'save':
                save(dollars, printers)
            elif b == 'work':
                time_now = time.time()
                if (time_now - called_work) >= 15:
                    dollars = work(dollars)
                    called_work = time_now
                else:
                    print("You can work in", int(15 - (time_now - called_work)), 'seconds!')
            elif b == 'buy':
                for u in atata:
                    s = ''
                    s += str(u.replace('_', ' ')) + '-' + str(atata[u])
                    print(s.center(80))
                kor = input('What do you want to buy?')
                kor = kor.lower().capitalize()
                printers, dollars = buy(dollars, printers, kor.replace('', '_'))
            elif b == 'inventory':
                inventory(printers)
            elif b == 'cmds':
                cmds1(cmds)
            elif b == 'clear data':
                clear_data()
                dollars = 0
                printers = []
                multiplier = 0
            elif b == 'casino':
                dollars = casino
            elif b == 'rebith':
                dollars, printers = rebith(dollars, printers)
            elif b == 'close game':
                print('You just closed the game. Bue!')
                return
            else:
                print('The command not doesnt exist!')
                cmds1(cmds)

def bal(dollars):
    print('==============Currently you have', dollars, 'dollars===============')

def admin(dollars):
    dollars += 20000000
    print('+20000000')
    return cash

def save(dollars, printers):
    f = open("cash_balance.txt",'w+')
    f.write(str(dollars)+'\n')
    f.write(str(printers))
    f = open("multiplier.txt",'w+')
    f.write(str(multiplier)+'\n')
    f.close

def inventory(printers):
    print('currently you have:')
    for i in printers:
        print(i)

def cmds1(cmds):
    print('List of commands: ')
    for i in cmds:
        print(i.center(80))

def clear_data():
    g = input("Are you sure you want to clear all of your data? It will remove all your progress! (yes or no)")
    g = g.lower()
    if g == "yes":
        f = open('dollars_balance.txt', 'w+')
        f.write('')
        f.close()
        k = open('multiplier.txt', 'w+')
        k.write()
        k.close
    else:
        print('then why u typed this command then?')

def casino(dollars):
    b = input("What is you bet?")
    if b > dollars:
        print("Sorry ur broke")
    else:
        f = random.randint(1, 2)
        if f == 1:
            dollars = pdollars(dollars, b)
            print("Congrat! You juss won", b * 2 * multiplier, 'dollars!')
        else:
             dollars -= b
             print('oh no u lost')
    return dollars

def pcash(dollars, amount):
    dollars += multiplier*amount
    return cash

def rebith(dollars,printers):
    global multiplier
    b = input("Are you sure that you want to do rebith? You are gonna lose everything, but you will get 2x multiplier.The price is 20 million.(yes or no)")
    b = b.lower()
    if b == 'yes':
        if dollars >= 20000000:
              clear_data()
              multiplier += 1
              dollars = 0
              printers = []
              f= open("multiplier.txt","w+")
              f.write(str(multiplier)+'\n')
              f.close()
              print("Congratulations you just made rebith! Current multiplier is x"+str(multiplier)+'!')
        else:
            print('sorry ur poor')
    else:
        print('but it gives u 2x multiplier!1!!111!!!1!')
    return (dollars,printers)
game_start()

        


        
            


    


        
    


