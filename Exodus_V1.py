import turtle as t
#Pregatim Scena
t.setup(1920,980)
c=t.Screen()
canvas=t.Screen().getcanvas()
#Personaj
t.shape("arrow")
t.shapesize(1,1,1)
t.Screen().bgcolor("grey")
t.color("black")
t.pencolor("white")

#Miscare
def fr():
    t.forward(45)
def lf():
    t.left(90)
def rh():
    t.right(90)
def bc():
    t.back(45)

c.onkey(fr,"Up")
c.onkey(lf,"Left")
c.onkey(rh,"Right")
c.onkey(bc,"Down")
c.listen()
#implementarea butoanelor
from tkinter import *
def myClickB():
    MLB=Label(canvas.master,t.pencolor("blue"))
    MLB.pack()

def myClickR():
        MLB=Label(canvas.master, t.pencolor("red"))
        MLB.pack()


def myClickO():
    MLB=Label(canvas.master, t.pencolor("orange"))
    MLB.pack()

def myClickV():
        MLB=Label(canvas.master, t.pencolor("violet"))
        MLB.pack()

def myClickY():
        MLB=Label(canvas.master, t.pencolor("yellow"))
        MLB.pack()

BButton = Button(canvas.master,bg="blue",command=myClickB,height=2,width=4)
BButton.pack(side=LEFT)
RButton = Button(canvas.master,bg="red",command=myClickR,height=2,width=4)
RButton.pack(side=LEFT)
OButton = Button(canvas.master,bg="orange",command=myClickO,height=2,width=4)
OButton.pack(side=LEFT)
VButton = Button(canvas.master,bg="violet",command=myClickV,height=2,width=4)
VButton.pack(side=LEFT)
YButton = Button(canvas.master,bg="yellow",command=myClickY,height=2,width=4)
YButton.pack(side=LEFT)


def Clear():
    MLB=Label(canvas.master, t.clear())
    MLB.pack()

ClearButton = Button(canvas.master,command=Clear,text="Clear",height=2,width=4)
ClearButton.pack(side=LEFT)


t.done()#sfarsit program