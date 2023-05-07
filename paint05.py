'''正五角星'''
import turtle as t
t.clear()
t.reset()
t.Pen()
for i in range(5):
    t.forward(200)
    t.left(180-180/5)
t.done()