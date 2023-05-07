'''正七角星'''
import turtle as t
t.clear()
t.reset()
t.Pen()
for i in range(7):
    t.forward(200)
    t.left(180-180/7)
t.done()