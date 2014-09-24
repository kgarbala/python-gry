# Krzysztof Garbala
# -*- coding: utf-8 -*-
# Python 3.4
''' Pong'''
import tkinter, tkinter.messagebox, random

WIDTH = 600
HEIGHT = 400
R = 10
X = WIDTH/2
Y = HEIGHT/2
BALL_POS = [X-R, X-R, X+R, X+R]
i = -10
V_BALL = [0, 0, 0, 0]
STATE = True

def start():
    '''Wznowienie Gry'''
    global STATE, V_BALL
    STATE = True
    V_BALL = [random.randrange(-5, 5), random.randrange(-5, 5)]
    #C.itemconfig(BALL ,fill="Red")
    pos = [20, 20, 30, 30]
    C.coords(BALL, pos[0], pos[1], pos[2], pos[3])
    print ("V_BALL[0]=", V_BALL[0], "V_BALL[1]=", V_BALL[1])
    #C.itemconfig(BALL, coords=[10,10, 100, 100])

def pause():
    '''zatrzymanie piłki'''
    global STATE
    if STATE:
        STATE = False
    else:
        STATE = True

def update():
    '''ruch podow, pilki w czasie uaktualniany co 20ms?'''
    global BALL_POS
    if STATE:
        if BALL_POS[0] <= 0 or BALL_POS[0] >= WIDTH:
            V_BALL[0] = V_BALL[0]*(-1)
        if BALL_POS[1] <= 0 or BALL_POS[1] >= HEIGHT-15:
            V_BALL[1] = V_BALL[1]*(-1)
        BALL_POS = [BALL_POS[0]+V_BALL[0], BALL_POS[1]+V_BALL[1],\
	             BALL_POS[2]+V_BALL[0], BALL_POS[3]+V_BALL[1]]
        C.coords(BALL, BALL_POS[0], BALL_POS[1], BALL_POS[2], BALL_POS[3])
    FRAME.after(20, update)

FRAME = tkinter.Tk()
FRAME.title("Pong")
PAUSE = tkinter.Button(FRAME, text="Pause", command=pause)
PAUSE.pack()
START = tkinter.Button(FRAME, text="New Game", command=start)
START.pack()
C = tkinter.Canvas(FRAME, bg="green", height=HEIGHT, width=WIDTH)
C.pack()
C.create_line((WIDTH-10, 0), (WIDTH-10, HEIGHT), fill='White', width=2)
C.create_line((10, 0), (10, HEIGHT), fill='White', width=2)
Z = C.create_line((WIDTH/2, 0), (WIDTH/2, HEIGHT), \
    fill='White', width=2)
POD_L = C.create_line((10, HEIGHT/2-50), (10, HEIGHT/2+50), \
    fill='Grey', width=10)
POD_R = C.create_line((WIDTH-10, HEIGHT/2-50), \
    (WIDTH-10, HEIGHT/2+50), fill='Black', width=10)
BALL = C.create_oval(BALL_POS, outline="red", fill="White", width=2)
update()
FRAME.mainloop()
