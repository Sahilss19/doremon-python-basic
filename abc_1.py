from turtle import *

class doraemon:
    def __init__(self):
        self.s = Screen()
        self.t = Turtle()
        self.t.pensize(5)
        self.t.speed(9)
        self.s.setup(width=1000, height=800)

    def my_goto(self, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def eyes(self):
        self.t.fillcolor("White")
        self.t.begin_fill()
        tracer(False)
        a = 2.5
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a -= 0.05
                self.t.left(3)
                self.t.forward(a)
            else:
                a += 0.05
                self.t.left(3)
                self.t.forward(a)
        tracer(True)
        self.t.end_fill()

    def beard(self):
        self.my_goto(-32, 135)
        self.t.setheading(165)
        self.t.forward(60)

        self.my_goto(-32, 125)
        self.t.setheading(180)
        self.t.forward(60)

        self.my_goto(-32, 115)
        self.t.setheading(193)
        self.t.forward(60)

        self.my_goto(37, 135)
        self.t.setheading(15)
        self.t.forward(60)

        self.my_goto(37, 125)
        self.t.setheading(0)
        self.t.forward(60)

        self.my_goto(37, 115)
        self.t.setheading(-13)
        self.t.forward(60)

    def mouth(self):
        self.my_goto(5, 148)
        self.t.setheading(270)
        self.t.forward(100)
        self.t.setheading(0)
        self.t.circle(120, 50)
        self.t.setheading(230)
        self.t.circle(-120, 100)

    def scarf(self):
        self.t.fillcolor("Red")
        self.t.begin_fill()
        self.t.setheading(0)
        self.t.forward(200)
        self.t.circle(-5, 90)
        self.t.forward(10)
        self.t.circle(-5, 90)
        self.t.forward(207)
        self.t.circle(-5, 90)
        self.t.forward(10)
        self.t.circle(-5, 90)
        self.t.end_fill()

    def nose(self):
        self.my_goto(-10, 158)
        self.t.setheading(315)
        self.t.fillcolor("Red")
        self.t.begin_fill()
        self.t.circle(20)
        self.t.end_fill()

    def pupil(self):
        self.t.setheading(0)
        self.my_goto(-20, 195)
        self.t.fillcolor("black")
        self.t.begin_fill()
        self.t.circle(13)
        self.t.end_fill()

        self.t.pensize(6)
        self.my_goto(20, 205)
        self.t.setheading(75)
        self.t.circle(-10, 150)

        self.t.pensize(4)
        self.my_goto(-17, 200)
        self.t.setheading(0)
        self.t.fillcolor("White")
        self.t.begin_fill()
        self.t.circle(5)
        self.t.end_fill()
        self.my_goto(0, 0)

    def face(self):
        self.t.forward(183)
        self.t.left(45)
        self.t.fillcolor("White")
        self.t.begin_fill()
        self.t.circle(120, 100)
        self.t.setheading(180)
        self.t.forward(121)
        self.t.pendown()
        self.t.setheading(215)
        self.t.circle(120, 100)
        self.t.end_fill()
        self.my_goto(63.56, 218.24)
        self.t.setheading(90)
        self.eyes()
        self.t.setheading(180)
        self.t.penup()
        self.t.forward(60)
        self.t.pendown()
        self.t.setheading(90)
        self.eyes()
        self.t.penup()
        self.t.setheading(180)
        self.t.forward(64)

    def head(self):
        self.t.penup()
        self.t.circle(150, 40)
        self.t.pendown()
        self.t.fillcolor("Blue")
        self.t.begin_fill()
        self.t.circle(150, 280)
        self.t.end_fill()

    def start(self):
        self.head()
        self.scarf()
        self.face()
        self.pupil()
        self.nose()
        self.mouth()
        self.beard()

if __name__ == '__main__':
    d = doraemon()
    d.start()
    done()
