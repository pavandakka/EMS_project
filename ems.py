from bokeh.layouts import column
from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import database


#functions

def deleteall_employee():
    res=messagebox.askyesno('confirm','Do you want to delete all records?')
    if res:
        database.deleteall()


def show_all():
    treeview_data()


def search_employee():
    if searchBox.get()=='':
        messagebox.showerror('ERROR','Please select an option')
    elif searchEntry.get()=='':
        messagebox.showerror('ERROR','Enter value to search')
    else:
        search_data=database.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in search_data:
            tree.insert('', END, values=employee)


def delete_employee():
    selected_items=tree.selection()
    if not selected_items:
        messagebox.showerror('ERROR','select data to delete')
    else:
        database.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is deleted')


def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('ERROR','select data to Updata')
    else:
        database.update(idEntry.get(),nameEntry.get(),phEntry.get(),roleComboBox.get(),genderComboBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is updated')


def selection(dpk):
    selectecd_items=tree.selection()
    if selectecd_items:
        row=tree.item(selectecd_items)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phEntry.insert(0,row[2])
        roleComboBox.set(row[3])
        genderComboBox.set(row[4])
        salaryEntry.insert(0,row[5])


def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phEntry.delete(0,END)
    roleComboBox.set('Web Developer')
    genderComboBox.set('Male')
    salaryEntry.delete(0,END)


def treeview_data():
    employees=database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('',END,values=employee)


def add_employee():
    if idEntry.get()=='' or nameEntry.get()=='' or phEntry.get()=='' or salaryEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('ERROR','ID already exists')
    else:
        database.insert(idEntry.get(),nameEntry.get(),phEntry.get(),roleComboBox.get(),genderComboBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Done', 'Added successfully')


#SUI Interface

window=CTk()
window.geometry('1000x600')
window.title('Employee Management System')
window.resizable(False,False)
window.configure(fg_color='black')
image=CTkImage(Image.open('windowban.jpg'),size=(1024,200))
imageLabel=CTkLabel(window,image=image,text='')
imageLabel.grid(row=0,column=0,columnspan=2)


leftframe=CTkFrame(window,fg_color='black')
leftframe.grid(row=1,column=0)


idLabel=CTkLabel(leftframe,text='ID',font=('arial',18,'bold'))
idLabel.grid(row=0,column=0,padx=20,pady=10,sticky='w' )

idEntry=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
idEntry.grid(row=0,column=1)


nameLabel=CTkLabel(leftframe,text='Name',font=('arial',18,'bold'))
nameLabel.grid(row=1,column=0,padx=20,pady=10 ,sticky='w'  )

nameEntry=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
nameEntry.grid(row=1,column=1)


phLabel=CTkLabel(leftframe,text='Phone',font=('arial',18,'bold'))
phLabel.grid(row=2,column=0,padx=20,pady=10,sticky='w' )

phEntry=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
phEntry.grid(row=2,column=1)


roleLabel=CTkLabel(leftframe,text='Role',font=('arial',18,'bold'))
roleLabel.grid(row=3,column=0,padx=20,pady=10,sticky='w' )

role=['Web Developer','Cloud Architect','Technical Writer','DevOps Engineer','Data Scientist','Bussiness Analysist','IT Consultant','Python Developer']
roleComboBox=CTkComboBox(leftframe,values=role,width=180,state='readonly')
roleComboBox.grid(row=3,column=1)
roleComboBox.set(role[0])


genderlabel=CTkLabel(leftframe,text='Gender', font=('arial',18,'bold'))
genderlabel.grid(row=4,column=0,padx=20,pady=10,sticky='w' )

gender=['Male','Female']
genderComboBox=CTkComboBox(leftframe,values=gender,width=180,state='readonly')
genderComboBox.grid(row=4,column=1)
genderComboBox.set('Male')


salaryLabel=CTkLabel(leftframe,text='Salary',font=('arial',18,'bold'))
salaryLabel.grid(row=5,column=0,padx=20,pady=10,sticky='w' )

salaryEntry=CTkEntry(leftframe,font=('arial',15,'bold'),width=180)
salaryEntry.grid(row=5,column=1)


rightframe=CTkFrame(window)
rightframe.grid(row=1,column=1)

search=['Id','Name','Phone','Role','Gender','Salary']
searchBox=CTkComboBox(rightframe,values=search,width=100,state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Search by')

searchEntry=CTkEntry(rightframe)
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightframe,text='Search',width=100,command=search_employee)
searchButton.grid(row=0,column=2)

showButton=CTkButton(rightframe,text='Show All',width=100,command=show_all)
showButton.grid(row=0,column=3,pady=5)


tree=ttk.Treeview(rightframe,height=9)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=('Id','Name','Phone','Role','Gender','Salary')

tree.heading('Id',text='ID')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')

tree.config(show='headings')

tree.column('Id',width=90)
tree.column('Name',width=190)
tree.column('Phone',width=150)
tree.column('Role',width=140)
tree.column('Gender',width=90)
tree.column('Salary',width=120)

style=ttk.Style()
style.configure('Treeview.Heading',font=('arial',15,'bold'))
style.configure('Treeview',font=('arial',11,'bold'),rowheight=30)

srcollbar=ttk.Scrollbar(rightframe,orient=VERTICAL,command=tree.yview)
srcollbar.grid(row=1,column=4,sticky='ns')

tree.config(yscrollcommand=srcollbar.set)

buttonframe=CTkFrame(window,fg_color='black')
buttonframe.grid(row=2,column=0,columnspan=3,pady=30)

newButton=CTkButton(buttonframe, text='New Employee',font=('arial',13,'bold'), width=130,corner_radius=15,command=lambda: clear(True))
newButton.grid(row=0,column=0,padx=10)

addButton=CTkButton(buttonframe, text='Add Employee',font=('arial',13,'bold'), width=130,corner_radius=15,command=add_employee)
addButton.grid(row=0,column=1,padx=10)

updateButton=CTkButton(buttonframe, text='Update Employee',font=('arial',13,'bold'), width=130,corner_radius=15,command=update_employee)
updateButton.grid(row=0,column=2,padx=10)

deleteButton=CTkButton(buttonframe, text='Delete Employee',font=('arial',13,'bold'), width=130,corner_radius=15,command=delete_employee)
deleteButton.grid(row=0,column=3,padx=10)

deleteallButton=CTkButton(buttonframe, text='Delete All',font=('arial',13,'bold'), width=130,corner_radius=15,command=deleteall_employee)
deleteallButton.grid(row=0,column=4,padx=10)

treeview_data()

window.bind('<ButtonRelease>',selection)

window.mainloop()