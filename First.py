import random
import Tkinter as tk
import array

root = tk.Tk()
root.title("RPG Dice Roller")

textframe = tk.Frame(root)
listframe = tk.Frame(root)

amountAMT = tk.Entry(textframe, width=5)
amountMOD = tk.Entry(textframe, width=5)
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


buttonD2 = tk.Button(textframe, text ="D2", command = D2)
buttonD3 = tk.Button(textframe, text ="D3", command = D3)
buttonD4 = tk.Button(textframe, text ="D4", command = D4)
buttonD6 = tk.Button(textframe, text ="D6", command = D6)
buttonD8 = tk.Button(textframe, text ="D8", command = D8)
buttonD10 = tk.Button(textframe, text ="D10", command = D10)
buttonD12 = tk.Button(textframe, text ="D12", command = D12)
buttonD20 = tk.Button(textframe, text ="D20", command = D20)
buttonD100 = tk.Button(textframe, text ="D100", command = D100)






scrollbar = tk.Scrollbar(listframe, orient=tk.VERTICAL)
textBox = tk.Text(listframe, yscrollcommand=scrollbar.set)
scrollbar.configure(command=textBox.yview)
lblAMT = tk.Label(textframe, text="Amount:")
lblMOD = tk.Label(textframe, text="Mod:")
lblMODpn = tk.Label(textframe, text = "(+/-)")

lblAMT.pack(side=tk.LEFT)
amountAMT.pack(side=tk.LEFT, fill=tk.X)
buttonD2.pack(side=tk.LEFT)
buttonD3.pack(side=tk.LEFT)
buttonD4.pack(side=tk.LEFT)
buttonD6.pack(side=tk.LEFT)
buttonD8.pack(side=tk.LEFT)
buttonD10.pack(side=tk.LEFT)
buttonD12.pack(side=tk.LEFT)
buttonD20.pack(side=tk.LEFT)
buttonD100.pack(side=tk.LEFT)
lblMOD.pack(side=tk.LEFT)
amountMOD.pack(side=tk.LEFT, fill=tk.X)
lblMODpn.pack(side=tk.LEFT)
textBox.pack(side=tk.LEFT, expand=1)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
textframe.pack(fill=tk.BOTH)
listframe.pack(fill=tk.BOTH, expand=1)

#root.geometry("800x400")





root.mainloop()


#amount = int(input('Amount of dice: '))








