from tkinter import *
from PIL import ImageTk, Image
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
image2 = Image.open("h3xer-hand.png")
bgimg2 = ImageTk.PhotoImage(image2)
var = StringVar()
var.set(click)

def updateClicks():
    var.set(click)

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
        updateClicks()





def buttonCommand():
    global click
    global mult
    click += 1*(mult)
    uiPrint()
    updateClicks()


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

mainClickButton = Button(master, text="Sex!", command = buttonCommand)
mainClickButton.pack()

purchaseDoubleClickButton = Button(master, text="Purchase More Sex", command = purchaseMoreSexCommand)
purchaseDoubleClickButton.pack()

label = Label(master, textvariable=var)
label.pack(side=TOP, anchor=NW,)

label = Label(master, image=bgimg)
label.pack()


master.title("Sex With H3xer")
master.geometry("%sx%s+%s+%s" % (400,600,512,512))
mainloop()