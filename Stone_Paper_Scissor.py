import random
import gui
comp=0
user=0

def stone():
    global comp
    global user
    options = ["Stone", "Paper", "Scissor"]
    random_item = random.choice(options)

    if random_item == "Stone":
        gui.variable1.set("Tie!!!")
        gui.comp1.set(comp)
        gui.user1.set(user)

    elif random_item == "Paper":
        comp+=1
        gui.variable1.set("Computer Wins!!!")
        gui.comp1.set(comp)
        gui.user1.set(user)

    else:
        user+=1
        gui.variable1.set("You Win!!!")
        gui.comp1.set(comp)
        gui.user1.set(user)

def paper():
    global comp
    global user
    options = ["Stone", "Paper", "Scissor"]
    random_item = random.choice(options)

    if random_item == "Stone":
        user += 1
        gui.variable1.set("You Win!!!")
        gui.comp1.set(comp)
        gui.user1.set(user)

    elif random_item == "Paper":
        gui.variable1.set("Tie!!!")
        gui.comp1.set(comp)
        gui.user1.set(user)

    else:
        comp += 1
        gui.variable1.set("Computer Wins!!!")
        gui.comp1.set(comp)
        gui.user1.set(user)

def scissor():
    global comp
    global user
    options = ["Stone", "Paper", "Scissor"]
    random_item = random.choice(options)

    if random_item == "Stone":
        comp += 1
        gui.variable1.set("Computer Wins!!!")
        gui.comp1.set(comp)
        gui.user1.set(user)

    elif random_item == "Paper":
        user += 1
        gui.variable1.set("You Win!!!")
        gui.comp1.set(comp)
        gui.user1.set(user)

    else:
        gui.variable1.set("Tie!!!")
        gui.comp1.set(comp)
        gui.user1.set(user)
