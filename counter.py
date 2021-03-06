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

# globals
NUMBER_OF_CARDS = 52
runningCount = cardCount = deckCount = trueCount = 0
firstCard = secCard = dealerCard = 0
numOfDecs = 8

# functions
# calculate true count
def calculateTrueCount(deckCount, runningCount):
    global cardCount, trueCount

    cardCount = cardCount + 1
    trueCount = round(runningCount / (float(numOfDecs) - (deckCount + cardCount / 52)), 2)

# add 1 to deck count
def deckAddCount(*args):
    global cardCount, deckCount

    cardCount = 0
    deckCount = deckCount + 1

    cardCountLabel.configure(text=f'{cardCount}')
    deckCountLabel.configure(text=f'{deckCount}')

# add 1 to running count and to card count
def clickAdd(*args):
    global runningCount, cardCount, deckCount, trueCount

    runningCount = runningCount + 1

    calculateTrueCount(deckCount, runningCount)

    if cardCount >= 52:
        deckAddCount()

    runningCountLabel.configure(text=f'{runningCount}')
    cardCountLabel.configure(text=f'{cardCount}')
    trueCountLabel.configure(text=f'{trueCount}')

# add -1 to running count and 1 to card count
def clickMinus(*args):
    global runningCount, cardCount, deckCount, trueCount

    runningCount = runningCount - 1

    calculateTrueCount(deckCount, runningCount)

    if cardCount >= NUMBER_OF_CARDS:
        deckAddCount()

    runningCountLabel.configure(text=f'{runningCount}')
    cardCountLabel.configure(text=f'{cardCount}')
    trueCountLabel.configure(text=f'{trueCount}')

# add 1 to card count
def clickNeutral(*args):
    global cardCount, deckCount, trueCount

    calculateTrueCount(deckCount, runningCount)

    if cardCount >= NUMBER_OF_CARDS:
        deckAddCount()

    cardCountLabel.configure(text=f'{cardCount}')
    trueCountLabel.configure(text=f'{trueCount}')

# reset counters
def reset(*args):
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
def giveAdvice(*args):
    global firstCard, secCard, dealerCard

    if not firstCard or not secCard or not dealerCard or firstCard == 0 or secCard == 0 or dealerCard == 0:
        return adviceResLabel.configure(text=" ")

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

# set number of decs
def setNumOfDecs(*args):
    global numOfDecs, cardCount, deckCount

    if cardCount > 0 or deckCount > 0:
        return entryBoxDeckCount.config({"background": "Red"})

    numOfDecs = entryBoxDeckCount.get()
    entryBoxDeckCount.config({"background": "White"})
    if int(numOfDecs) <= 0:
        entryBoxDeckCount.config({"background": "Red"})
        numOfDecs = 8

    cardCountLabel.configure(text=f'{cardCount}')
    deckCountLabel.configure(text=f'{deckCount}')

def setNumOfCards(*args):
    global cardCount, deckCount

    if cardCount > 0 or deckCount > 0:
        return entryBoxCardCount.config({"background": "Red"})
    else:
        entryBoxCardCount.config({"background": "White"})

    count = entryBoxCardCount.get()

    if "." in count:
        pre, post = ([int(x)] for x in count.split(".", 1))
        deckCount = int(pre[0])
        num = "0." + str(post[0])
        cardCount = float(num) * NUMBER_OF_CARDS
        cardCount = int(cardCount)
    else:
        deckCount = deckCount + int(count)

    cardCountLabel.configure(text=f'{cardCount}')
    deckCountLabel.configure(text=f'{deckCount}')

# init
windows = tk.Tk()
windows.title("BJ counter")
windows.geometry("360x380")

# labels for counts
runningLabel = tk.Label(windows, text="running count:")
runningLabel.grid(column=0, row=3)

runningCountLabel = tk.Label(windows, text="0")
runningCountLabel.grid(column=1, row=3)

cardLabel = tk.Label(windows, text="card count:")
cardLabel.grid(column=0, row=4)

cardCountLabel = tk.Label(windows, text="0")
cardCountLabel.grid(column=1, row=4)

deckLabel = tk.Label(windows, text="deck count:")
deckLabel.grid(column=0, row=5)

deckCountLabel = tk.Label(windows, text="0")
deckCountLabel.grid(column=1, row=5)

trueLabel = tk.Label(windows, text="true count:")
trueLabel.grid(column=0, row=6)

trueCountLabel = tk.Label(windows, text="0")
trueCountLabel.grid(column=1, row=6)

# labels for cards
firstCardLabel = tk.Label(windows, text="first card")
firstCardLabel.grid(column=0, row=8)

secCardLabel = tk.Label(windows, text="second card")
secCardLabel.grid(column=1, row=8)

dealerCardLabel = tk.Label(windows, text="dealers card")
dealerCardLabel.grid(column=2, row=8)

# labels for advice
adviceLabel = tk.Label(windows, text="next move:")
adviceLabel.grid(column=0, row=11)

adviceResLabel = tk.Label(windows)
adviceResLabel.grid(column=1, row=11)

# labels for hint
hintLabel = tk.Label(windows, text="H - hit\nS - stand\nD - double\\hit\nDs - double\\stand\nN - do not split\n"
                                   "Y - split")
hintLabel.grid(column=0, row=12, columnspan=2)

# labels for controls
controlLabel = tk.Label(windows, text="controls:\nup - high num\ndown - low num\nright - neut num\nleft - neut num\n"
                        "r - reset")
controlLabel.grid(column=2, row=12)

# labels for entry
entryLabelDeckCount = tk.Label(windows, text="Number of decks\nDefault 8")
entryLabelDeckCount.grid(column=0,row=0)

entryLabelCardCount = tk.Label(windows, text="Number of decks\nplayed")
entryLabelCardCount.grid(column=0, row=1)

# buttons +, 0, -, reset
lowNumButton = ttk.Button(windows, text="2-6", command=clickAdd)
lowNumButton.grid(column=0, row=2)

neutralNumButton = ttk.Button(windows, text="7-9", command=clickNeutral)
neutralNumButton.grid(column=1, row=2)

highNumButton = ttk.Button(windows, text="10-A", command=clickMinus)
highNumButton.grid(column=2, row=2, padx=11)

resetCountsButton = ttk.Button(windows, text="reset", command=reset)
resetCountsButton.grid(column=3, row=2)

# buttons for advice
adviceButton = ttk.Button(windows, text="advice", command=giveAdvice)
adviceButton.grid(column=1, row=10)

# buttons for entry box
entryButtonDeckCount = ttk.Button(windows, text="set", command=setNumOfDecs)
entryButtonDeckCount.grid(column=2, row=0)

entryButtonCardCount = ttk.Button(windows, text="set", command=setNumOfCards)
entryButtonCardCount.grid(column=2, row=1)

# dropdown for cards
clicked1 = StringVar()
clicked2 = StringVar()
clicked3 = StringVar()

dropDown1 = OptionMenu(windows, clicked1, *chs.dropDownOptions)
dropDown1.grid(column=0, row=9)

dropDown2 = OptionMenu(windows, clicked2, *chs.dropDownOptions)
dropDown2.grid(column=1, row=9)

dropDown3 = OptionMenu(windows, clicked3, *chs.dropDownOptions)
dropDown3.grid(column=2, row=9)

clicked1.trace('w', setCardValues)
clicked2.trace('w', setCardValues)
clicked3.trace('w', setCardValues)

# binding key presses to buttons
windows.bind('<Up>', clickMinus)
windows.bind('<Down>', clickAdd)
windows.bind('<Left>', clickNeutral)
windows.bind('<Right>', clickNeutral)
windows.bind('<r>', reset)

# entry box for deck count
entryBoxDeckCount = tk.Entry(windows, width=10, justify='center')
entryBoxDeckCount.grid(column=1, row=0)
entryBoxDeckCount.insert(0, "8")

entryBoxCardCount = tk.Entry(windows, width=10, justify='center')
entryBoxCardCount.grid(column=1, row=1)
entryBoxCardCount.insert(0, "0")

# main loop
windows.mainloop()
