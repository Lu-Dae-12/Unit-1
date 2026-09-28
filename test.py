import turtle
t = turtle
x=100

for i in range(3):
    print(i)

for i in range (5):
    for j in range (4):
        t.forward(x)
        t.left(90)
    t.right(10)
