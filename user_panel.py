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

    date = Label(window, text="DATE: " +datetime.now().strftime("%d-%h-%Y"),font=("arial",12))
    time = Label(window, text="TIME: "+datetime.now().strftime("%I:%M:%S %p"),font=("arial",12))
    date.place(relx=0.8, rely=0.048)
    time.place(relx=0.8, rely=0.1)

    def update_time():
        time.config(text="TIME: "+datetime.now().strftime("%I:%M:%S %p"))
        window.update()
        window.after(1000, update_time)

    data=ttk.Treeview(window,columns=("Id","Title","Author","Genre","Stock","Price"))
    data.configure(selectmode="browse")
    scroll=ttk.Scrollbar(window,orient="vertical",command=data.yview)
    scroll.place(relheight=0.6,relx=0.545,rely=0.2)
    data.tag_configure('odd',background="lightblue")
    data.tag_configure('even',background="#ffffff")
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
    data.place(relx=0.05,rely=0.2,relheight=0.6)

    count=0
    cur.execute("select * from books")
    books=cur.fetchall()
    for i in books:
        data.insert(parent="",index="end",iid=i[0],values=i,tags=('even' if count%2==0 else 'odd',))
        count+=1

    cart_count=0
    cart_label=Label(window,text=f"CART TOTAL:[{cart_count}]",bg="#808080",fg="#FFFFFF")
    cart_label.place(relx=0.75,rely=0.15)
    label=Label(window, text="Book Id")
    label.place(relx=0.6,rely=0.15)
    label = Label(window, text=f"h")
    label = Label(window, text="Quantity")
    label.place(relx=0.75,rely=0.2)

    logout=Image.open("./media/logout.png").resize((40,40),Image.LANCZOS)
    logout=ImageTk.PhotoImage(logout,master=window)
    label1=Label(window,image=logout)
    label1.place(relx=0.95,y=25)
    def logout_method(event):
        window.destroy()
        main.login()
    label1.bind("<Button-1>",logout_method)
    def on_enter(event):
        window.configure(cursor="hand2")
    def on_leave(event):
        window.configure(cursor="")
    label1.bind("<Enter>",on_enter)
    label1.bind("<Leave>",on_leave)
    
    cart=ttk.Treeview(window,columns=("Id","Name","Price","Quantity","Amount"),selectmode="browse")
    cart.column("#0",width=0,stretch=NO)
    cart.column("Id",width=50,anchor='center')
    cart.column("Name",width=200,anchor='center')
    cart.column("Price",width=60,anchor='center')
    cart.column("Quantity",width=60,anchor='center')
    cart.column("Amount",width=60,anchor='center')
    cart.heading("#0",text="")
    cart.heading("Id",text="Id")
    cart.heading("Name",text="Name")
    cart.heading("Price",text="Price")
    cart.heading("Quantity",text="Quantity")
    cart.heading("Amount",text="Amount")
    cart.place(relx=0.6,rely=0.2,relheight=0.6)


    update_time()
    window.mainloop()