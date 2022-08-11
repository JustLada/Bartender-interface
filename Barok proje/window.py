from ast import Sub
from asyncio import events
from asyncore import close_all
from fileinput import close
from tkinter import *
from PIL import Image,ImageTk
import time as dt

def pouringScreen():
    Pouring = Toplevel()
    Pouring.geometry("800x480")
    canvasPouring = Canvas(
        Pouring,
        bg = "#246371",
        height = 800,
        width = 480,
        bd = 0,
        highlightthickness = 0,
        relief = "raised")
    canvasPouring.create_text(
        240, 220,
        text = "Pouring",
        fill = "black",
        font = ("Bangers", int(40.0)))
    canvasPouring.pack()
    Pouring.configure(bg = "#246371")
    Pouring.attributes('-alpha', 0.8)
    Pouring.after(1300,Pouring.destroy)
    Pouring.resizable(False, False)
    Pouring.overrideredirect(True)
def settingbutton():
    print("closing...")
    exit()
def btn_clicked1():
    print("5cl viski")
    pouringScreen()
def btn_clicked2():
    print("5cl rakı")    
    pouringScreen()
def btn_clicked3():
    print("5cl konyak")
    pouringScreen()
def btn_clicked4():
    print("5cl vodka")
    pouringScreen()
def btn_clicked5():
    print("Plus Button Clicked")  
    
    def viski1():
        print("+1 viski")
        pouringScreen()
        SubViski.destroy()
    def viski2():
        print("+2 viski")
        pouringScreen()
        SubViski.destroy()
    def viski3():
        print("+3 viski")
        pouringScreen()
        SubViski.destroy()
    def lossfocus(event):
        if event.widget is SubViski:
            # check which widget getting the focus
            w = SubViski.tk.call('focus')
        if not w:
            # not widget in this window
            SubViski.destroy()    


    SubViski = Toplevel()
    SubViski.focus_set()

    SubViski.geometry("328x480")
    SubViski.configure(bg = "#DACE8E")
    canvasViski = Canvas(
    SubViski,
    bg = "#DACE8E",
    height = 480,
    width = 328,
    bd = 0,
    highlightthickness = 0,
    relief = "raised")
    canvasViski.place(x = 0, y =0)

    
    
    viskikapak = (Image.open('viski.png'))
    new_image1 = ImageTk.PhotoImage(viskikapak)
    canvasViski.create_image(122,30, anchor=NW, image=new_image1)

    img9 = PhotoImage(file = f"img9.png")
    b9 = Button(
        master=SubViski,
        image = img9,
        borderwidth = 0,
        bg = "#DACE8E",
        activebackground='#DACE8E',
        highlightthickness = 0,
        command = viski1,
        relief = "flat")

    b9.place(
        x = 43, y = 113,
        width = 241,
        height = 80)

    img10 = PhotoImage(file = f"img10.png")
    b10 = Button(
        master=canvasViski,
        image = img10,
        borderwidth = 0,
        bg = "#DACE8E",
        activebackground='#DACE8E',
        highlightthickness = 0,
        command = viski2,
        relief = "flat")

    b10.place(
        x = 43, y = 231,
        width = 241,
        height = 80)

    img11 = PhotoImage(file = f"img11.png")
    b11 = Button(
        master=canvasViski,
        image = img11,
        borderwidth = 0,
        bg = "#DACE8E",
        activebackground='#DACE8E',
        highlightthickness = 0,
        command = viski3,
        relief = "flat")

    b11.place(
        x = 43, y = 349,
        width = 241,
        height = 80)

    SubViski.overrideredirect(True)
    SubViski.bind('<FocusOut>', lossfocus)
    SubViski.resizable(False, False)
    SubViski.mainloop()
def btn_clicked6():
    print("Button 6 Clicked")

    def raki1():
        print("+1 rakı")
        pouringScreen()
        SubRaki.destroy()
    def raki2():
        print("+2 rakı")
        pouringScreen()
        SubRaki.destroy()
    def raki3():
        print("+3 rakı")
        pouringScreen()
        SubRaki.destroy()
    def lossfocus(event):
        if event.widget is SubRaki:
            # check which widget getting the focus
            w = SubRaki.tk.call('focus')
        if not w:
            # not widget in this window
            SubRaki.destroy()    


    SubRaki = Toplevel()
    SubRaki.focus_set()

    SubRaki.geometry("328x480")
    SubRaki.configure(bg = "#DACE8E")
    canvasRaki = Canvas(
    SubRaki,
    bg = "#DACE8E",
    height = 480,
    width = 328,
    bd = 0,
    highlightthickness = 0,
    relief = "raised")
    canvasRaki.place(x = 0, y =0)

    
    
    Rakikapak = (Image.open('rakı.png'))
    new_image2 = ImageTk.PhotoImage(Rakikapak)
    canvasRaki.create_image(122,30, anchor=NW, image=new_image2)

    img9 = PhotoImage(file = f"img9.png")
    b9 = Button(
        master=SubRaki,
        image = img9,
        borderwidth = 0,
        bg = "#DACE8E",
        activebackground='#DACE8E',
        highlightthickness = 0,
        command = raki1,
        relief = "flat")

    b9.place(
        x = 43, y = 113,
        width = 241,
        height = 80)

    img10 = PhotoImage(file = f"img10.png")
    b10 = Button(
        master=canvasRaki,
        image = img10,
        borderwidth = 0,
        bg = "#DACE8E",
        activebackground='#DACE8E',
        highlightthickness = 0,
        command = raki2,
        relief = "flat")

    b10.place(
        x = 43, y = 231,
        width = 241,
        height = 80)

    img11 = PhotoImage(file = f"img11.png")
    b11 = Button(
        master=canvasRaki,
        image = img11,
        borderwidth = 0,
        bg = "#DACE8E",
        activebackground='#DACE8E',
        highlightthickness = 0,
        command = raki3,
        relief = "flat")

    b11.place(
        x = 43, y = 349,
        width = 241,
        height = 80)

    SubRaki.overrideredirect(True)
    SubRaki.bind('<FocusOut>', lossfocus)
    SubRaki.resizable(False, False)
    SubRaki.mainloop()
def btn_clicked7():
    print("Button 7 Clicked")

    def kanyak1():
        print("+1 kanyak")
        pouringScreen()
        SubKanyak.destroy()
    def kanyak2():
        print("+2 kanyak")
        pouringScreen()
        SubKanyak.destroy()
    def kanyak3():
        print("+3 kanyak")
        pouringScreen()
        SubKanyak.destroy()
    def lossfocus(event):
        if event.widget is SubKanyak:
            # check which widget getting the focus
            w = SubKanyak.tk.call('focus')
        if not w:
            # not widget in this window
            SubKanyak.destroy()    


    SubKanyak = Toplevel()
    SubKanyak.focus_set()

    SubKanyak.geometry("328x480")
    SubKanyak.configure(bg = "#DACE8E")
    canvasKanyak = Canvas(
    SubKanyak,
    bg = "#DACE8E",
    height = 480,
    width = 328,
    bd = 0,
    highlightthickness = 0,
    relief = "raised")
    canvasKanyak.place(x = 0, y =0)

    
    
    Kanyakkapak = (Image.open('konyak.png'))
    new_image2 = ImageTk.PhotoImage(Kanyakkapak)
    canvasKanyak.create_image(100,30, anchor=NW, image=new_image2)

    img9 = PhotoImage(file = f"img9.png")
    b9 = Button(
        master=SubKanyak,
        image = img9,
        borderwidth = 0,
        bg = "#DACE8E",
        activebackground='#DACE8E',
        highlightthickness = 0,
        command = kanyak1,
        relief = "flat")

    b9.place(
        x = 43, y = 113,
        width = 241,
        height = 80)

    img10 = PhotoImage(file = f"img10.png")
    b10 = Button(
        master=canvasKanyak,
        image = img10,
        borderwidth = 0,
        bg = "#DACE8E",
        activebackground='#DACE8E',
        highlightthickness = 0,
        command = kanyak2,
        relief = "flat")

    b10.place(
        x = 43, y = 231,
        width = 241,
        height = 80)

    img11 = PhotoImage(file = f"img11.png")
    b11 = Button(
        master=canvasKanyak,
        image = img11,
        borderwidth = 0,
        bg = "#DACE8E",
        activebackground='#DACE8E',
        highlightthickness = 0,
        command = kanyak3,
        relief = "flat")

    b11.place(
        x = 43, y = 349,
        width = 241,
        height = 80)

    SubKanyak.overrideredirect(True)
    SubKanyak.bind('<FocusOut>', lossfocus)
    SubKanyak.resizable(False, False)
    SubKanyak.mainloop()    
def btn_clicked8():
    print("Button 8 Clicked")

    def kanyak1():
        print("+1 votka")
        pouringScreen()
        SubVodka.destroy()
    def kanyak2():
        print("+2 votka")
        pouringScreen()
        SubVodka.destroy()
    def kanyak3():
        print("+3 votka")
        pouringScreen()
        SubVodka.destroy()
    def lossfocus(event):
        if event.widget is SubVodka:
            # check which widget getting the focus
            w = SubVodka.tk.call('focus')
        if not w:
            # not widget in this window
            SubVodka.destroy()    


    SubVodka = Toplevel()
    SubVodka.focus_set()

    SubVodka.geometry("328x480")
    SubVodka.configure(bg = "#DACE8E")
    canvasVodka = Canvas(
    SubVodka,
    bg = "#DACE8E",
    height = 480,
    width = 328,
    bd = 0,
    highlightthickness = 0,
    relief = "raised")
    canvasVodka.place(x = 0, y =0)

    
    
    Vodkakapak = (Image.open('vodka.png'))
    new_image2 = ImageTk.PhotoImage(Vodkakapak)
    canvasVodka.create_image(115,30, anchor=NW, image=new_image2)

    img9 = PhotoImage(file = f"img9.png")
    b9 = Button(
        master=SubVodka,
        image = img9,
        borderwidth = 0,
        bg = "#DACE8E",
        activebackground='#DACE8E',
        highlightthickness = 0,
        command = kanyak1,
        relief = "flat")

    b9.place(
        x = 43, y = 113,
        width = 241,
        height = 80)

    img10 = PhotoImage(file = f"img10.png")
    b10 = Button(
        master=canvasVodka,
        image = img10,
        borderwidth = 0,
        bg = "#DACE8E",
        activebackground='#DACE8E',
        highlightthickness = 0,
        command = kanyak2,
        relief = "flat")

    b10.place(
        x = 43, y = 231,
        width = 241,
        height = 80)

    img11 = PhotoImage(file = f"img11.png")
    b11 = Button(
        master=canvasVodka,
        image = img11,
        borderwidth = 0,
        bg = "#DACE8E",
        activebackground='#DACE8E',
        highlightthickness = 0,
        command = kanyak3,
        relief = "flat")

    b11.place(
        x = 43, y = 349,
        width = 241,
        height = 80)

    SubVodka.overrideredirect(True)
    SubVodka.bind('<FocusOut>', lossfocus)
    SubVodka.resizable(False, False)
    SubVodka.mainloop()

window = Tk()
w = Label(window, text=f"{dt.strftime('%H:%M:%S')}", fg="white", bg="black", font=("helvetica", 40))

window.geometry("800x480")
window.configure(bg = "#246371")
canvas = Canvas(
    window,
    bg = "#246371",
    height = 480,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    bg = "#246371",
    activebackground='#246371',
    highlightthickness = 0,
    command = btn_clicked1,
    relief = "flat")

b0.place(
    x = 30, y = 95,
    width = 170,
    height = 177)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    bg = "#246371",
    activebackground='#246371',
    highlightthickness = 0,
    command = btn_clicked2,
    relief = "flat")

b1.place(
    x = 220, y = 95,
    width = 170,
    height = 177)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    bg = "#246371",
    activebackground='#246371',
    highlightthickness = 0,
    command = btn_clicked3,
    relief = "flat")

b2.place(
    x = 410, y = 95,
    width = 170,
    height = 177)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    bg = "#246371",
    activebackground='#246371',
    highlightthickness = 0,
    command = btn_clicked4,
    relief = "flat")

b3.place(
    x = 600, y = 95,
    width = 170,
    height = 177)

img4 = ImageTk.PhotoImage(file = f"img4.png")
img4canvas = canvas.create_image(150, 150, image=img4)

b4 = Button(
    image = img4,
    borderwidth = 0,
    bg = "#246371",
    activebackground='#246371',
    highlightthickness = 0,
    command = btn_clicked5,
    relief = "flat")

b4.place(
    x = 75, y = 302,
    width = 80,
    height = 80)

img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    bg = "#246371",
    activebackground='#246371',
    highlightthickness = 0,
    command = btn_clicked6,
    relief = "flat")

b5.place(
    x = 265, y = 302,
    width = 80,
    height = 80)

img6 = PhotoImage(file = f"img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    bg = "#246371",
    activebackground='#246371',
    highlightthickness = 0,
    command = btn_clicked7,
    relief = "flat")

b6.place(
    x = 455, y = 302,
    width = 80,
    height = 80)

img7 = PhotoImage(file = f"img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    bg = "#246371",
    activebackground='#246371',
    highlightthickness = 0,
    command = btn_clicked8,
    relief = "flat")

b7.place(
    x = 645, y = 302,
    width = 80,
    height = 80)

imgSetting = PhotoImage(file = f"powerbutton.png")
bSet = Button(
    image = imgSetting,
    borderwidth = 0,
    bg = "#246371",
    activebackground='#246371',
    highlightthickness = 0,
    command = settingbutton,
    relief = "flat")

bSet.place(
    x = 730, y = 10,
    width = 50,
    height = 50)


img8= (Image.open("img8.png")) 
resized_image= img8.resize((90,55), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
canvas.create_image(10,10, anchor=NW, image=new_image)

window.resizable(False, False)
window.overrideredirect(True)
window.mainloop()
