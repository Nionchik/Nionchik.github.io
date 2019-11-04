Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Приве,мир")
Приве,мир
>>> print("Hi")
Hi
>>> 8*8
64
>>> 8*8*88/9
625.7777777777778
>>> Nice=100
>>> print(nice)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(nice)
NameError: name 'nice' is not defined
>>> print(Nice)
100
>>> MyMoney=999
>>> MyHP=100
>>> Message='Мои деньги:%s, мои жизни:%s'
>>> print(Message % MyMoney % MyHP)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(Message % MyMoney % MyHP)
TypeError: not enough arguments for format string
>>> print(Message % MyMoney)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(Message % MyMoney)
TypeError: not enough arguments for format string
>>> Message='Мои деньги:%s, мои жизни:'
>>> print(Message % MyMoney)
Мои деньги:999, мои жизни:
>>> Message='Мои деньги:, мои жизни:%s'
>>> print(Message % MyHP)
Мои деньги:, мои жизни:100
>>> chisla='Что находится между %s и %s?'
>>> print(chisla % ("a","c"))
Что находится между a и c?
>>> print(Message % (MyMoney,MyHP))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(Message % (MyMoney,MyHP))
TypeError: not all arguments converted during string formatting
>>> MyMoney = 999
>>> MyHP = 100
>>>  Message = 'Мои деньги:%s, мои жизни:%s'
 
SyntaxError: unexpected indent
>>> Message = 'Мои деньги:%s, мои жизни:%s'
>>> print(Message % (MyMoney,MyHP))
Мои деньги:999, мои жизни:100
>>> 
