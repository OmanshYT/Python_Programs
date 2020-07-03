import turtle

t = turtle.Pen()

def end():
    print('That is the end of my program!I hope you like it')
    feed = int(input('Do you have any feedback for the app(1) or is it perfect(2): '))
    if feed == 1:
        print('If so, then please email bmw.27.pro@gmail.com!')
    else:
        print('Thank you a lot for the compliment!')
    again = int(input('Would you like to make another shape(1) or leave(2): '))
    if again == 2:
        exit()

def ask_rectangle():
        print('Now your rectangle')
        horizontal1 = int(input('Your horizontal line: '))
        vertical1 = int(input('Your vertical line:'))
        yourcol = input('Your colour fill: ')
        rectangle(horizontal1, vertical1, yourcol)
        return horizontal1, vertical1, yourcol

def ask_triangle():
    print('Now your triangle')
    base2 = int(input('One side of your triangle: '))
    color1 = input('Your colour fill: ')
    triangle(base2, color1)
    return base2, color1

def ask_circle():
    print('Now your circle')
    radius2 = int(input('Enter your radius: '))
    colour2 = input('Enter your colour fill: ')
    circle(radius2, colour2)
    return radius2,colour2

def rectangle(horizontal, vertical, colour):
    t.shape('turtle')
    t.speed('slowest')
    t.pendown()
    t.pensize(1)
    t.color(colour)
    t.begin_fill()
    for i in range(1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

def triangle(base,colour1):
    t.shape('turtle')
    t.speed('slowest')
    t.pendown()
    t.pensize(1)
    t.color(colour1)
    t.begin_fill()
    for i in range(1,4):
        t.forward(base)
        t.left(120)
    t.end_fill()

def circle(radius,colour2):
    t.shape('turtle')
    t.speed('slowest')
    t.pendown()
    t.pensize(1)
    t.color(colour2)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

god = True

while god == True:
    choice = int(input('Do you want to draw a rectangle(1),triangle(2), circle(3) or all(4): '))
    if choice == 1:
        ask_rectangle()
    elif choice == 2:
        ask_triangle()
    elif choice == 3:
        ask_circle()
    else:
        which = int(input('Would you like to make your shapes in a specific order(1) or not(2):'))
        if which == 1:
            shape = int(input('Which shape do you want first: '
                           'a rectangle(1), a triangle(2) or a circle(3):'))
            if shape == 1:
                ask_rectangle()
            elif shape == 2:
                ask_triangle()
            elif shape == 3:
                ask_circle()
            now = int(input('Now which shape do you want to make, a rectangle(1), a triangle(2) or a circle(3):'))
            if now == 1:
                ask_rectangle()
            elif now == 2:
                ask_triangle()
            elif now == 3:
                ask_circle()
            bruh = int(input('Now which shape do you want to make, a rectangle(1), a triangle(2), a circle(3): '))
            if bruh == 1:
                ask_rectangle()
            elif bruh == 2:
                ask_triangle()
            elif bruh == 3:
                ask_circle()
        else:
            (a,b,c) = ask_rectangle()
            please = int(input('Do you want to move forward and make your next triangle(1) or not(2): '))
            if please == 1:
                side = int(input('Which side, left(1), right(2) or on top(3) of your first shape: '))
                if side == 1:
                    t.left(180)
                elif side == 2:
                    t.forward(a)
                    t.right(30)
            ask_triangle()
            do = int(input('Do you want to have your circle on the top corner(1), the left side(2), the right(3)'))
            ask_circle()
end()