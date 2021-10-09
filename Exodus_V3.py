import turtle as t
from tkinter import *

#Pregatim Scena
t.setup(1920,980)
canvas=t.Screen().getcanvas()

#pregatire turtle
t.shape("turtle")
t.shapesize(1,1,1)
t.Screen().bgcolor("grey")
t.color("black")
t.pencolor("white")
t.speed(-1)

#corpul personajului
def body(x):
    t.fillcolor(x)
    t.begin_fill()
    t.right(90)
    t.forward(50)
    t.right(180)
    t.circle(40, -180)
    t.right(180)
    t.forward(200)
    t.right(180)
    t.circle(100, -180)
    t.backward(20)
    t.left(15)
    t.circle(500, -20)
    t.backward(20)
    t.circle(40, -180)
    t.left(7)
    t.backward(50)
    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()
    t.right(240)
    t.circle(50, -70)
    t.end_fill()

#fata personajului
def glass(x):
    t.up()
    t.right(230)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.down()
    t.fillcolor(x)
    t.begin_fill()
    t.right(150)
    t.circle(90, -55)
    t.right(180)
    t.forward(1)
    t.right(180)
    t.circle(10, -65)
    t.right(180)
    t.forward(110)
    t.right(180)
    t.circle(50, -190)
    t.right(170)
    t.forward(80)
    t.right(180)
    t.circle(45, -30)
    t.end_fill()


#caracterele
def caractere():
     t.setpos(-360,-250)
     t.left(180)
     body("red")
     glass("white")
     t.up()
     t.setpos(360, -250)
     t.down()
     t.left(390)
     body("blue")
     glass("white")
     t.up()
     t.setpos(0,0)

#desenul
def desen():
    t.reset()
    t.speed(-1)
    t.pencolor("white")
    t.up()
    t.clear()
    t.pensize(4)
    t.setpos(-750,-350)
    t.down()
    t.left(90)
    t.forward(600)
    t.right(90)
    t.forward(1500)
    t.right(90)
    t.forward(600)
    t.left(270)
    t.forward(1500)
    t.right(180)
    t.forward(750)
    t.left(90)
    t.forward(600)
    t.up()
    t.setpos(-720,-330)
    t.down()
    t.write("DAVID BESOI",font=("Verdana",15, "normal"))
    t.up()
    t.setpos(-80,-300)
    t.down()
    t.left(180)
    t.circle(20, 180)
    t.up()
    t.setpos(-60, -320)
    t.down()
    t.right(180)
    t.forward(20)
    t.right(180)
    t.forward(32)
    t.pensize(19)
    t.forward(22)
    t.pensize(15)
    t.up()
    t.setpos(30,-330)
    t.down()
    t.write("OCTAV MANDA", font=("Verdana", 15, "normal"))
    t.up()
    t.pencolor("red")
    t.setpos(660,-300)
    t.down()
    t.left(180)
    t.pensize(4)
    t.circle(20, 180)
    t.up()
    t.setpos(680, -320)
    t.down()
    t.right(180)
    t.forward(20)
    t.right(180)
    t.forward(32)
    t.pensize(19)
    t.forward(22)
    t.pensize(15)
    t.up()
    t.pensize(4)
    t.pencolor("white")
    t.setpos(-250,280)
    t.down()
    t.forward(180)
    t.right(90)
    t.forward(500)
    t.right(90)
    t.forward(180)
    t.right(90)
    t.forward(500)
    t.up()
    t.setpos(-125,350)
    t.down()
    t.write("BIRCHI SORIN", font=("Verdana", 25, "normal"))
    t.up()
    t.pensize(3)
    t.pencolor("red")
    t.setpos(180, 320)
    t.down()
    t.left(90)
    t.circle(15, 180)
    t.up()
    t.setpos(195, 300)
    t.down()
    t.right(180)
    t.forward(15)
    t.right(180)
    t.forward(25)
    t.pensize(12)
    t.forward(22)
    t.up()
    t.pencolor("black")
    t.setpos(-800,-480)
    t.down()
    t.pensize(4)
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(1600)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(1600)
    t.end_fill()
    t.up()
    t.setpos(-600,-450)
    t.down()
    t.pencolor("white")
    t.write("Mute", font=("Verdana", 15, "normal"))
    t.up()
    t.setpos(-500, -450)
    t.down()
    t.pencolor("white")
    t.write("Stop Video", font=("Verdana", 15, "normal"))
    t.up()
    t.setpos(-350, -450)
    t.down()
    t.pencolor("white")
    t.write("Participanti", font=("Verdana", 15, "normal"))
    t.up()
    t.setpos(-200, -450)
    t.down()
    t.pencolor("white")
    t.write("Chat", font=("Verdana", 15, "normal"))
    t.up()
    t.setpos(-50, -450)
    t.down()
    t.pencolor("green")
    t.write("Share Screen", font=("Verdana", 15, "normal"))
    t.up()
    t.setpos(175, -450)
    t.down()
    t.pencolor("red")
    t.write("Record", font=("Verdana", 15, "normal"))
    t.up()
    t.setpos(350, -450)
    t.down()
    t.pencolor("white")
    t.write("Reaction", font=("Verdana", 15, "normal"))
    t.up()
    t.setpos(555, -450)
    t.down()
    t.pencolor("red")
    t.write("Leave", font=("Verdana", 15, "normal"))
    t.up()
    t.setpos(0,0)
    t.pencolor("black")

#miscarea broscutei la apasarea click stanga
def dragging(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

#implementarea butoanelor
def myClickB():
    MLB=Label(canvas.master,t.pencolor("blue"))
    MLB.pack()

def myClickR():
    MLB = Label(canvas.master, t.pencolor("red"))
    MLB.pack()

def myClickO():
    MLB = Label(canvas.master, t.pencolor("orange"))
    MLB.pack()

def myClickP():
    MLB = Label(canvas.master, t.pencolor("purple"))
    MLB.pack()

def myClickY():
    MLB = Label(canvas.master, t.pencolor("yellow"))
    MLB.pack()

def myClickBL():
    MLB = Label(canvas.master, t.pencolor("black"))
    MLB.pack()

def myClickW():
    MLB = Label(canvas.master, t.pencolor("white"))
    MLB.pack()

def myClickG():
    MLB = Label(canvas.master, t.pencolor("green"))
    MLB.pack()

def myClickC():
    MLB = Label(canvas.master, t.pencolor("cyan"))
    MLB.pack()

def myClickL():
    MLB = Label(canvas.master, t.pencolor("lime"))
    MLB.pack()

def UP():
    MLB = Label(canvas.master, t.up())
    MLB.pack()

def DOWN():
    MLB = Label(canvas.master, t.down())
    MLB.pack()

def Clear():
    MLB = Label(canvas.master, t.clear())
    MLB.pack()

#butonul pentru desen
def Auto():
    MLB = Label(canvas.master, desen(),caractere())
    MLB.pack()

#butonul albastru
BButton = Button(canvas.master,bg="blue",command=myClickB,height=2,width=4)
BButton.pack(side=LEFT)

#butonul rosu
RButton = Button(canvas.master,bg="red",command=myClickR,height=2,width=4)
RButton.pack(side=LEFT)

#butonul portocaliu
OButton = Button(canvas.master,bg="orange",command=myClickO,height=2,width=4)
OButton.pack(side=LEFT)

#butonul mov
PButton = Button(canvas.master,bg="purple",command=myClickP,height=2,width=4)
PButton.pack(side=LEFT)

#butonul galben
YButton = Button(canvas.master,bg="yellow",command=myClickY,height=2,width=4)
YButton.pack(side=LEFT)

#butonul verde
GButton = Button(canvas.master,bg="green",command=myClickG,height=2,width=4)
GButton.pack(side=LEFT)

#butonul cyan
CButton = Button(canvas.master,bg="cyan",command=myClickC,height=2,width=4)
CButton.pack(side=LEFT)

#butonul lime
LButton = Button(canvas.master,bg="lime",command=myClickL,height=2,width=4)
LButton.pack(side=LEFT)

#butonul negru
BLButton = Button(canvas.master,bg="black",command=myClickBL,height=2,width=4)
BLButton.pack(side=LEFT)

#butonul alb
WButton = Button(canvas.master,bg="white",command=myClickW,height=2,width=4)
WButton.pack(side=LEFT)

#butonul pentru ridicarea broscutei
UP = Button(canvas.master,command=UP,text="UP",height=2,width=4)
UP.pack(side=LEFT)

#butonul pentru coborarea broscutei
DOWN = Button(canvas.master,command=DOWN,text="DOWN",height=2,width=6)
DOWN.pack(side=LEFT)

#butonul pentru stergere
ClearButton = Button(canvas.master,command=Clear,text="Clear",height=2,width=4)
ClearButton.pack(side=LEFT)

#Porneste desenul
AutoButton = Button(canvas.master,command=Auto,text="Auto",height=2,width=4)
AutoButton.pack(side=LEFT)

#functia principala a programului
def main():
       t.listen()
       t.ondrag(dragging)
       mainloop()

main()