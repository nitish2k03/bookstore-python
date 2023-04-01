from tkinter import *
import oracledb
from PIL import ImageTk,Image

def addbook():
    window=Tk()
    window.title("Add Book Details")
    window.minsize(height="400",width="600")
    bg=Image.open("bg.jpg")
    bg=ImageTk.PhotoImage(bg)
    canvas=Canvas(window)
    canvas.create_image(0,0,image=bg,anchor=NW)
    canvas.place(relheight=1,relwidth=1,relx=0,rely=0)
    window.mainloop()



