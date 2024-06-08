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
asx = 0
asxmulti = 1
prest = 1
adv = "No Achievements"


image = Image.open("h3xer.png")
bgimg = ImageTk.PhotoImage(image)

var = StringVar()
var.set(click)
var1 = StringVar()
var1.set(mult)
var2 = StringVar()
var2.set(asx)
var3 = StringVar()
var3.set(asxmulti)
var4 = StringVar()
var4.set(prest)
def updateData():
    var.set(click)
    var1.set(mult)
    var2.set(asx)
    var3.set(asxmulti)
    var4.set(prest)

def prestige():
    global prest
    global click
    global asx
    global mult
    global asxmult
    if click >= 100000*prest:
        prest += 1
        click = 0
        asx = 1*prest
        asxmult = 1*prest
        mult = 1*prest
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

def purchaseAutoClickerCommand():
    global click
    global asx # declare global
    if click < 70:
        print("Not enough clicks!")
        blankLine()
    else:
        click -= 70 # pay for an autoclicker
        print("Auto clicker purchased!")
        asx += 1 # receive an autoclicker
        updateData()

def purchaseASXUpgrade():
    global click
    global asxmulti
    if click < 1000:
        print("Not enough sex!")
        blankLine()
    elif click >= 1000:
        asxmulti += 1
        click = click - 1000
        print("Auto Sex Upgrade Purchased!")
        blankLine()
        updateData()

def autoclick():
    global master
    global click
    global asx
    click += asx*asxmulti # get clicks from autoclickers
    updateData()
    master.after(1000, autoclick) # do this again 1 second later


def reset():
    global click
    global asx
    global mult
    global asxmulti
    asx = 0
    click =0
    mult = 1
    asxmulti = 1

def buttonCommand():
    global click
    global mult
    global adv
    click += 1*(mult)
    uiPrint()
    updateData()
    dataUpdate()

data = {
    "click": click,
    "mult": mult,
    "asx": asx,
    "asxmulti": asxmulti,
    "prest": prest,
}
def dataUpdate():
    global data
    data = {
        "click": click,
        "mult": mult,
        "asx": asx,
        "asxmulti": asxmulti,
        "prest": prest,
}

def save():
    with open("save.json", "w") as f:
        json.dump(data, f,)
def load():
    global data
    global click
    global mult
    global asx
    global asxmulti
    global prest
    with open("save.json", "r") as f:
        data = json.load(f)
        click = data["click"]
        mult = data["mult"]
        asx = data["asx"]
        asxmulti = data["asxmulti"]
        prest = data["prest"]
    updateData()
label = Label(master, image=bgimg)
label.place(x=0, y=0, relwidth=1, relheight=1)

mainClickButton = Button(master, text="Sex!", command = buttonCommand)
mainClickButton.pack(side=TOP,)

purchaseDoubleClickButton = Button(master, text="Purchase More Sex x1", command = purchaseMoreSexCommand)
purchaseDoubleClickButton.pack(side=TOP, anchor=NE,)

purchaseDoubleClickButton2 = Button(master, text="Purchase More Sex x10", command = purchaseMoreSexX10Command)
purchaseDoubleClickButton2.pack(side=TOP, anchor=NE,)

purchaseDoubleClickButton2 = Button(master, text="Purchase More Sex x100", command = purchaseMoreSexX100Command)
purchaseDoubleClickButton2.pack(side=TOP, anchor=NE,)

purchaseAutoClickerButton = Button(master, text="Purchase Auto Sex Machine", command = purchaseAutoClickerCommand)
purchaseAutoClickerButton.pack(side=TOP, anchor=NE,)
purchaseASXUpgrade = Button(master, text="Purchase Auto Sex Upgrade", command = purchaseASXUpgrade)
purchaseASXUpgrade.pack(side=TOP, anchor=NE,)

mainClickButton = Button(master, text="Load", command = load)
mainClickButton.pack(side=BOTTOM, anchor=NW)

mainClickButton = Button(master, text="Save", command = save)
mainClickButton.pack(side=BOTTOM, anchor=NW)

mainClickButton = Button(master, text="Reset", command = reset)
mainClickButton.pack(side=BOTTOM, anchor=NE)
mainClickButton = Button(master, text="Prestige", command = prestige)
mainClickButton.pack(side=BOTTOM, anchor=NE)



label = Label(master, text="Sex:")
label.pack(side=TOP, anchor=NW,)
label = Label(master, textvariable=var)
label.pack(side=TOP, anchor=NW,)
label = Label(master, text="Multiplier:")
label.pack(side=TOP, anchor=NW,)
label = Label(master, textvariable=var1)
label.pack(side=TOP, anchor=NW,)
label = Label(master, text="Auto Sex:")
label.pack(side=TOP, anchor=NW,)
label = Label(master, textvariable=var2)
label.pack(side=TOP, anchor=NW,)
label = Label(master, text="Auto Sex Multiplier:")
label.pack(side=TOP, anchor=NW,)
label = Label(master, textvariable=var3)
label.pack(side=TOP, anchor=NW,)
label = Label(master, text="Prestige:")
label.pack(side=TOP, anchor=NW,)
label = Label(master, textvariable=var4)
label.pack(side=TOP, anchor=NW,)



autoclick()
master.title("Sex With H3xer")
master.geometry("%sx%s+%s+%s" % (600,800,512,512))
mainloop()