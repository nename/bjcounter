"""
author: Tomas Hampl
date: 1/11/2020
name of the file: counter.py
description: program to count cards and give basic strategy advices
"""

# !/usr/bin/python
# -*- coding: utf-8 -*-

# libraries
import tkinter as tk
from tkinter import ttk
from tkinter import *

# mine libraries
import cheatsheet as chs

# global counters
runningCount = cardCount = deckCount = trueCount = 0

# global cards
firstCard = secCard = dealerCard = 0

# functions
# add 1 to deck count
def deckAddCount():
    global cardCount, deckCount

    cardCount = 0
    deckCount = deckCount + 1

    cardCountLabel.configure(text=f'{cardCount}')
    deckCountLabel.configure(text=f'{deckCount}')

# add 1 to running count and to card count
def clickAdd():
    global runningCount, cardCount, deckCount, trueCount
    cardCount = cardCount + 1
    runningCount = runningCount + 1
    trueCount = runningCount / (8 - deckCount)

    if cardCount >= 52:
        deckAddCount()

    runningCountLabel.configure(text=f'{runningCount}')
    cardCountLabel.configure(text=f'{cardCount}')
    trueCountLabel.configure(text=f'{trueCount}')

# add -1 to running count and 1 to card count
def clickMinus():
    global runningCount, cardCount, deckCount, trueCount
    cardCount = cardCount + 1
    runningCount = runningCount - 1
    trueCount = runningCount / (8 - deckCount)

    if cardCount >= 52:
        deckAddCount()

    runningCountLabel.configure(text=f'{runningCount}')
    cardCountLabel.configure(text=f'{cardCount}')
    trueCountLabel.configure(text=f'{trueCount}')

# add 1 to card count
def clickNeutral():
    global cardCount, deckCount, trueCount
    cardCount = cardCount + 1
    trueCount = runningCount / (8 - deckCount)

    if cardCount >= 52:
        deckAddCount()

    cardCountLabel.configure(text=f'{cardCount}')
    trueCountLabel.configure(text=f'{trueCount}')

# reset counters
def reset():
    global runningCount, cardCount, deckCount, trueCount
    runningCount = cardCount = deckCount = trueCount = 0

    runningCountLabel.configure(text=f'{runningCount}')
    cardCountLabel.configure(text=f'{cardCount}')
    deckCountLabel.configure(text=f'{deckCount}')
    trueCountLabel.configure(text=f'{trueCount}')

# set card values to globals
def setCardValues(*args):
    global firstCard, secCard, dealerCard

    firstCard = clicked1.get()
    secCard = clicked2.get()
    dealerCard = clicked3.get()

# display advice
def giveAdvice():
    global firstCard, secCard, dealerCard

    print(firstCard, secCard, dealerCard)

    if not firstCard or not secCard or not dealerCard or firstCard == 0 or secCard == 0 or dealerCard == 0:
        adviceResLabel.configure(text="0")
        return

    advice = ""
    indexDealer = chs.dropDownOptions.index(dealerCard)

    # split pair
    if firstCard == secCard:
        index = chs.dropDownOptions.index(firstCard)
        advice = chs.pairSplitting[index][indexDealer]

    # soft pair
    elif firstCard == "A":
        if int(secCard) > 9:
            advice = "S"
        else:
            index = chs.dropDownOptions.index(secCard)
            advice = chs.softCards[index][indexDealer]

    # hard pair
    else:
        res = int(firstCard) + int(secCard)
        if res < 8:
            advice = "H"
        elif res > 17:
            advice = "S"
        else:
            index = chs.hardTotals.index(str(res))
            advice = chs.hardCards[index][indexDealer]

    adviceResLabel.configure(text=f'{advice}')

# init
windows = tk.Tk()
windows.title("BJ counter")
windows.geometry("340x310")

# labels for counts
runningLabel = tk.Label(windows, text="running count:")
runningLabel.grid(column=0, row=1)

runningCountLabel = tk.Label(windows, text="0")
runningCountLabel.grid(column=1, row=1)

cardLabel = tk.Label(windows, text="card count:")
cardLabel.grid(column=0, row=2)

cardCountLabel = tk.Label(windows, text="0")
cardCountLabel.grid(column=1, row=2)

deckLabel = tk.Label(windows, text="deck count:")
deckLabel.grid(column=0, row=3)

deckCountLabel = tk.Label(windows, text="0")
deckCountLabel.grid(column=1, row=3)

trueLabel = tk.Label(windows, text="true count:")
trueLabel.grid(column=0, row=4)

trueCountLabel = tk.Label(windows, text="0")
trueCountLabel.grid(column=1, row=4)

# labels for cards
firstCardLabel = tk.Label(windows, text="first card")
firstCardLabel.grid(column=0, row=6)

secCardLabel = tk.Label(windows, text="second card")
secCardLabel.grid(column=1, row=6)

dealerCardLabel = tk.Label(windows, text="dealers card")
dealerCardLabel.grid(column=2, row=6)

# labels for advice
adviceLabel = tk.Label(windows, text="next move")
adviceLabel.grid(column=0, row=9)

adviceResLabel = tk.Label(windows)
adviceResLabel.grid(column=1, row=9)

hintLabel = tk.Label(windows, text="H - hit\nS - stand\nD - double\\hit\nDs - double\\stand\nN - do not split\n"
                                   "Y - split")
hintLabel.grid(column=1, row=10)

# buttons +, 0, -, reset
lowNumButton = ttk.Button(windows, text="2-6", command=clickAdd)
lowNumButton.grid(column=0, row=0)

neutralNumButton = ttk.Button(windows, text="7-9", command=clickNeutral)
neutralNumButton.grid(column=1, row=0)

highNumButton = ttk.Button(windows, text="10-A", command=clickMinus)
highNumButton.grid(column=2, row=0)

resetCountsButton = ttk.Button(windows, text="reset", command=reset)
resetCountsButton.grid(column=3, row=0)

# buttons for advice
adviceButton = ttk.Button(windows, text="advice", command=giveAdvice)
adviceButton.grid(column=1, row=8)

# dropdown for cards
clicked1 = StringVar()
clicked2 = StringVar()
clicked3 = StringVar()

dropDown1 = OptionMenu(windows, clicked1, *chs.dropDownOptions)
dropDown1.grid(column=0, row=7)

dropDown2 = OptionMenu(windows, clicked2, *chs.dropDownOptions)
dropDown2.grid(column=1, row=7)

dropDown3 = OptionMenu(windows, clicked3, *chs.dropDownOptions)
dropDown3.grid(column=2, row=7)

clicked1.trace('w', setCardValues)
clicked2.trace('w', setCardValues)
clicked3.trace('w', setCardValues)

windows.mainloop()
