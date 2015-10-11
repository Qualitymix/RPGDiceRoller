import random
import Tkinter
from array import *
from Tkinter import *

root = Tk()
root.title("RPG Dice Roller")

textframe = Frame(root)
listframe = Frame(root)

amountAMT = Entry(textframe, width=5)
amountMOD = Entry(textframe, width=5)
amountINPT = int()




def D2():
    dtype = 2
    Roll(GetAMT(), dtype)
def D3():
    dtype = 3
    Roll(GetAMT(), dtype)
def D4():
    dtype = 4
    Roll(GetAMT(), dtype)
def D6():
    dtype = 6
    Roll(GetAMT(), dtype)
def D8():
    dtype = 8
    Roll(GetAMT(), dtype)
def D10():
    dtype = 10
    Roll(GetAMT(), dtype)
def D12():
    dtype = 12
    Roll(GetAMT(), dtype)
def D20():
    dtype = 20
    Roll(GetAMT(), dtype)
def D100():
    dtype = 100
    Roll(GetAMT(), dtype)

def GetAMT():
    try:
        text_contents = int(amountAMT.get())
    except ValueError:
        text_contents=1
    if not amountAMT.get():
        text_contents=1
    amountINPT = text_contents
    return amountINPT

def GetMOD():
    try:
        text_contentsM = int(amountMOD.get())
    except ValueError:
        text_contentsM=1
    if not amountMOD.get():
        text_contentsM=0
    amountMODINPT = text_contentsM
    return amountMODINPT

def Roll(inpt, dtype):
    textBox.delete(1.0, END)
    amountpass = 0
    total = 0
    dicearray = array('i')

    while amountpass < inpt:
        x = random.randint(1, dtype)
        dicearray.insert(amountpass, x)
        amountpass = amountpass + 1
        textBox.insert(INSERT,'Roll ')
        textBox.insert(INSERT,amountpass)
        textBox.insert(INSERT, ': ')
        #textBox.insert(INSERT,'\n')
        textBox.insert(INSERT,x)
        textBox.insert(INSERT,'\n')

    for i in dicearray:
        total = total + i
    totalRoll = total + GetMOD()
    if (totalRoll <= 0):
        totalRoll = 0
    textBox.insert(INSERT, 'Total:')
    textBox.insert(INSERT, total)
    if (GetMOD() >= 0):
        textBox.insert(INSERT, ' + ')
    if (GetMOD() < 0):
        textBox.insert(INSERT, ' - ')
    textBox.insert(INSERT, abs(GetMOD()))
    textBox.insert(INSERT, ' = ')
    textBox.insert(INSERT, totalRoll)


buttonD2 = Button(textframe, text ="D2", command = D2)
buttonD3 = Button(textframe, text ="D3", command = D3)
buttonD4 = Button(textframe, text ="D4", command = D4)
buttonD6 = Button(textframe, text ="D6", command = D6)
buttonD8 = Button(textframe, text ="D8", command = D8)
buttonD10 = Button(textframe, text ="D10", command = D10)
buttonD12 = Button(textframe, text ="D12", command = D12)
buttonD20 = Button(textframe, text ="D20", command = D20)
buttonD100 = Button(textframe, text ="D100", command = D100)






scrollbar = Scrollbar(listframe, orient=VERTICAL)
textBox = Text(listframe, yscrollcommand=scrollbar.set)
scrollbar.configure(command=textBox.yview)
lblAMT = Tkinter.Label(textframe, text="Amount:")
lblMOD = Tkinter.Label(textframe, text="Mod:")
lblMODpn = Tkinter.Label(textframe, text = "(+/-)")

lblAMT.pack(side=LEFT)
amountAMT.pack(side=LEFT, fill=X)
buttonD2.pack(side=LEFT)
buttonD3.pack(side=LEFT)
buttonD4.pack(side=LEFT)
buttonD6.pack(side=LEFT)
buttonD8.pack(side=LEFT)
buttonD10.pack(side=LEFT)
buttonD12.pack(side=LEFT)
buttonD20.pack(side=LEFT)
buttonD100.pack(side=LEFT)
lblMOD.pack(side=LEFT)
amountMOD.pack(side=LEFT, fill=X)
lblMODpn.pack(side=LEFT)
textBox.pack(side=LEFT, expand=1)
scrollbar.pack(side=RIGHT, fill=Y)
textframe.pack(fill=BOTH)
listframe.pack(fill=BOTH, expand=1)

#root.geometry("800x400")





root.mainloop()


#amount = int(input('Amount of dice: '))








