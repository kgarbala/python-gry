# Krzysztof Garbala
# -*- coding: utf-8 -*-
# Python 3.4
''' Memory'''

import tkinter, tkinter.messagebox, random
WIDTH = 500
HEIGHT = 50
OPTION = 0
COUNT = 0
D = []
A = []
B = []
CARDDECK = []
TEX = [0]*16
STATE = False

while len(CARDDECK) < 16:
    CARDS = random.randrange(0, 10)
    if CARDS in CARDDECK:
        continue
    CARDDECK.append(CARDS)
    CARDDECK.append(CARDS)

def new_game():
    '''nowa gra'''
    global COUNT, OPTION, A, B, D, STATE
    OPTION = 0
    COUNT = 0
    B = []
    A = []
    D = [False]*16
    random.shuffle(CARDDECK)
    L.config(text='Turns = ' + str(COUNT))
    if STATE:
        for card in range(0, 16):
            C.delete(TEX[card])
    for pos, card in zip(range(0, 850, 50), range(0, 16)):
        TEX[card] = C.create_text((pos+25, 50), fill='Green', \
	    text=str(CARDDECK[card]), font=("Helvectica", "30"))
    STATE = True

def mouseclick(event):
    '''klikanie na ekranie'''
    global OPTION, COUNT
    if event.x in range(0, 800) and event.y in range(0, 100):
        A.append(event.x//50) # pozycja kliknięcia
        B.append(CARDDECK[event.x//50])  # wartosc karty odkrytej
        if OPTION == 0:
            if D[A[-1]] == False:
                OPTION = 1
                C.itemconfig(TEX[A[-1]], fill='purple', \
		    font=("Helvectica", "30"))
                D[A[-1]] = True
        elif OPTION == 1:
            if D[A[-1]] == False and A[-1] != A[-2]:
                C.itemconfig(TEX[A[-1]], fill='purple', \
		    font=("Helvectica", "30"))
                OPTION = 2
                COUNT += 1
                D[A[-1]] = True
        elif OPTION == 2:
            if D[A[-1]] == False:
                C.itemconfig(TEX[A[-1]], fill='purple', \
		    font=("Helvectica", "30"))
                OPTION = 1
                D[A[-1]] = True
            if B[-2] != B[-3]:
                C.itemconfig(TEX[A[-2]], fill='Green', \
		    font=("Helvectica", "30"))
                C.itemconfig(TEX[A[-3]], fill='Green', \
		    font=("Helvectica", "30"))
                D[A[-2]] = False
                D[A[-3]] = False

    L.config(text='Turns = ' + str(COUNT))
    counter = 0
    for num in range(0, len(D)-1):
        if D[num] == True:
            counter += 1
    if counter+1 == len(D):
        new_game()
        wins()
        counter = 0

def draw(canvas):
    '''rysowanie na ekranie'''
    global WIDTH
    for WIDTH, pos in zip(range(0, 850, 50), range(0, len(CARDDECK))):
        if D[pos] == True:
            canvas.create_line((WIDTH+25, 0), (WIDTH+25, 100))
    # obramowanie
    for pos, num  in zip(range(0, 850, 50), range(0, 16)):
        canvas.create_line((pos, 1), (pos, 100), fill='Red', width=5)

def wins():
    '''messagebox przy zwyciestwie'''
    tkinter.messagebox.showinfo("You wins", "New Game")

FRAME = tkinter.Tk() # okienko
FRAME.minsize(800, 100)
FRAME.title("Memory")
B = tkinter.Button(FRAME, text="New Game", command=new_game)
C = tkinter.Canvas(FRAME, bg="green", height=100, width=800)
L = tkinter.Label(FRAME, text="Turns = 0")
#B2 = tkinter.Button(FRAME, text ="Hello", command = wins)
#B2.pack()
B.pack()
C.pack()
L.pack()
new_game()
draw(C)
C.create_line((0, 0), (0, 100), fill='Red', width=10)
C.create_line((0, 1), (800, 1), fill='Red', width=10)
C.create_line((0, 100), (800, 100), fill='Red', width=10)
C.create_line((800, 0), (800, 100), fill='Red', width=10)
FRAME.bind("<Button-1>", mouseclick)
FRAME.mainloop() # wywolanie okienka
