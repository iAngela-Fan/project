'''正六角星'''
import turtle as t
t.clear()
t.reset()
t.Pen()
LENGTH=200
t.circle(LENGTH,steps=3)
t.penup()
t.circle(LENGTH, 180)
t.pendown()
t.circle(LENGTH,steps=3)