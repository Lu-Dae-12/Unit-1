for i in range(5):
    print(i)

def square(loop):

    def addSquares(iRange):
        length = 25
        for i in range(iRange):
            square(length, 90)
        length += 25
    addSquares(5)
