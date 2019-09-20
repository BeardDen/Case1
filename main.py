import turtle

def square (x, y, a) :
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward((a**2+a**2)**0.5)
    turtle.right(135)

def main ():
    square(-200, 200, 180)
    turtle.down()

if __name__ =="__main__" :
    main()


