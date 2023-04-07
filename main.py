import oracledb
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import user_panel
import admin_panel

con=oracledb.connect(user="C##Nitish",password="123",dsn="192.168.19.1/orcl")
print("Successfully connected to Oracle Database")
cur=con.cursor()

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
        con.close()
        if(data[0][3]=="admin"):
            admin_panel.adm_panel(e1.get(),e2.get())
        else:
            user_panel.logged(e1.get(),e2.get())
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


        # for i in range(0,8):
        #         ima[i]=Image.open(avatarl[i]).resize((60,60),Image.LANCZOS)
        #         ima[i]=ImageTk.PhotoImage(ima[i],master=canvas_n)
        #         ima[i].name = avatarl[i]
        #         label=Label(canvas_n,image=ima[i])
        #         label.image=ima[i]
        #         label.place(x=a,y=b)
        #         def img_click(event):
        #             image = event.widget.image
                    
        #             global av
        #             av=avatarl.index(image.name)+1
        #             print (av)
        #         label.bind('<Button-1>',img_click)
        #         a+=80
        #         if(a>400):
        #             a=150
        #             b+=80
        
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
    con.close()

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

if __name__ == "__main__":
    login()



