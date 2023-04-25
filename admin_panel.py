from tkinter import *
from PIL import ImageTk,Image
import main
from tkinter import ttk,messagebox


def adm_panel(ida,passwa,cur,con):
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
    avt=Image.open(main.avatarl[ai]).resize((100,100),Image.LANCZOS)
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
        main.login()
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

    def books_show(event):
        canvas3.itemconfig(but1,image=books_s)
        global data,scroll
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
        if scroll:
            scroll.place_forget()
        global data,search_box2
        canvas3.itemconfig(but2,image=users_s)
        cur.execute("select * from user_creds")
        users=cur.fetchall()
        data=ttk.Treeview(canvas3,height=10)
        search_box2=Entry(canvas3)
        search_box2.place(relheight=0.05,relwidth=0.4,relx=0.2,rely=0.03)
        search_box2.insert(0,"Search Here by User Id")
        def search_box_click2(event):
            search_box2.delete(0,END)
            search_box2.unbind("<Button-1>")
        search_box2.bind("<Button-1>",search_box_click2)
        def upd_data(event):
            data.delete(*data.get_children())
            val=search_box2.get()
            cur.execute("SELECT * FROM user_creds WHERE lower(id) LIKE '%"+val+"%'")
            if len(search_box2.get())>0:
                count=0
                for row in cur.fetchall():
                        data.insert(parent='',index='end',iid=row[0],values=row,tags=('even' if count%2==0 else 'odd',))
                        count+=1

            if len(search_box2.get())==0:
                            data.delete(*data.get_children())
                            cur.execute("SELECT * FROM user_creds")
                            count=0
                            for row in cur.fetchall():
                                data.insert(parent='',index='end',iid=row[0],values=row,tags=('even' if count%2==0 else 'odd',))
                                count+=1
        search_box2.bind("<KeyRelease>",upd_data)
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

        selection1.configure(command=sel2)
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
        if scroll:
            scroll.place_forget()
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
        data.place(relwidth=0.8,relx=0.18,rely=0.15)
        cur.execute("select * from transactions")
        bot=cur.fetchall()
        count=0
        for i in bot:
            data.insert(parent="",index="end",iid=i[0],values=i,tags=('even' if count%2==0 else 'odd',))
            count+=1
        global search_box3
        search_box3=Entry(canvas3)
        search_box3.place(relheight=0.05,relwidth=0.4,relx=0.2,rely=0.03)
        search_box3.insert(0,"Search Here by Invoice Id")
        def search_box_click3(event):
            search_box3.delete(0,END)
            search_box3.unbind("<Button-1>")
        search_box3.bind("<Button-1>",search_box_click3)
        def upd_data3(event):
            data.delete(*data.get_children())
            val=search_box3.get()
            cur.execute("SELECT * FROM transactions WHERE inv_id like '%"+val+"%'")
            if len(search_box3.get())>0:
                count=0
                for row in cur.fetchall():
                        data.insert(parent='',index='end',iid=row[0],values=row,tags=('even' if count%2==0 else 'odd',))
                        count+=1
            if len(search_box3.get())==0:
                            data.delete(*data.get_children())
                            cur.execute("SELECT * FROM transactions")
                            count=0
                            for row in cur.fetchall():
                                data.insert(parent='',index='end',iid=row[0],values=row,tags=('even' if count%2==0 else 'odd',))
                                count+=1

        search_box3.bind("<KeyRelease>",upd_data3)
        global recordss_frame,trans_frame
        recordss_frame=LabelFrame(canvas3,text="Records")
        recordss_frame.place(relheight=0.2,relwidth=0.8,relx=0.18,rely=0.6)
        id_label=Label(recordss_frame,text="Id")
        id_label.place(relheight=0.3,relx=0.06,rely=0.1)
        id_entry=Entry(recordss_frame)
        id_entry.place(relheight=0.25,relwidth=0.2,relx=0.10,rely=0.1)
        cust_name_label=Label(recordss_frame,text="Customer")
        cust_name_label.place(relheight=0.3,relx=0.02,rely=0.5)
        cust_name_entry=Entry(recordss_frame)
        cust_name_entry.place(relheight=0.25,relwidth=0.2,relx=0.10,rely=0.5)
        clerk_label=Label(recordss_frame,text="Clerk")
        clerk_label.place(relheight=0.3,relx=0.36,rely=0.1)
        clerk_entry=Entry(recordss_frame)
        clerk_entry.place(relheight=0.25,relwidth=0.2,relx=0.43,rely=0.1)
        path_label=Label(recordss_frame,text="Inv Path")
        path_label.place(relheight=0.3,relx=0.36,rely=0.5)
        path_entry=Entry(recordss_frame)
        path_entry.place(relheight=0.25,relwidth=0.2,relx=0.43,rely=0.5)
        date_label=Label(recordss_frame,text="Date")
        date_label.place(relheight=0.3,relx=0.72,rely=0.3)
        date_entry=Entry(recordss_frame)
        date_entry.place(relheight=0.25,relwidth=0.2,relx=0.78,rely=0.3)

        trans_frame=LabelFrame(canvas3,text="Commands")
        trans_frame.place(relheight=0.1,relwidth=0.8,relx=0.18,rely=0.85)
        def sel3():
            clear()
            curItem=data.focus()
            id_entry.delete(0,END)
            cust_name_entry.delete(0,END)
            clerk_entry.delete(0,END)
            path_entry.delete(0,END)
            date_entry.delete(0,END)
            id_entry.insert(0,data.item(curItem)['values'][0])
            cust_name_entry.insert(0,data.item(curItem)['values'][1])
            clerk_entry.insert(0,data.item(curItem)['values'][2])
            path_entry.insert(0,data.item(curItem)['values'][3])
            date_entry.insert(0,data.item(curItem)['values'][4])
        selection1.configure(command=sel3)
        def clear():
            id_entry.delete(0,END)
            cust_name_entry.delete(0,END)
            clerk_entry.delete(0,END)
            path_entry.delete(0,END)
            date_entry.delete(0,END)
        import os
        def open_inv():
            curItem=data.focus()
            path=data.item(curItem)['values'][3]
            os.startfile(path)
        def upd_tree():
            data.delete(*data.get_children())
            cur.execute("SELECT * FROM transactions")
            count=0
            for row in cur.fetchall():
                data.insert(parent='',index='end',iid=row[0],values=row,tags=('even' if count%2==0 else 'odd',))
                count+=1
        def delete():
            if len(id_entry.get())==0:
                messagebox.showerror("Error","Id Field is Required")
                return
            try:
                os.remove(path_entry.get())
                cur.execute("DELETE FROM transactions WHERE inv_id=:inv_id",{'inv_id':id_entry.get()})
                con.commit()
                messagebox.showinfo("Success","Record Deleted Successfully")

            except:
                messagebox.showerror("Error","Can't Delete This Record")
            clear()
            upd_tree()
        b1=Button(trans_frame,text="Open Invoice",command=open_inv)
        b1.place(relheight=0.6,relwidth=0.1,relx=0.175,rely=0.1)
        b3=Button(trans_frame,text="Delete Invoice",command=delete)
        b3.place(relheight=0.6,relwidth=0.1,relx=0.45,rely=0.1)
        b4=Button(trans_frame,text="Clear All Fields",command=clear)
        b4.place(relheight=0.6,relwidth=0.1,relx=0.725,rely=0.1)

    window3.mainloop()