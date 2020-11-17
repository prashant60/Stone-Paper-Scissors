import random
import gui
from tkinter import *
comp=0
user=0

def stone():
    global comp
    global user
    options = ["Stone", "Paper", "Scissor"]
    random_item = random.choice(options)

    gui.photo_u=PhotoImage(file='C:\\Users\\Prashant\\Documents\\GitHub\\Stone-Paper-Scissors\\stone.png')
    
    if random_item == "Stone":
        gui.photo_c=PhotoImage(file='C:\\Users\\Prashant\\Documents\\GitHub\\Stone-Paper-Scissors\\stone.png')
        gui.variable1.set("Tie!!!")
        gui.comp1.set(comp)
        gui.user1.set(user)

    elif random_item == "Paper":
        gui.photo_c=PhotoImage(file='C:\\Users\\Prashant\\Documents\\GitHub\\Stone-Paper-Scissors\\paper.png')
        comp+=1
        gui.variable1.set("Computer\nWins!!!")
        gui.comp1.set(comp)
        gui.user1.set(user)

    else:
        gui.photo_c=PhotoImage(file='C:\\Users\\Prashant\\Documents\\GitHub\\Stone-Paper-Scissors\\scissor.png')
        user+=1
        gui.variable1.set("You Win!!!")
        gui.comp1.set(comp)
        gui.user1.set(user)
    gui.var_img()

def paper():
    global comp
    global user
    options = ["Stone", "Paper", "Scissor"]
    random_item = random.choice(options)

    gui.photo_u=PhotoImage(file='C:\\Users\\Prashant\\Documents\\GitHub\\Stone-Paper-Scissors\\paper.png')
    
    if random_item == "Stone":
        gui.photo_c=PhotoImage(file='C:\\Users\\Prashant\\Documents\\GitHub\\Stone-Paper-Scissors\\stone.png')
        user += 1
        gui.variable1.set("You Win!!!")
        gui.comp1.set(comp)
        gui.user1.set(user)

    elif random_item == "Paper":
        gui.photo_c=PhotoImage(file='C:\\Users\\Prashant\\Documents\\GitHub\\Stone-Paper-Scissors\\paper.png')
        gui.variable1.set("Tie!!!")
        gui.comp1.set(comp)
        gui.user1.set(user)

    else:
        gui.photo_c=PhotoImage(file='C:\\Users\\Prashant\\Documents\\GitHub\\Stone-Paper-Scissors\\scissor.png')
        comp += 1
        gui.variable1.set("Computer\nWins!!!")
        gui.comp1.set(comp)
        gui.user1.set(user)
    gui.var_img()

def scissor():
    global comp
    global user
    options = ["Stone", "Paper", "Scissor"]
    random_item = random.choice(options)

    gui.photo_u=PhotoImage(file='C:\\Users\\Prashant\\Documents\\GitHub\\Stone-Paper-Scissors\\scissor.png')

    if random_item == "Stone":
        gui.photo_c=PhotoImage(file='C:\\Users\\Prashant\\Documents\\GitHub\\Stone-Paper-Scissors\\stone.png')
        comp += 1
        gui.variable1.set("Computer\nWins!!!")
        gui.comp1.set(comp)
        gui.user1.set(user)

    elif random_item == "Paper":
        gui.photo_c=PhotoImage(file='C:\\Users\\Prashant\\Documents\\GitHub\\Stone-Paper-Scissors\\paper.png')
        user += 1
        gui.variable1.set("You Win!!!")
        gui.comp1.set(comp)
        gui.user1.set(user)

    else:
        gui.photo_c=PhotoImage(file='C:\\Users\\Prashant\\Documents\\GitHub\\Stone-Paper-Scissors\\scissor.png')
        gui.variable1.set("Tie!!!")
        gui.comp1.set(comp)
        gui.user1.set(user)
    gui.var_img()
