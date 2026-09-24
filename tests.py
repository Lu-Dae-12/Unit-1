import turtle
t = turtle
x=100

for i in range(60):
    for j in range (4):
        t.forward(x)
        t.left(90)
    t.right(5)

    sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
triangle(100,90)