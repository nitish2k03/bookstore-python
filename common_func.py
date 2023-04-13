import time
start=time.time()
import oracledb
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox,ttk
import oracledb
from datetime import datetime
import os

print(time.time()-start)
con=oracledb.connect(user="c##nitish",password="123",dsn="Nitish/orcl")
print("Successfully connected to Oracle Database")
cur=con.cursor()
print(time.time()-start)

def adm_panel(ida,passwa):
    window3=Tk()
    window3.iconbitmap("./media/favicon.ico")
    window3.title("Book Store Management System")
    window3.maxsize(height="600",width="1200")
    window3.minsize(height="600",width="1200")
    canvas3=Canvas(window3,height=600,width=1200)
    canvas3.place(relheight=1,relwidth=1,relx=0,rely=0)
    canvas3.create_rectangle(0,0,200,600,fill="#000000")
    canvas3.create_text(20,15,text="Admin Panel",fill="#333fff",font=("kanit",20),anchor=NW)
    canvas3.create_text(30,230,text="Welcome Back",fill="#333fff",font=("kanit",16),anchor=NW)
    canvas3.create_text(60,270,text=ida,fill="#333fff",font=("kanit",16),anchor=NW)
    cur.execute("select avatar from user_creds where id=:1",(ida,))
    ai=cur.fetchone()
    ai=int(ai[0])-1
    avt=Image.open(avatarl[ai]).resize((100,100),Image.LANCZOS)
    avt=ImageTk.PhotoImage(avt,master=canvas3)
    canvas3.create_image(50,85,image=avt,anchor=NW)
    cur.execute("select * from books")
    books=cur.fetchall()
    def on_enter(event):
        canvas3.configure(cursor="hand2")

    def on_leave(event):
        canvas3.configure(cursor="")

    
    users_s=Image.open("./media/users_sel.png").resize((150,35),Image.LANCZOS)
    users_s=ImageTk.PhotoImage(users_s,master=canvas3)

    users_u=Image.open("./media/users_unsel.png").resize((150,35),Image.LANCZOS)
    users_u=ImageTk.PhotoImage(users_u,master=canvas3)

    trans_s=Image.open("./media/transactions_sel.png").resize((150,35),Image.LANCZOS)
    trans_s=ImageTk.PhotoImage(trans_s,master=canvas3)

    trans_u=Image.open("./media/transactions_unsel.png").resize((150,35),Image.LANCZOS)
    trans_u=ImageTk.PhotoImage(trans_u,master=canvas3)

    books_s=Image.open("./media/books_sel.png").resize((150,35),Image.LANCZOS)
    books_s=ImageTk.PhotoImage(books_s,master=canvas3)

    books_u=Image.open("./media/books_unsel.png").resize((150,35),Image.LANCZOS)
    books_u=ImageTk.PhotoImage(books_u,master=canvas3)


    logout=Image.open("./media/logout.png").resize((35,35),Image.LANCZOS)
    logout=ImageTk.PhotoImage(logout,master=canvas3)
    logout_but=canvas3.create_image(1135,15,image=logout,anchor=NW)



    def logout_method(event):
        window3.destroy()
        login()
    canvas3.tag_bind(logout_but,"<Button-1>",logout_method)
    canvas3.tag_bind(logout_but,"<Enter>",on_enter)
    canvas3.tag_bind(logout_but,"<Leave>",on_leave)
    

    def books_unchange(event):
        canvas3.itemconfig(but1,image=books_u)
        canvas3.tag_bind(but1,"<Button-1>",books_change)
        data.destroy()

    def books_change(event):
        canvas3.itemconfig(but1,image=books_s)
        canvas3.tag_bind(but1,"<Button-1>",books_unchange)
        if data:
            data.destroy()
            canvas3.itemconfig(but2,image=users_u)  
            canvas3.tag_bind(but2,"<Button-1>",users_change)
            canvas3.itemconfig(but3,image=trans_u)  
            canvas3.tag_bind(but3,"<Button-1>",trans_change)
        books_show(event)
        selection2.place_forget()
        records_frame.place_forget()
        user_frame.place_forget()

    def users_unchange(event):
        canvas3.itemconfig(but2,image=users_u)
        canvas3.tag_bind(but2,"<Button-1>",users_change)
        data.destroy()
    def users_change(event):
        canvas3.itemconfig(but2,image=users_s)
        canvas3.tag_bind(but2,"<Button-1>",users_unchange)
        if data:
            data.destroy()
            canvas3.itemconfig(but1,image=books_u)
            canvas3.tag_bind(but1,"<Button-1>",books_change)
            canvas3.itemconfig(but3,image=trans_u)
            canvas3.tag_bind(but3,"<Button-1>",trans_change)
        search_box.place_forget()
        record_frame.place_forget()
        book_frame.place_forget()
        selection1.place_forget()
        users_show(event)

    def trans_unchange(event):
        canvas3.itemconfig(but3,image=trans_u)
        canvas3.tag_bind(but3,"<Button-1>",trans_change)
        data.destroy()

    def trans_change(event):
        canvas3.itemconfig(but3,image=trans_s)
        canvas3.tag_bind(but3,"<Button-1>",trans_unchange)
        if data:
            data.destroy()
            canvas3.itemconfig(but1,image=books_u)
            canvas3.tag_bind(but1,"<Button-1>",books_change)
            canvas3.itemconfig(but2,image=users_u)
            canvas3.tag_bind(but2,"<Button-1>",users_change)
        trans_show(event)



    but1=canvas3.create_image(30,400,image=books_u,anchor=NW)
    canvas3.tag_bind(but1,"<Button-1>",books_change)
    canvas3.tag_bind(but1,"<Enter>",on_enter)
    canvas3.tag_bind(but1,"<Leave>",on_leave)
    
    but2=canvas3.create_image(30,450,image=users_u,anchor=NW)
    canvas3.tag_bind(but2,"<Button-1>",users_change)
    canvas3.tag_bind(but2,"<Enter>",on_enter)
    canvas3.tag_bind(but2,"<Leave>",on_leave)

    but3=canvas3.create_image(30,500,image=trans_u,anchor=NW)
    canvas3.tag_bind(but3,"<Button-1>",trans_change)
    canvas3.tag_bind(but3,"<Enter>",on_enter)
    canvas3.tag_bind(but3,"<Leave>",on_leave)


    search_box=Entry(canvas3)
    search_box.place(relheight=0.05,relwidth=0.4,relx=0.2,rely=0.03)
    search_box.insert(0,"Search Here by Book Title")
    def search_box_click(event):
        search_box.delete(0,END)
        search_box.unbind("<Button-1>")
    search_box.bind("<Button-1>",search_box_click)
    def upd_data(event):
        data.delete(*data.get_children())
        val=search_box.get()
        cur.execute("SELECT * FROM books WHERE lower(title) LIKE '%"+val+"%'")
        if len(search_box.get())>0:
            count=0
            for row in cur.fetchall():
                    data.insert(parent='',index='end',iid=row[0],values=row,tags=('even' if count%2==0 else 'odd',))
                    count+=1

        if len(search_box.get())==0:
                        data.delete(*data.get_children())
                        cur.execute("SELECT * FROM books")
                        count=0
                        for row in cur.fetchall():
                            data.insert(parent='',index='end',iid=row[0],values=row,tags=('even' if count%2==0 else 'odd',))
                            count+=1
                    

    search_box.bind("<KeyRelease>",upd_data)

    def books_show(event):
        canvas3.itemconfig(but1,image=books_s)
        search_box.place(relheight=0.05,relwidth=0.4,relx=0.2,rely=0.03)
        global data
        style=ttk.Style()
        # style.theme_use('default')
        style.configure("Treeview",background="black",foreground="white",rowheight=25,fieldbackground="#ffffff")
        data=ttk.Treeview(canvas3,columns=("Id","Title","Author","Genre","Stock","Price"),height=10)
        data.configure(selectmode="browse")
        scroll=ttk.Scrollbar(canvas3,orient="vertical",command=data.yview)
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
        data.place(relwidth=0.8,relx=0.18,rely=0.15)

        count=0
        for i in books:
            data.insert(parent="",index="end",iid=i[0],values=i,tags=('even' if count%2==0 else 'odd',))
            count+=1

        global record_frame,book_frame
        record_frame=LabelFrame(canvas3,text="Record")
        record_frame.place(relheight=0.2,relwidth=0.8,relx=0.18,rely=0.6)
        id_label=Label(record_frame,text="Id")
        id_label.place(relheight=0.3,relx=0.02,rely=0.1)
        id_entry=Entry(record_frame)
        id_entry.place(relheight=0.25,relwidth=0.2,relx=0.06,rely=0.1)
        title_label=Label(record_frame,text="Title")
        title_label.place(relheight=0.3,relx=0.02,rely=0.5)
        title_entry=Entry(record_frame)
        title_entry.place(relheight=0.25,relwidth=0.2,relx=0.06,rely=0.5)
        author_label=Label(record_frame,text="Author")
        author_label.place(relheight=0.3,relx=0.33,rely=0.1)
        author_entry=Entry(record_frame)
        author_entry.place(relheight=0.25,relwidth=0.2,relx=0.4,rely=0.1)
        genre_label=Label(record_frame,text="Genre")
        genre_label.place(relheight=0.3,relx=0.33,rely=0.5)
        genre_entry=Entry(record_frame)
        genre_entry.place(relheight=0.25,relwidth=0.2,relx=0.4,rely=0.5)
        stock_label=Label(record_frame,text="Stock")
        stock_label.place(relheight=0.3,relx=0.72,rely=0.1)
        stock_entry=Entry(record_frame)
        stock_entry.place(relheight=0.25,relwidth=0.2,relx=0.78,rely=0.1)
        price_label=Label(record_frame,text="Price")
        price_label.place(relheight=0.3,relx=0.72,rely=0.5)
        price_entry=Entry(record_frame)
        price_entry.place(relheight=0.25,relwidth=0.2,relx=0.78,rely=0.5)

        book_frame=LabelFrame(canvas3,text="Commands")
        book_frame.place(relheight=0.1,relwidth=0.8,relx=0.18,rely=0.85)
        global selection1
        def sel():
            cle()
            curItem=data.focus()
            id_entry.insert(0,data.item(curItem)['values'][0])
            title_entry.insert(0,data.item(curItem)['values'][1])
            author_entry.insert(0,data.item(curItem)['values'][2])
            genre_entry.insert(0,data.item(curItem)['values'][3])
            stock_entry.insert(0,data.item(curItem)['values'][4])
            price_entry.insert(0,data.item(curItem)['values'][5])

        selection1=Button(canvas3,text="Fetch Record",command=sel)
        selection1.place(relheight=0.05,relwidth=0.1,relx=0.5,rely=0.54)

        def cle():
            id_entry.delete(0,END)
            title_entry.delete(0,END)
            author_entry.delete(0,END)
            genre_entry.delete(0,END)
            stock_entry.delete(0,END)
            price_entry.delete(0,END)

        def upd_tree(event):
            data.delete(*data.get_children())
            cur.execute("SELECT * FROM books")
            count=0
            for row in cur.fetchall():
                data.insert(parent='',index='end',iid=row[0],values=row,tags=('even' if count%2==0 else 'odd',))
                count+=1

        def add_book():
            if(len(id_entry.get())==0 or len(title_entry.get())==0  or len(author_entry.get())==0 or len(genre_entry.get())==0 or len(stock_entry.get())==0 or len(price_entry.get())==0):
                messagebox.showerror("Error","All Fields Are Required")
                return
            try:
                cur.execute("INSERT INTO books VALUES(:1,:2,:3,:4,:5,:6)",(id_entry.get(),title_entry.get(),author_entry.get(),genre_entry.get(),stock_entry.get(),price_entry.get()))
                con.commit()
                messagebox.showinfo("Success","Book Added Successfully")
                cle()
            except:
                messagebox.showerror("Error","Book Already Exists")
            upd_tree(event)

        def del_book():
            if(len(id_entry.get())==0):
                messagebox.showerror("Error","ID Field is Required")
                return
            if(id_entry.get not in data.get_children()):
                messagebox.showerror("Error","Book Doesn't Exist")
                return
            try:
                cur.execute("DELETE FROM books WHERE b_id=:1",(id_entry.get(),))
                con.commit()
                messagebox.showinfo("Success","Book Deleted Successfully")
            except:
                messagebox.showerror("Error","Book Doesn't Exist")
            cle()
            upd_tree(event)

        def upd_book():
            if(len(id_entry.get())==0):
                messagebox.showerror("Error","All Fields Are Required")
                return
            try:
                cur.execute("UPDATE books SET title=:1,author=:2,genre=:3,stock=:4,price=:5 WHERE b_id=:6",(title_entry.get(),author_entry.get(),genre_entry.get(),stock_entry.get(),price_entry.get(),id_entry.get()))
                con.commit()
                messagebox.showinfo("Success","Book Updated Successfully")
            except:
                messagebox.showerror("Error","Book Doesn't Exist")
            cle()
            upd_tree(event)

        def all_del():
            response=messagebox.askquestion("Confirm","All Books Will Be Deleted. Are You Sure?")
            if(response=="yes"):
                cur.execute("DELETE FROM books")
                con.commit()
                messagebox.showinfo("Success","All Books Deleted Successfully")
            upd_tree(event)

        add_button=Button(book_frame,text="Add Book",command=add_book)
        add_button.place(relheight=0.6,relwidth=0.1,relx=0.04,rely=0.1)
        del_button=Button(book_frame,text="Delete Book",command=del_book)
        del_button.place(relheight=0.6,relwidth=0.1,relx=0.41,rely=0.1)
        upd_button=Button(book_frame,text="Update Book",command=upd_book)
        upd_button.place(relheight=0.6,relwidth=0.1,relx=0.21,rely=0.1)
        remo_button=Button(book_frame,text="Remove All Records",command=all_del)
        remo_button.place(relheight=0.6,relwidth=0.15,relx=0.60,rely=0.1)
        cle_button=Button(book_frame,text="Clear All Fields",command=cle)
        cle_button.place(relheight=0.6,relwidth=0.15,relx=0.82,rely=0.1)
        

    books_show(None)
    print("success")

    def users_show(event):
        canvas3.itemconfig(but2,image=users_s)
        cur.execute("select * from user_creds")
        users=cur.fetchall()
        global data
        data=ttk.Treeview(canvas3,height=10)
        global count
        count=0
        data.tag_configure('odd',background="lightblue")
        data.tag_configure('even',background="#ffffff")
        data["columns"]=("Id","Pass","Avatar","Role")
        data.column("#0",width=0,stretch=NO)
        data.column("Id",width=50,anchor='center')
        data.column("Pass",width=200,anchor='center')
        data.column("Avatar",width=60,anchor='center')
        data.column("Role",width=40,anchor='center')
        data.heading("#0",text="")
        data.heading("Id",text="Id")
        data.heading("Pass",text="Password")
        data.heading("Avatar",text="Avatar")
        data.heading("Role",text="Role")
        data.place(relwidth=0.8,relx=0.18,rely=0.15)
        count=0
        for i in users:
            data.insert(parent="",index="end",iid=i[0],values=i,tags=('even' if count%2==0 else 'odd',))
            count+=1
        global records_frame,user_frame
        records_frame=LabelFrame(canvas3,text="Records")
        records_frame.place(relheight=0.2,relwidth=0.8,relx=0.18,rely=0.6)
        id_label=Label(records_frame,text="Id")
        id_label.place(relheight=0.3,relx=0.2,rely=0.1)
        id_entry=Entry(records_frame)
        id_entry.place(relheight=0.25,relwidth=0.2,relx=0.25,rely=0.1)
        pass_label=Label(records_frame,text="Password")
        pass_label.place(relheight=0.3,relx=0.18,rely=0.5)
        pass_entry=Entry(records_frame)
        pass_entry.place(relheight=0.25,relwidth=0.2,relx=0.25,rely=0.5)
        avatar_label=Label(records_frame,text="Avatar")
        avatar_label.place(relheight=0.3,relx=0.55,rely=0.1)
        avatar_entry=Entry(records_frame)
        avatar_entry.place(relheight=0.25,relwidth=0.2,relx=0.60,rely=0.1)
        role_label=Label(records_frame,text="Role")
        role_label.place(relheight=0.3,relx=0.55,rely=0.5)
        role_entry=Entry(records_frame)
        role_entry.place(relheight=0.25,relwidth=0.2,relx=0.60,rely=0.5)
    
        user_frame=LabelFrame(canvas3,text="Commands")
        user_frame.place(relheight=0.1,relwidth=0.8,relx=0.18,rely=0.85)
        global selection2
        def sel2():
            clea()
            curItem=data.focus()
            id_entry.delete(0,END)
            pass_entry.delete(0,END)
            avatar_entry.delete(0,END)
            role_entry.delete(0,END)
            id_entry.insert(0,data.item(curItem)['values'][0])
            pass_entry.insert(0,data.item(curItem)['values'][1])
            avatar_entry.insert(0,data.item(curItem)['values'][2])
            role_entry.insert(0,data.item(curItem)['values'][3])
        
        def clea():
            id_entry.delete(0,END)
            pass_entry.delete(0,END)
            avatar_entry.delete(0,END)
            role_entry.delete(0,END)

        selection2=Button(canvas3,text="Fetch Record",command=sel2)
        selection2.place(relheight=0.05,relwidth=0.1,relx=0.5,rely=0.54)

        def upd_tree():
            data.delete(*data.get_children())
            cur.execute("select * from user_creds")
            bot=cur.fetchall()
            count=0
            for i in bot:
                data.insert(parent="",index="end",iid=i[0],values=i,tags=('even' if count%2==0 else 'odd',))
                count+=1

        def add_user():
            if(id_entry.get()=="" or pass_entry.get()=="" or avatar_entry.get()=="" or role_entry.get()==""):
                messagebox.showerror("Error","Please Fill All Fields")
                return
            if avatar_entry.get() not in ("1","2","3","4","5","6","7","8"):
                messagebox.showerror("Error","Avatar Must Be Between 1-8")
                return
            if role_entry.get() not in ("user","admin"):
                messagebox.showerror("Error","Role Must Be Either user or admin")
                return
            try:
                cur.execute("INSERT INTO user_creds VALUES(:1,:2,:3,:4)",(id_entry.get(),pass_entry.get(),avatar_entry.get(),role_entry.get()))
                con.commit()
                messagebox.showinfo("Success","User Added Successfully")
            except:
                messagebox.showerror("Error","User Already Exists")
            clea()
            upd_tree()
        def upd_user():
            if(id_entry.get()=="" or pass_entry.get()=="" or avatar_entry.get()=="" or role_entry.get()==""):
                messagebox.showerror("Error","Please Fill All Fields")
                return
            if avatar_entry.get() not in ("1","2","3","4","5","6","7","8"):
                messagebox.showerror("Error","Avatar Must Be Between 1-8")
                return
            if role_entry.get() not in ("user","admin"):
                messagebox.showerror("Error","Role Must Be Either user or admin")
                return
            try:
                cur.execute("UPDATE user_creds SET pass=:1,avatar=:2,role=:3 WHERE id=:4",(pass_entry.get(),avatar_entry.get(),role_entry.get(),id_entry.get()))
                con.commit()
                messagebox.showinfo("Success","User Updated Successfully")
            except:
                messagebox.showerror("Error","User Does Not Exist")
            clea()
            upd_tree()
        def del_user():
            if(id_entry.get()==""):
                messagebox.showerror("Error","Please Fill Id Field")
                return
            try:
                cur.execute("DELETE FROM user_creds WHERE id=:1",(id_entry.get(),))
                con.commit()
                messagebox.showinfo("Success","User Deleted Successfully")
            except:
                messagebox.showerror("Error","User Does Not Exist")
            upd_tree()
            clea()

        b1=Button(user_frame,text="Add User",command=add_user)
        b1.place(relheight=0.6,relwidth=0.1,relx=0.04,rely=0.1)
        b2=Button(user_frame,text="Update User",command=upd_user)
        b2.place(relheight=0.6,relwidth=0.1,relx=0.32,rely=0.1)
        b3=Button(user_frame,text="Delete User",command=del_user)
        b3.place(relheight=0.6,relwidth=0.1,relx=0.58,rely=0.1)
        b4=Button(user_frame,text="Clear All Fields",command=clea)
        b4.place(relheight=0.6,relwidth=0.15,relx=0.82,rely=0.1)

    def trans_show(event):
        canvas3.itemconfigure(but3,image=trans_s) 
        global data
        data=ttk.Treeview(canvas3,columns=("inv_id","name","user","path","date"),show="headings")
        data.tag_configure('odd',background="white")
        data.tag_configure('even',background="lightblue")
        data.column("inv_id",width=40,anchor="center")
        data.column("name",anchor="center")
        data.column("user",anchor="center")
        data.column("path",anchor="center")
        data.column("date",anchor="center")
        data.heading("inv_id",text="Invoice Id")
        data.heading("name",text="Customer Name")
        data.heading("user",text="Billing Clerk")
        data.heading("path",text="Invoice Path")
        data.heading("date",text="Date Created")
        data.place(relheight=0.4,relwidth=0.8,relx=0.18,rely=0.1)
        cur.execute("select * from transactions")
        bot=cur.fetchall()
        count=0
        for i in bot:
            data.insert(parent="",index="end",iid=i[0],values=i,tags=('even' if count%2==0 else 'odd',))
            count+=1
        

    window3.mainloop()
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
    avt=Image.open(avatarl[ai]).resize((80,80),Image.LANCZOS)
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

    global cart_count,cart_amount,cart
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
        login()
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
    canvas.tag_bind(cart_but,"<Button-1>",lambda event:cart_window())
    canvas.tag_bind(cart_but,"<Enter>",lambda event:canvas.configure(cursor="hand2"))
    canvas.tag_bind(cart_but,"<Leave>",lambda event:canvas.configure(cursor=""))
    def cart_window():
        if(cart_count==0):
            messagebox.showerror("Error","Cart is empty")
            return
        root=Toplevel(window)
        root.title("Customer Details")
        root.geometry("400x400")
        root.resizable(0,0)
        lbl1=Label(root,text="Customer Details")
        lbl1.place(relx=0.5,rely=0.1,anchor=CENTER)
        lbl2=Label(root,text="Name")
        lbl2.place(relx=0.2,rely=0.2,anchor=CENTER)
        lbl3=Label(root,text="Contact No")
        lbl3.place(relx=0.2,rely=0.3,anchor=CENTER)
        inp1=Entry(root)
        inp1.place(relx=0.5,rely=0.2,anchor=CENTER)
        inp2=Entry(root)
        inp2.place(relx=0.5,rely=0.3,anchor=CENTER)

        def generate_invoice():
            global cart,cart_amount
            s_no=1
            if(inp1.get()=="" or inp2.get()==""):
                messagebox.showerror("Error","Please enter all details")
                return
            name=inp1.get()
            contact=inp2.get()
            lbl4=Label(root,text="Generating Invoice...")
            lbl4.place(relx=0.5,rely=0.8,anchor=CENTER)
            root.update()
            no=cur.execute("select max(inv_id) from transactions").fetchone()[0]
            filename=f"./Invoices/Invoice_{no+1}.pdf"
            cur.execute("insert into transactions(inv_id, cust_name, user_id, inv_path) values(:1,:2,:3,:4)",(no+1, name, ida, f"D:/python/Invoices/Invoice_{no+1}.pdf"))
            con.commit()
            title=f"Invoice_{no+1}"
            from reportlab.pdfgen import canvas
            pdf=canvas.Canvas(filename,pagesize=(200,270),bottomup=0)
            pdf.drawImage("./media/logo_inv.png",14,10,width=50,height=30)
            pdf.setTitle(title)
            pdf.setFont("Helvetica-Bold",8)
            pdf.drawCentredString(125,20,"Book Store Pvt Limited")
            pdf.setFont("Helvetica",5)
            pdf.drawString(80,28,"Contact : 1234567890")
            pdf.drawString(80,34,"Email : xyz@bookstore.in")
            pdf.drawString(80,40,"Address : 123, ABC Street, XYZ City, 123456")
            pdf.line(5,45,195,45)
            pdf.setFont("Courier-Bold",8)
            pdf.drawCentredString(100,55,"TAX-INVOICE")
            pdf.roundRect(15,63,170,40,1,stroke=1,fill=0)
            pdf.setFont("Times-Bold",5)
            pdf.drawString(20,71,"Customer Name : " + name)
            pdf.drawString(20,79,"Customer Contact :" + contact)
            pdf.drawString(20,95,"Invoice No. : " + str(no+1))
            pdf.drawString(20,87, "Created On : " + datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
            pdf.roundRect(15,108,170,130,1,stroke=1,fill=0)
            pdf.line(15,120,185,120)
            pdf.drawString(17,118,"S.No.")
            pdf.drawString(31,118,"Book ID")
            pdf.drawString(70,118,"DESCRIPTION")
            pdf.drawString(127,118,"RATE")
            pdf.drawString(147,118,"QTY")
            pdf.drawString(165,118,"TOTAL")
            pdf.line(15,210,185,210)
            pdf.line(30,108,30,220)
            pdf.line(50,108,50,220)
            pdf.line(125,108,125,220)
            pdf.line(145,108,145,220)
            pdf.line(160,108,160,220)
            y=128
            for inv_data in cart.get_children():
                pdf.drawString(18,y,str(s_no))
                pdf.drawString(34,y, str(cart.item(inv_data)["values"][0]))
                pdf.drawString(52,y, str(cart.item(inv_data)["values"][1]))
                pdf.drawString(127,y,str(cart.item(inv_data)["values"][2]))
                pdf.drawString(148,y, str(cart.item(inv_data)["values"][3]))
                pdf.drawString(165,y, str(cart.item(inv_data)["values"][4]))
                s_no+=1
                y+=6
                cur.execute("update books set stock=stock-:1 where b_id=:2",(int(cart.item(inv_data)["values"][3]),int(cart.item(inv_data)["values"][0])))
                con.commit()

            pdf.drawString(146,217,"Total:")
            pdf.drawString(165,217,f"{cart_amount}")
            pdf.line(15,220,185,220)
            pdf.line(100,220,100,238)
            pdf.drawString(28,225,"Terms - Due on receipt")
            pdf.drawString(20,235,"(This is system generated invoice)")
            pdf.setFont("Times-Bold",5)
            pdf.drawRightString(165,230,"(Includes 12 % GST)")
            pdf.setFont("Times-Bold",5)
            pdf.drawRightString(180,260,"Signature")
            pdf.save()
            messagebox.showinfo("Success","Invoice Generated Successfully !")
            root.destroy()
            cle_cart()
            data.delete(*data.get_children())
            cur.execute("select * from books")
            count=0
            for book in cur.fetchall():
                data.insert("",END,values=book,tags=('even' if count%2==0 else 'odd',))
                count+=1
            os.startfile(f"D:/python/Invoices/Invoice_{no+1}.pdf")
        but1=Button(root,text="Generate Invoice",command=lambda:generate_invoice())
        but1.place(relx=0.5,rely=0.5,anchor=CENTER)
        root.mainloop()
        

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
def gets():
    idd=e1.get()
    passw=e2.get()
    return idd,passw

def forgot(event):
    messagebox.showinfo("Forgot Password","Contact System Administator")  

def upd_canc():
    window.deiconify()
    window2.destroy()
    

def update(event):
    global e5,e3,e4,window2,bg2
    window.withdraw()
    window2=Tk()
    window2.title("Update Password")
    
    window2.maxsize(height="500",width="600")
    window2.minsize(height="500",width="600")

    bg2=Image.open("./media/login1.png").resize((600,500),Image.LANCZOS)
    bg2=ImageTk.PhotoImage(bg2,master=window2)

    canvas2=Canvas(window2)
    canvas2.place(relheight=1,relwidth=1,relx=0,rely=0)
    canvas2.create_image(0,0,image=bg2,anchor=NW)
    canvas2.create_text(200,160,text="Update",font=("Arial",20,"bold"))
    canvas2.create_text(190,200,text="Enter Username")
    e3=Entry(window2,bg="white")
    e3.place(x=320,y=200)
    canvas2.create_text(200,240,text="Enter Old Password")
    e4=Entry(window2,bg="white")
    e4.place(x=320,y=240)
    canvas2.create_text(200,280,text="Enter New Password")
    e5=Entry(window2,bg="white")
    e5.place(x=320,y=280)
    window2.bind("<Return>",update_pass)
    b1=Button(window2,text="Update",bg="white",command=lambda:update_pass("<Button-1>"))
    b1.place(x=230,y=320)
    b2=Button(window2,text="Exit",bg="white",command=upd_canc)
    b2.place(x=350,y=320)
    
    window2.mainloop()


def update_pass(event):
    co1=e3.get()
    co2=e4.get()
    co3=e5.get()
    if(co3==""):
        
        messagebox.showerror("Error","Enter A Valid New Password")
    else:
        try:
            cur.execute("select * from user_creds where id=:1 and pass=:2",(co1,co2))
            data=cur.fetchall()
            if (data):
                cur.execute("update user_creds set pass=:1 where id=:2",(co3,co1))
                messagebox.showinfo("Success","Password Updated Successfully")
                con.commit()
                window.deiconify()
                window2.destroy()
            else:
                messagebox.showerror("Error","Invalid Username or Password")
        except:
            messagebox.showerror("Error","Invalid Username or Password")


def check(event):
    cur.execute("select * from user_creds where id=:1 and pass=:2",gets())
    data=cur.fetchall()
    if (data):
        window.withdraw()
        if(data[0][3]=="admin"):
            adm_panel(e1.get(),e2.get())
        else:
            logged(e1.get(),e2.get())
    else:
        messagebox.showerror("Error","Invalid Username or Password")

def reg_cancel():
    window1.destroy()
    login()

def reg_cancel2():
    window1.destroy()
    window4.destroy()
    login()

def register_u(event):
    window.destroy()
    register(event)

def register_ag(event):
    window1.deiconify()
    window4.iconify()

def register(event):
    global e6,e7,window1,canvas1,window4
    window1=Tk()
    window1.title("Book Store Management System")
    window1.maxsize(height="500",width="600")
    window1.minsize(height="500",width="600")

    bg1=Image.open("./media/login1.png").resize((600,500),Image.LANCZOS)
    bg1=ImageTk.PhotoImage(bg1,master=window1)

    canvas1=Canvas(window1)
    canvas1.place(relheight=1,relwidth=1,relx=0,rely=0)
    canvas1.create_image(0,0,image=bg1,anchor=NW)
    canvas1.create_text(210,160,text="Register",font=("Arial",20,"bold"))
    canvas1.create_text(190,210,text="Enter Username")
    e6=Entry(window1,bg="white")
    e6.place(x=320,y=210)
    canvas1.create_text(190,250,text="Enter Password")
    e7=Entry(window1,bg="white",show="*")
    e7.place(x=320,y=250)
    def nextpage(event):
        global window4
        window1.iconify()
        window4=Tk()
        window4.title("Book Store Management System")
        window4.maxsize(height="500",width="600")
        window4.minsize(height="500",width="600")
        canvas_n=Canvas(window4)
        canvas_n.place(relheight=1,relwidth=1,relx=0,rely=0)
        bg3=Image.open("./media/login1.png").resize((600,500),Image.LANCZOS)
        bg3=ImageTk.PhotoImage(bg3,master=canvas_n)
        canvas_n.create_image(0,0,image=bg3,anchor=NW)
        canvas_n.create_text(240,150,text="Select Avatar",font=("Arial",20,"bold"))
        canvas_n.create_text(250,180,text="Click on the image to select")
        a=150
        b=200
        labels = []
        for path in avatarl:
            image = Image.open(path).resize((60,60),Image.LANCZOS)
            photo = ImageTk.PhotoImage(image,master=canvas_n)
            label = Label(canvas_n, image=photo,bg="white")
            label.photo = photo
            photo.name=path
            label.image=photo
            label.place(x=a,y=b)
            a+=80
            if(a>400):
                a=150
                b+=80
            labels.append(label)
        def label_click(event):
            for i in range(len(labels)):
                if event.widget == labels[i]:
                    labels[i].config(bg="darkgreen")
                    global av
                    image = event.widget.image
                    av=avatarl.index(image.name)+1
                else:
                    labels[i].config(bg="white")
            

        for label in labels:
            label.bind("<Button-1>", label_click)
        b1=Button(window4,text="Register",bg="white",command=lambda :register_user("<Button-1>"))
        b1.place(x=210,y=350)
        b2=Button(window4,text="Exit",bg="white",command=reg_cancel2)
        b2.place(x=370,y=350)
        b3=Button(window4,text="Back",bg="white",command=lambda :register_ag("<Button-1>"))
        b3.place(x=290,y=350)
        window4.mainloop()
    b1=Button(window1,text="Next Page",bg="white",command=lambda:nextpage("<Button-1>"))
    b1.place(x=230,y=300)
    window1.bind("<Return>",nextpage)
    b2=Button(window1,text="Exit",bg="white",command=reg_cancel)
    b2.place(x=350,y=300)
    mainloop()

def register_user(event):
    if(e6.get()=="" or e7.get()==""):
        messagebox.showerror("Error","Enter A Valid Username and Password")
    else:
        try:
            cur.execute("insert into user_creds values(:1,:2,:3,:4)",(e6.get(),e7.get())+(av,"user"))
            messagebox.showinfo("Success"," User Registered Successfully")
            print("Data inserted successfully")
            con.commit()
            window1.destroy()
            window4.destroy()
            login()
        except:
            messagebox.showerror("Error","User already exists")
            print("Error while inserting data")

def exit(event):
    window.destroy()

def show(event):
    e2.config(show="") 
    canvas.itemconfig(cb1,image=invisible)
    canvas.tag_bind(cb1,"<Button-1>",hide)

def hide(event):
    e2.config(show="*") 
    canvas.itemconfig(cb1,image=eyebut)
    canvas.tag_bind(cb1,"<Button-1>",show)

def on_enter(event):
    canvas.configure(cursor="hand2")
def on_leave(event):
    canvas.configure(cursor="")


avatarl=["./media/Avatars/b1.png",
         "./media/Avatars/b2.png",
         "./media/Avatars/b3.png",
         "./media/Avatars/b4.png",
         "./media/Avatars/g1.png",
         "./media/Avatars/g2.png",
         "./media/Avatars/g3.png",
         "./media/Avatars/g4.png"]

ima=list(range(1,9))

def login():
    global e1,e2,window,canvas,cb1,eyebut,invisible,btn1,btn3,btn4,btn5,bg
    window=Tk()
    window.title("Book Store Management System")
    window.iconbitmap("./media/favicon(1).ico")
    window.maxsize(height="600",width="800")
    window.minsize(height="600",width="800")

    bg=Image.open("./media/login2.png").resize((800,600))
    bg1=ImageTk.PhotoImage(bg,master=window)

    canvas=Canvas(window)
    canvas.place(relheight=1,relwidth=1,relx=0,rely=0)
    canvas.create_image(0,0,image=bg1,anchor=NW)

    logbut=Image.open("./media/login_button.png").resize((65,25),Image.LANCZOS)
    logbut=ImageTk.PhotoImage(logbut,master=window)

    rembut=Image.open("./media/remove.png").resize((20,20),Image.LANCZOS)
    rembut=ImageTk.PhotoImage(rembut,master=window)

    eyebut=Image.open("./media/eye.png").resize((25,25),Image.LANCZOS)
    eyebut=ImageTk.PhotoImage(eyebut,master=window)

    invisible=Image.open("./media/invisible.png").resize((25,25),Image.LANCZOS)
    invisible=ImageTk.PhotoImage(invisible,master=window)

    textbox=Image.open("./media/TextBox.png").resize((270,27),Image.LANCZOS)
    textbox=ImageTk.PhotoImage(textbox,master=window)

    canvas.create_text(260,183,anchor=NW,text="Username*",font=("calibri",13))

    canvas.create_image(255,207,image=textbox,anchor=NW)
    e1=Entry(canvas,insertbackground="white",border=0,bg="black",fg="white")
    e1.place(relheight=0.033,relwidth=0.31,relx=0.33,rely=0.35)

    canvas.create_text(260,253,anchor=NW,text="Password*",font=("calibri",13))
    canvas.create_image(255,278,image=textbox,anchor=NW)
    e2=Entry(canvas,show="*",insertbackground="white",border=0,bg="black",fg="white")
    e2.place(relheight=0.033,relwidth=0.31,relx=0.33,rely=0.47)

    cb1=canvas.create_image(535,278,image=eyebut,anchor=NW)
    canvas.tag_bind(cb1,'<Button-1>',show)
    canvas.tag_bind(cb1,"<Enter>",on_enter)
    canvas.tag_bind(cb1,"<Leave>",on_leave)

    btn1=canvas.create_image(375,340,image=logbut,anchor=NW)
    canvas.tag_bind(btn1,"<Button-1>",check)
    canvas.tag_bind(btn1,"<Enter>",on_enter)
    canvas.tag_bind(btn1,"<Leave>",on_leave)
    window.bind("<Return>",check)


    btn3=canvas.create_text(330,440,anchor=NW,text="Don't have an account ?",font=("calibri",13))
    canvas.tag_bind(btn3,"<Button-1>",register_u)
    canvas.tag_bind(btn3,"<Enter>",on_enter)
    canvas.tag_bind(btn3,"<Leave>",on_leave)

    btn5=canvas.create_text(240,390,anchor=NW,text="Update Password",font=("calibri",13))
    canvas.tag_bind(btn5,"<Button-1>",update)
    canvas.tag_bind(btn5,"<Enter>",on_enter)
    canvas.tag_bind(btn5,"<Leave>",on_leave)

    btn4=canvas.create_text(440,390,anchor=NW,text="Forgot Password ?",font=("calibri",13))
    canvas.tag_bind(btn4,"<Button-1>",forgot)
    canvas.tag_bind(btn4,"<Enter>",on_enter)
    canvas.tag_bind(btn4,"<Leave>",on_leave)
    window.mainloop()