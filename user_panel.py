import oracledb
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import main
from datetime import datetime

con=oracledb.connect(user="C##Nitish",password="123",dsn="192.168.19.1/orcl")
cur=con.cursor()

def logged(ida,passwa):
    window=Tk()
    window.title("Book Store Management System")
    window.maxsize(height="700",width="1400")
    window.minsize(height="700",width="1400")


    canvas=Canvas(window,height=500,width=600)
    canvas.place(relheight=1,relwidth=1,relx=0,rely=0)

    cur.execute("select avatar from user_creds where id=:1",(ida,))
    ai=cur.fetchone()
    ai=int(ai[0])-1
    avt=Image.open(main.avatarl[ai]).resize((80,80),Image.LANCZOS)

    greet=Label(window,text="Hey, "+ida,font=("Arial",20))
    greet.place(relx=0.1,rely=0.048)

    avt=ImageTk.PhotoImage(avt,master=canvas)
    canvas.create_image(40,15,image=avt,anchor=NW)

    date = Label(window, text="DATE: " +datetime.now().strftime("%d-%m-%Y"),font=("arial",12))
    time = Label(window, text="TIME: "+datetime.now().strftime("%I:%M:%S %p"),font=("arial",12))
    date.place(relx=0.8, rely=0.048)
    time.place(relx=0.8, rely=0.1)

    def update_time():
        time.config(text="TIME: "+datetime.now().strftime("%I:%M:%S %p"))
        window.update()
        window.after(1000, update_time)

    data=ttk.Treeview(window,columns=("Id","Title","Author","Genre","Stock","Price"),height=10)
    data.configure(selectmode="browse")
    scroll=ttk.Scrollbar(window,orient="vertical",command=data.yview)
    data.tag_configure('odd',background="lightblue")
    data.tag_configure('even',background="#ffffff")
    scroll.place(relheight=0.38,relx=0.98,rely=0.15)
    data.configure(yscrollcommand=scroll.set)
    data.column("#0",width=0,stretch=NO)
    data.column("Id",width=50,anchor='center')
    data.column("Title",width=200,anchor='center')
    data.column("Author",width=200,anchor='center')
    data.column("Genre",width=120,anchor='center')
    data.column("Stock",width=60,anchor='center')
    data.column("Price",width=60,anchor='center')
    data.heading("#0",text="")
    data.heading("Id",text="Id")
    data.heading("Title",text="Title")
    data.heading("Author",text="Author")
    data.heading("Genre",text="Genre")
    data.heading("Stock",text="Stock")
    data.heading("Price",text="Price")
    data.place(relwidth=0.8,relx=0.18,rely=0.2)

    count=0
    cur.execute("select * from books")
    books=cur.fetchall()
    for i in books:
        data.insert(parent="",index="end",iid=i[0],values=i,tags=('even' if count%2==0 else 'odd',))
        count+=1

    update_time()

    window.mainloop()