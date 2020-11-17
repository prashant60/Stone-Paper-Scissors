from tkinter import *
from Stone_Paper_Scissor import *
import time

root=Tk()

comp1 = StringVar()
user1 = StringVar()
variable1=StringVar()

root['bg'] = 'wheat'
root.title("STONE-PAPER-SCISSORS")
root.resizable(0,0)

label1 = Label(root, text="STONE-PAPER-SCISSOR")
label1.pack()
label1.place(y=1, height=80)
label1.config(bg="red", width=20, anchor=CENTER, bd=8, font = ("jokerman", "20"), background='#88d8c0', relief=RAISED, fg="red")

mylabel = Label(root, text="    Developed by ------ Prashant Goel     ")
mylabel.pack()
mylabel.config(bg='aqua', bd=0, height=2, fg="red", font=("","14", "bold"))
mylabel.place(y=242)

def count1():
    label_u = Label(root, text="scissor!", relief=SUNKEN)
    label_u.pack()
    label_u.config(bg='black', bd=6, height=2, width=10, fg="red", font=("", "14", "bold"))
    label_u.place(x=242, y=191)
    label_u.after(400,var_img)
    
def count2():
    label2 = Label(root, text="paper!", relief=SUNKEN)
    label2.pack()
    label2.config(bg='black', bd=6, height=2, width=10, fg="red", font=("", "14", "bold"))
    label2.place(x=108, y=191)
    label2.after(400,count1)

def count3():
    label_c = Label(root, text="stone!", relief=SUNKEN)
    label_c.pack()
    label_c.config(bg='black', bd=6, height=2, width=10, fg="red", font=("", "14", "bold"))
    label_c.place(y=191)
    label_c.after(400,count2)

def var_img():
    label_c = Label(root, bg='red', bd=8, relief=SUNKEN)
    label_c.pack()
    label_c.config(image=photo_c, width=92, height=42)
    label_c.place(y=191)

    label2 = Label(root, textvariable=variable1, relief=SUNKEN)
    label2.pack()
    label2.config(bg='black', bd=6, height=2, width=10, fg="red", font=("", "14", "bold"))
    label2.place(x=108, y=191)
    
    label_u = Label(root, bg='red', bd=8, relief=SUNKEN)
    label_u.pack()
    label_u.config(image=photo_u, width=92, height=42)
    label_u.place(x=242, y=191)

def blank_var():
    label_c = Label(root, relief=SUNKEN)
    label_c.pack()
    label_c.config(bg='red', bd=6, height=2, width=10, fg="red", font=("", "14", "bold"))
    label_c.place(y=191)

    label2 = Label(root, relief=SUNKEN)
    label2.pack()
    label2.config(bg='red', bd=6, height=2, width=10, fg="red", font=("", "14", "bold"))
    label2.place(x=108, y=191)
    
    label_u = Label(root, relief=SUNKEN)
    label_u.pack()
    label_u.config(bg='red', bd=6, height=2, width=10, fg="red", font=("", "14", "bold"))
    label_u.place(x=242, y=191)

    label_u.after(300,count3)
    
def play():
    score1 = Label(root, text="COMPUTER: ")
    score1.pack()
    score1.config(bg='aqua', bd=0, height=2, fg="red", font=("", "14", "bold"))
    score1.place(y=80)

    score3 = Label(root, textvariable=comp1)
    score3.pack()
    score3.config(bg='yellow', bd=0, height=2, width=5, fg="red", font=("", "14", "bold"))
    score3.place(x=125, y=80)

    sep = Label(root)
    sep.pack()
    sep.config(bg='red', bd=0, height=2, width=1, fg="red", font=("", "14", "bold"))
    sep.place(x=186, y=80)

    score2 = Label(root, text="USER: ")
    score2.pack()
    score2.config(bg='aqua', bd=0, height=2, fg="red", font=("", "14", "bold"))
    score2.place(x=199, y=80)

    score4 = Label(root, textvariable=user1)
    score4.pack()
    score4.config(bg='yellow', bd=0, height=2, width=7, fg="red", font=("", "14", "bold"))
    score4.place(x=265, y=80)

    stone_button = Button(root, bg='blue', bd=8, relief=RAISED, cursor="hand2", command=stone)
    stone_button.pack()
    stone_button.config(image=photo1,  width=98, height=48)
    stone_button.place(y=126)

    paper_button = Button(root, bg='blue', bd=8, relief=RAISED, cursor="hand2", command=paper)
    paper_button.pack()
    paper_button.config(image=photo2, width=99, height=48)
    paper_button.place(x=116, y=126)

    scissor_button = Button(root, bg='blue', bd=8, relief=RAISED, cursor="hand2", command=scissor)
    scissor_button.pack()
    scissor_button.config(image=photo3, width=98, height=48)
    scissor_button.place(x=233, y=126)
    
    var_img()

photo = PhotoImage(file='C:\\Users\\Prashant\\Documents\\GitHub\\Stone-Paper-Scissors\\photo.png')
photo1 = PhotoImage(file='C:\\Users\\Prashant\\Documents\\GitHub\\Stone-Paper-Scissors\\stone.png')
photo2 = PhotoImage(file='C:\\Users\\Prashant\\Documents\\GitHub\\Stone-Paper-Scissors\\paper.png')
photo3 = PhotoImage(file='C:\\Users\\Prashant\\Documents\\GitHub\\Stone-Paper-Scissors\\scissor.png')

photo_u = PhotoImage(file='C:\\Users\\Prashant\\Documents\\GitHub\\Stone-Paper-Scissors\\black_u.png')
photo_c = PhotoImage(file='C:\\Users\\Prashant\\Documents\\GitHub\\Stone-Paper-Scissors\\black_c.png')

game_logo = Label(root, bg="white", bd=0, relief=SUNKEN)
game_logo.pack()
game_logo.config(image=photo, width=350, height=100)
game_logo.place(y=80)

play_button = Button(root, bg="orange", bd=10, relief=SUNKEN, text="PLAY GAME", cursor="hand2", command=play)
play_button.pack()
play_button.config(width=23, font=("","17", "bold"))
play_button.place(y=180)

root.geometry("350x288+100+100")
root.mainloop()
