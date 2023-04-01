import oracledb
from tkinter import *
from PIL import ImageTk,Image
import main
from addbook import *
from searchbook import *
from delbook import *
from updbook import *

con=oracledb.connect(user="C##Nitish",password="123",dsn="192.168.19.1/orcl")
cur=con.cursor()

def logged(ida,passwa):
    window=Tk()
    window.title("Book Store Management System")
    window.maxsize(height="500",width="600")
    window.minsize(height="500",width="600")


    canvas=Canvas(window,height=500,width=600)
    canvas.place(relheight=1,relwidth=1,relx=0,rely=0)

    fr=Frame(window,bg="#ffd700",bd=8)
    fr.place(relheight=0.2,relwidth=0.6,relx=0.35,rely=0.03)

    canvas.create_rectangle(0,0,170,500,fill="#000000")

    wel=Label(fr,bg="black",fg="white",text="Welcome to \nBook Store Management System",font=("times",16))
    wel.place(relheight=1,relwidth=1,relx=0,rely=0)

    cur.execute("select avatar from user_creds where id=:1",(ida,))
    ai=cur.fetchone()
    ai=int(ai[0])-1
    avt=Image.open(main.avatarl[ai]).resize((100,100),Image.LANCZOS)
    avt=ImageTk.PhotoImage(avt,master=canvas)
    canvas.create_image(35,35,image=avt,anchor=NW)

    window.mainloop()
