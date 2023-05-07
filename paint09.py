'''移動圖形'''
import turtle as t
t.clear()
t.reset()
t.up()
t.goto(-100,-100)
t.Pen()
t.down()
for i in range(4):
    t.forward(200)
    t.left(90)
t.done()