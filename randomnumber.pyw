from tkinter import *

import easygui
import os

root = Tk()
root.iconbitmap("krtecek2.ico")
root.geometry("300x250")
root.title("Random number generator")
root.grid()

e1 = Entry(root,width=4, font=("Arial", 25))
e1.pack()
e2 = Entry(root,width=4, font=("Arial", 25))
e2.pack()

def randnum(event):
	import random
	value =random.randint(int(e1.get()),int(e2.get()))
	updateDisplay(value)

def updateDisplay(myString):
	displayVariable.set(myString)

button_1 = Button(root, text="random", width=10, font=("Arial", 15))
button_1.bind("<Button-1>",randnum)
button_1.pack()
displayVariable = StringVar()
displayLabel = Label(root, textvariable=displayVariable, font=("Arial", 60))
displayLabel.pack()
root.mainloop()
