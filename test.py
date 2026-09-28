import turtle
t = turtle
x=100

for i in range(3):
    print(i)

    for i in range(4):
        t.forward(100)
    t.left(90)

def triangle ():
    sidelength = 100
rotate = 90
def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
triangle(100,90)
