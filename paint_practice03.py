'''自訂函式畫同心圓'''
def concentric(x,size):
    for i in range(1,x):
        t.up()
        t.left(90)
        t.backward(size)
        t.right(90)
        t.down()
        t.circle(size*i)
import turtle as t
t.clear()
t.reset()
t.Pen()
concentric(3,20)
t.done()
