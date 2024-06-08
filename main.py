from tkinter import *
from PIL import ImageTk, Image
import json
import time

master = Tk()

def uiPrint():
    info()
    print("")
    print(click)
    blankLine()

def info():
    print("More Sex purchases need 50 clicks!")


info()

click = 0
mult = 1
dcp1 = 0





image = Image.open("h3xer.png")
bgimg = ImageTk.PhotoImage(image)

var = StringVar()
var.set(click)
var1 = StringVar()
var1.set(mult)
def updateData():
    var.set(click)
    var1.set(mult)


def blankLine():
    for i in range(20):
        print("")

def purchaseMoreSexCommand():
    global click
    global mult
    if click < 50:
        print("Not enough sex!")
        blankLine()
    elif click >= 50:
        mult = mult+1
        click = click - 50
        print("More Sex Purchased!")
        blankLine()
        updateData()

def purchaseMoreSexX10Command():
    global click
    global mult
    if click < 50:
        print("Not enough sex!")
        blankLine()
    elif click >= 500:
        mult = mult+10
        click = click - 500
        print("Max Sex Purchased!")
        blankLine()
        updateData()

def purchaseMoreSexX100Command():
    global click
    global mult
    if click < 5000:
        print("Not enough sex!")
        blankLine()
    elif click >= 5000:
        mult = mult+100
        click = click - 5000
        print("Max Sex Purchased!")
        blankLine()
        updateData()
def buttonCommand():
    global click
    global mult
    click += 1*(mult)
    uiPrint()
    updateData()
    dataUpdate()


    if click == 100:
        print('''Achievement Unlocked: Junior Clicker!
        BONUS 100 SEX!''')
        click += 100

    elif click == 400:
        print ('''Achievement Unlocked: Little Ninja Clicks!
        BONUS SEX!''')
        click += 300

    elif click == 1500:
        print ('''Achievement Unlocked: Click Ninja Master!
        EVEN MORE SEX!''')
        mult = mult * 4

    elif click == 3000:
        print ('''Achievement Unlocked:  Jackie Chan Style!
        EVEN MORE FUCKING SEX!''')
        mult = mult * 8


data = {
        "click": click,
        "mult": mult,
}
def dataUpdate():
    global data
    data = {
        "click": click,
        "mult": mult,
    }

def save():
    with open("save.json", "w") as f:
        json.dump(data, f,)
def load():
    global data
    global click
    global mult
    with open("save.json", "r") as f:
        data = json.load(f)
        click = data["click"]
        mult = data["mult"]
    updateData()

mainClickButton = Button(master, text="Sex!", command = buttonCommand)
mainClickButton.pack()

purchaseDoubleClickButton = Button(master, text="Purchase More Sex x1", command = purchaseMoreSexCommand)
purchaseDoubleClickButton.pack(side=TOP, anchor=NE,)

purchaseDoubleClickButton2 = Button(master, text="Purchase More Sex x10", command = purchaseMoreSexX10Command)
purchaseDoubleClickButton2.pack(side=TOP, anchor=NE,)

purchaseDoubleClickButton2 = Button(master, text="Purchase More Sex x100", command = purchaseMoreSexX100Command)
purchaseDoubleClickButton2.pack(side=TOP, anchor=NE,)

mainClickButton = Button(master, text="Load", command = load)
mainClickButton.pack(side=BOTTOM, anchor=NW)

mainClickButton = Button(master, text="Save", command = save)
mainClickButton.pack(side=BOTTOM, anchor=NW)



label = Label(master, text="Sex:")
label.pack(side=TOP, anchor=NW,)
label = Label(master, textvariable=var)
label.pack(side=TOP, anchor=NW,)
label = Label(master, text="Multiplier:")
label.pack(side=TOP, anchor=NW,)
label = Label(master, textvariable=var1)
label.pack(side=TOP, anchor=NW,)
label = Label(master, text="Multiplier:")
label.pack(side=TOP, anchor=NW,)
label = Label(master, textvariable=var1)
label.pack(side=TOP, anchor=NW,)

label = Label(master, image=bgimg)
label.pack()


master.title("Sex With H3xer")
master.geometry("%sx%s+%s+%s" % (600,800,512,512))
mainloop()