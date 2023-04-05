# import oracledb
from tkinter import *
# from PIL import ImageTk,Image,ImageDraw

# con=oracledb.connect(user='C##Nitish',password='123',dsn='192.168.19.1/orcl')
# print("Successfully connected to Oracle Database")
# cur=con.cursor()

# window=Tk()
# window.title("Student Details")
# window.minsize(height="400",width="600")

# canvas=Canvas(window)
# canvas.place(relheight=1,relwidth=1,relx=0,rely=0)

# # ima=list(range(1,9))

# # canvas.place(relheight=0.8,relwidth=0.8,relx=0.1,rely=0.1)
# # a=0
# # b=0
# # i=0
# # # for i in range(0,8):
# # #     ima[i]=Image.open(avatarl[i]).resize((100,100),Image.LANCZOS)
# # #     ima[i]=ImageTk.PhotoImage(ima[i])
# # #     canvas.create_image(a,b,image=ima[i],anchor=NW)
# # #     a+=120
# # #     if(a>400):
# # #         a=0
# # #         b+=120
# #     # canvas.tag_bind(ima[i],)


# # cur.execute("select avatar from user_creds where id='admin'")
# # ai=cur.fetchone()
# # ai=int(ai[0])-1
# # avt=Image.open(avatarl[ai]).resize((100,100),Image.LANCZOS)
# # avt=ImageTk.PhotoImage(avt)
# # canvas.create_image(0,0,image=avt,anchor=NW)

# avatarl=["./media/Avatars/b1.png",
#          "./media/Avatars/b2.png",
#          "./media/Avatars/b3.png",
#          "./media/Avatars/b4.png",
#          "./media/Avatars/g1.png",
#          "./media/Avatars/g2.png",
#          "./media/Avatars/g3.png",
#          "./media/Avatars/g4.png"]

# def select_image(event):
#     # Get the image object from the event widget
#     image = event.widget.image
#     # Print its name attribute
#     print(image.name)

# # Create a label for each image and bind it to a mouse click event
# for i in range(len(avatarl)):
#     # Open the image using PIL
#     im = Image.open(avatarl[i])
#     # Resize it to fit the label
#     im = im.resize((50, 50))
#     # Create a PhotoImage object from PIL image and give it a name attribute
#     tkimage = ImageTk.PhotoImage(im)
#     tkimage.name = avatarl[i]
#     # Create a label with the PhotoImage object as its image option
#     label = Label(canvas, image=tkimage)
#     # Keep a reference to the PhotoImage object
#     label.image = tkimage
#     # Bind it to a mouse click event and call select_image function on click
#     label.bind("<Button-1>", select_image)
#     # Pack it in the frame with some padding
#     label.pack(side=LEFT, padx=10)

# mainloop()



# # # canvas.create_rounded_rectangle(0,0,400,400,fill="white",radius=10)
# # draw=ImageDraw.Draw(window)
# # draw.rounded_rectangle((0,0,400,400),fill="white",radius=10)


# # //draw a rounded rectangle in python
# # result = Image.new('RGBA', (100, 100))
# # draw = ImageDraw.Draw(result)
# # draw.rounded_rectangle(((0, 0), (100, 100)), 20, fill="blue")
# # result.show()


# # white = Label(window,bg='white',width=600,height=500,border=0)
# # white.pack()

# # entry_name=Image.open('./media/login_bg.jpg')
# # entry_name = ImageTk.PhotoImage(entry_name,master=window)
# # entry_image = Label(window,image=entry_name,border=0,bg='white')
# # entry_image.place()

# # txt1=Label(window,bg="white",fg="black",text="Login Page",font=("times",16))
# # txt1.place(relheight=0.1,relwidth=1,relx=0,rely=0.1)

# # txt1=Label(window,bg="white",fg="black",text="Login Page",font=("corbel",16))
# # txt1.place(relheight=0.1,relwidth=1,relx=0,rely=0.2)

# # txt1=Label(window,bg="white",fg="black",text="Login Page",font=("blues smile",16))
# # txt1.place(relheight=0.1,relwidth=1,relx=0,rely=0.3)

# # txt1=Label(window,bg="white",fg="black",text="Login Page",font=("arial",16))
# # txt1.place(relheight=0.1,relwidth=1,relx=0,rely=0.4)

# # txt1=Label(window,bg="white",fg="black",text="Login Page",font=("Helvatica",16))
# # txt1.place(relheight=0.1,relwidth=1,relx=0,rely=0.5)




# # name_entry = Entry(window,width=27,border=0,font=('bold',11))
# # name_entry.place(x=267,y=144)

# # Email = Label(window,bg='white',font=('Bold',16),border=0,text="Email")
# # Email.place(x=345,y=170)
# # images=[]

# # # Define a function to make the transparent rectangle
# # def create_rectangle(x,y,a,b,**options):
# #     if 'alpha' in options:
# #         # Calculate the alpha transparency for every color(RGB)
# #         alpha = int(options.pop('alpha') * 255)
# #         # Use the fill variable to fill the shape with transparent color
# #         fill = options.pop('fill')
# #         fill = window.winfo_rgb(fill) + (alpha,)
# #         image = Image.new('RGBA', (a-x, b-y), fill)
# #         images.append(ImageTk.PhotoImage(image))
# #         canvas.create_image(x, y, image=images[-1], anchor='nw')
# #         canvas.create_rectangle(x, y,a,b, **options)
# # # Add a Canvas widget
# # canvas= Canvas(window)

# # # Create a rectangle in canvas
# # create_rectangle(50, 110,300,280, fill= "blue", alpha=.3)
# # create_rectangle(40, 90, 420, 250, fill= "red", alpha= .1)
# # canvas.pack()



# # mainloop()


# # bg=Image.open("bg.jpg")
# # bg=ImageTk.PhotoImage(bg,master=window)
# # canvas.create_image(0,0,image=bg,anchor=NW)

# # window.minsize(height="400",width="400")
# # window.mainloop()

# # cur.execute("create table student1 (id number(5),name varchar2(20),marks number(5))")
# # print("Table created successfully")

# # for i in range(1,3):
# #     id=int(input("Enter the id: "))
# #     name=input("Enter the name: ")
# #     marks=int(input("Enter the marks: "))
# #     cur.execute("insert into student1 values(:1,:2,:3)",(id,name,marks))
# #     print("Data inserted successfully")

# # cur.execute("select * from student1")
# # data=cur.fetchall()
# # for row in data:
# #     print("ID: ",row[0])
# #     print("Name: ",row[1])
# #     print("Marks: ",row[2])


# cur.close()
# con.commit()
# con.close()



root=Tk()
root.title("Login Page")
root.minsize(height="700",width="1500")
root.maxsize(height="700",width="1500")
mainloop()