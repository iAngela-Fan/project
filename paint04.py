'''任意多邊形'''
n=int(input('該正多邊形有幾個邊？'))
if n==3:
    oc=120
else:
    oc=360/n
import turtle as t
for i in range(n):
    t.forward(200)
    t.left(oc)
t.done()