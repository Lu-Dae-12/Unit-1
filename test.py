import turtle
t = turtle
x=100

for i in range(5):
    for j in range (5):
        t.forward(x)
        t.left(90)

def square() :
        def doubleSquares(iRange):
            length = 25
        for i in range(iRange):
            square(length, 90)
        length = length * 2
doubleSquares(5)