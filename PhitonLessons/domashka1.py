Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t=turtle.Pen()
>>> t=up()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t=up()
NameError: name 'up' is not defined
>>> t.up()
>>> t.backward(50)
>>> t.backward(25)
>>> t.forward(25)
>>> t.down()
>>> t.forward(50)
>>> t.forward(50)
>>> t.up()
>>> t.forward(25)
>>> t.left(90)
>>> t.forward(25)
>>> t.down()
>>> t.forward(100)
>>> t.up()
>>> t.forward(25)
>>> t.left(90)
>>> t.forward(25)
>>> t.down()
>>> t.forward(100)
>>> t.up()

>>> t.forward(25)
>>> t.left(90)
>>> t.forward(25)
>>> t.down()
>>> t.forward(100)
>>> t.right(90)
>>> t.up()
>>> t.forward(100)
>>> t.right(180)
>>> 
