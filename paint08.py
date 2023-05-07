'''填色'''
import turtle as t
t.clear()
t.reset()
t.Pen()
t.color('#DA70D6')
t.begin_fill()
for i in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()
t.done()