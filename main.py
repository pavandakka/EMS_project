from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if username.get()=='' or password.get()=='':
        messagebox.showerror('ERROR','All fields are required')
    elif username.get()=='pavan' and password.get()=='dakka':
        messagebox.showinfo('Success','Login Successfull')
        root.destroy()
        import ems
    else:
        messagebox.showwarning('ERROR','Wrong Credentials')


root=CTk()
root.geometry('1024x600')
root.resizable(0,0)
root.title('Login Page')
image=CTkImage(Image.open('EMS.jpg'),size=(1024,600))
imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headingLabel=CTkLabel(root,text='Emploeee Management System',bg_color='transparent',font=('arial',20,'bold'))
headingLabel.place(x=50,y=200)


username=CTkEntry(root,placeholder_text='Enter Your Username',width=180)
username.place(x=70,y=250)

password=CTkEntry(root,placeholder_text='password',width=180,show='*')
password.place(x=70,y=280)

loginButton=CTkButton(root,text='Login',cursor='hand2',command=login)
loginButton.place(x=80,y=310)

root.mainloop()