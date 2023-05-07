'''多個圓'''
import turtle as t
t.clear()
t.reset()
t.Pen()
t.up()
t.setposition(-300,0)
for i in range(1,5):
    t.down()
    for j in range(1,i+1):
        t.circle(20*j)
    t.up()
    t.forward(200)
t.done()