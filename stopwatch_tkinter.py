# Krzysztof Garbala
# -*- coding: utf-8 -*-
# Python 3.4
''' Stopwatch'''
import tkinter
MIN = 0
SEC = 0
MILI = 0
SCORE = 0
CLICK = 0
PATTERN = '{0:02d}:{1:02d}:{2:02d}'
STATE = False

def update():
    '''działanie zegara'''
    global MIN, SEC, MILI
    if STATE:
        MILI += 1
        if MILI >= 100:
            MILI = 0
            SEC += 1
        if SEC >= 60:
            SEC = 0
            MIN += 1
    form = PATTERN.format(MIN, SEC, MILI)
    L.config(text=form)
    FRAME.after(10, update) # 1000 to sekunda

def stop():
    '''zatrzymanie zegara'''
    global STATE, SCORE, CLICK
    if SEC%2 == 0 and (MILI - MILI%10 == 0) and STATE:
        SCORE += 1
        CLICK += 1
        L.configure(fg="Green")
    elif STATE:
        CLICK += 1
        L.configure(fg="Red")
    RESULTS.configure(text=str(SCORE)+"/"+str(CLICK))
    STATE = False

def start():
    '''start zegara'''
    global STATE
    L.configure(fg="Black")
    STATE = True

def restart():
    '''wyzerowanie zegara'''
    global MIN, SEC, MILI, SCORE, CLICK
    MIN = 0
    SEC = 0
    MILI = 0
    SCORE = 0
    CLICK = 0
    L.configure(fg="Black")
    RESULTS.configure(text=str(SCORE)+"/"+str(CLICK))

FRAME = tkinter.Tk()
FRAME.minsize(100, 100)
FRAME.title("Stopwatch")
L = tkinter.Label(FRAME, fg="black", font=("Helvectica", "30"))
L.pack()
START = tkinter.Button(FRAME, text="START", command=start)
START.pack()
STOP = tkinter.Button(FRAME, text="Stop", command=stop)
STOP.pack()
RESTART = tkinter.Button(FRAME, text="RESTART", command=restart)
RESTART.pack()
RESULTS = tkinter.Label(FRAME, text=str(SCORE)+"/"+str(CLICK), \
    fg="Purple", font=("Helvectica", "12"))
RESULTS.pack()
update()
FRAME.mainloop()
