import oracledb
from tkinter import *
from tkinter import ttk,messagebox
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
    canvas.create_rectangle(0,0,1400,100,fill="#000000")
    
    canvas.create_text(200,50,text="Hey, "+ida,font=("Arial",20),fill="#FFFFFF")

    avt=ImageTk.PhotoImage(avt,master=canvas)
    canvas.create_image(40,15,image=avt,anchor=NW)

    date = Label(window, text="DATE: " +datetime.now().strftime("%d-%h-%Y"),font=("arial",10),fg="#000000",bg="#FFFFFF")
    time = Label(window, text="TIME: "+datetime.now().strftime("%I:%M:%S %p"),font=("arial",10),fg="#000000",bg="#FFFFFF")
    date.place(relx=0.8, rely=0.035)
    time.place(relx=0.8, rely=0.087)

    def update_time():
        time.config(text="TIME: "+datetime.now().strftime("%I:%M:%S %p"))
        window.update()
        window.after(1000, update_time)

    data=ttk.Treeview(window,columns=("Id","Title","Author","Genre","Stock","Price"))
    data.configure(selectmode="browse")
    scroll=ttk.Scrollbar(window,orient="vertical",command=data.yview)
    scroll.place(relheight=0.6,relx=0.505,rely=0.2)
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
    data.place(relx=0.01,rely=0.2,relheight=0.6)

    count=0
    cur.execute("select * from books")
    books=cur.fetchall()
    for i in books:
        data.insert(parent="",index="end",iid=i[0],values=i,tags=('even' if count%2==0 else 'odd',))
        count+=1

    global cart_count,cart_amount
    cart_count=0
    cart_amount=0.0
    cart_label=Label(window,text=f"CART ITEMS : [ {cart_count} ]",bg="#808080",fg="#FFFFFF")
    cart_label.place(relx=0.68,rely=0.17,relwidth=0.3085)

    cart_amt=Label(window,text=f"CART TOTAL : [ {cart_amount} ]",bg="#808080",fg="#FFFFFF")
    cart_amt.place(relx=0.68,rely=0.8,relwidth=0.3085)

    label3=Label(window, text="Book Id")
    label3.place(relx=0.57,rely=0.39)
    label5 = Label(window, text="")
    label5.place(relx=0.58,rely=0.42)
    label4 = Label(window, text="Quantity*")
    label4.place(relx=0.57,rely=0.5)
    entry1 = Entry(window)
    entry1.place(relx=0.55,rely=0.55)
    def add_to_cart():
        global cart_count,curItem,cart_amount
        curItem=data.focus()
        if entry1.get()=="0":
            messagebox.showerror("Error","Quantity cannot be 0")
            return
        if entry1.get()!="":
            if int(entry1.get())>int(data.item(curItem)['values'][4]):
                messagebox.showerror("Error","Not enough stock")
            else:
                for ch in cart.get_children():
                    if cart.item(ch)["values"][0] == data.item(curItem)['values'][0]:
                        prev_amt=cart.item(ch)["values"][4]
                        cart.delete(ch)
                        cart.insert(parent="",index="end",iid=data.item(curItem)['values'][0],values=(data.item(curItem)['values'][0],data.item(curItem)['values'][1],
                        data.item(curItem)['values'][5],entry1.get(),float("{:.2f}".format(float(data.item(curItem)['values'][5])*int(entry1.get())))))
                        cart_amount=cart_amount-float(prev_amt)+float("{:.2f}".format(float(data.item(curItem)['values'][5])*int(entry1.get())))
                        cart_amount=float("{:.2f}".format(cart_amount))
                        cart_amt.config(text=f"CART TOTAL : [ {cart_amount} ]")
                        return
                cart.insert(parent="",index="end",iid=data.item(curItem)['values'][0],values=(data.item(curItem)['values'][0],data.item(curItem)['values'][1],
                data.item(curItem)['values'][5],entry1.get(),float("{:.2f}".format(float(data.item(curItem)['values'][5])*int(entry1.get())))))
                cart_count+=1
                cart_amount+=float("{:.2f}".format(float(data.item(curItem)['values'][5])*int(entry1.get())))
                cart_amount=float("{:.2f}".format(cart_amount))
                cart_amt.config(text=f"CART TOTAL : [ {cart_amount} ]")
                cart_label.config(text=f"CART ITEMS : [ {cart_count} ]")
    butt1=Button(window,text="Add to Cart ->",command=add_to_cart)
    butt1.place(relx=0.56,rely=0.6)
    def update_info(event):
        curItem=data.focus()
        label5.config(text=data.item(curItem)['values'][0])
        entry1.delete(0,END)
        entry1.insert(0,"1")
    
    data.bind("<<TreeviewSelect>>",update_info)
    logout=Image.open("./media/logout.png").resize((45,45),Image.LANCZOS)
    logout=ImageTk.PhotoImage(logout,master=canvas)
    logout_but=canvas.create_image(1300,32,image=logout,anchor=NW)
    def logout_method(event):
        window.destroy()
        main.login()
    canvas.tag_bind(logout_but,"<Button-1>",logout_method)
    canvas.tag_bind(logout_but,"<Enter>",lambda event:canvas.configure(cursor="hand2"))
    canvas.tag_bind(logout_but,"<Leave>",lambda event:canvas.configure(cursor=""))

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
    cart.place(relx=0.68,rely=0.2,relheight=0.6)


    update_time()

    cart_img=Image.open("./media/cart.png").resize((70,70),Image.LANCZOS)
    cart_img=ImageTk.PhotoImage(cart_img,master=canvas)
    cart_but=canvas.create_image(1300,600,image=cart_img,anchor=NW)
    def cart_window():
        cart_window=Toplevel(window)
        cart_window.geometry("400x400")
        cart_window.resizable(False,False)
        cart_window.title("Bill")
        cart_window.configure(bg="#808080")
        cart_window.grab_set()
        cart_window.focus_set()
        cart_window.transient(window)
        cart_window.protocol("WM_DELETE_WINDOW",lambda:cart_window.destroy())
        cart_window.mainloop()
    canvas.tag_bind(cart_but,"<Button-1>",lambda event:cart_window())
    canvas.tag_bind(cart_but,"<Enter>",lambda event:canvas.configure(cursor="hand2"))
    canvas.tag_bind(cart_but,"<Leave>",lambda event:canvas.configure(cursor=""))

    def del_cart():
        global cart_count,cart_amount
        curItem=cart.focus()
        cart_amount-=float(cart.item(curItem)['values'][4])
        cart_amount=float("{:.2f}".format(cart_amount))
        cart_amt.config(text=f"CART TOTAL : [ {cart_amount} ]")
        cart_count-=1
        cart_label.config(text=f"CART ITEMS : [ {cart_count} ]")
        cart.delete(curItem)
    remo_but=Button(window,text="Remove",command=del_cart)
    remo_but.place(relx=0.82,rely=0.9)

    def cle_cart():
        global cart_count,cart_amount
        cart_amount=0.0
        cart_count=0
        cart_label.config(text=f"CART ITEMS : [ {cart_count} ]")
        cart_amt.config(text=f"CART TOTAL : [ {cart_amount} ]")
        cart.delete(*cart.get_children())
    clear=Button(window,text="Clear Cart",command=cle_cart)
    clear.place(relx=0.72,rely=0.9)







    window.mainloop()