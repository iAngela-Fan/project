'''同心圓'''
import turtle as t
t.clear()
t.reset()
t.Pen()
for i in range(1,5+1):
    t.up()
    t.left(90)
    t.backward(20)
    t.right(90)
    t.down()
    t.circle(20*i)
t.done()
