""" Title: Create, Reed, Update, Detele app
    Author: Guillermo Leon
    website: https://savingl.cl

    To do:
"""

from tkinter import *
import sqlite3
from tkinter.messagebox import showinfo, askyesno, showwarning
from hamcrest import none

raiz=Tk()
raiz.title("CRUD App")

miFrame=Frame(raiz)
miFrame.pack()

""" ------------------ Functionality ------------ 
Conectar
Salir
"""

myConnection = None
myCursor = None

def connect():
    global myConnection, myCursor
    myConnection = sqlite3.connect("CRUD_DB")
    myCursor = myConnection.cursor()
    myCursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(50),
        apellido VARCHAR(50),
        password VARCHAR(20),
        direccion VARCHAR(50),
        comentarios TEXT
        );""")

    showinfo("Connection", "You have succesfully connected to the database, if the database doesn't exist, we have just created it for you")

def create():
    global myCursor, myConnection

    nombre_value = NombreEntry.get()
    apellido_value = ApellidoEntry.get()
    password_value = PasswordEntry.get()
    direccion_value = DireccionEntry.get()
    comentarios_value = ComentariosEntry.get("1.0",'end-1c')

    values_list = (nombre_value,apellido_value,password_value,direccion_value,comentarios_value)
    
    myCursor.execute("""INSERT INTO usuarios VALUES(NULL,?,?,?,?,?);""",values_list) 
    myConnection.commit()

    showinfo("Record created", "You have succesfully created a record")

def read():
    global myCursor

    id_value = IdEntry.get()

    try:
        myCursor.execute("SELECT * FROM usuarios WHERE id = ?",id_value)
        usuarios=myCursor.fetchall()

        #Delete everything that is already in the entry
        NombreEntry.delete(0,END)
        ApellidoEntry.delete(0,END)
        PasswordEntry.delete(0,END)
        DireccionEntry.delete(0,END)
        ComentariosEntry.delete(1.0,END)

        #Access and store the items inside the tuple that's inside the list returned by the .fetchall
        items = usuarios[0]

        #Show the values in the entry
        NombreEntry.insert(0,items[1])
        ApellidoEntry.insert(0,items[2])
        PasswordEntry.insert(0,items[3])
        DireccionEntry.insert(0,items[4])
        ComentariosEntry.insert(1.0,items[5])
    except:
        showwarning('Error','The registry does not exist')

def update():
    global myCursor, myConnection
    confirmation = askyesno("Are you sure?", "You are about to update a record, click 'Yes' to confirm, 'No' to cancel")
    if confirmation == True:
        values_list = [ #List of tuples that contains the database field name and the GUI field value
        (NombreEntry.get(),IdEntry.get()),
        (ApellidoEntry.get(),IdEntry.get()),
        (PasswordEntry.get(),IdEntry.get()),
        (DireccionEntry.get(),IdEntry.get()),
        (ComentariosEntry.get("1.0",'end-1c'),IdEntry.get())
        ]

        #Table names and column names must be "hardcoded", these can't be iterated with placeholders. See https://stackoverflow.com/questions/6514274/how-do-you-escape-strings-for-sqlite-table-column-names-in-python
        myCursor.execute("UPDATE usuarios SET nombre = :1 WHERE id = :2;",values_list[0])
        myCursor.execute("UPDATE usuarios SET apellido = :1 WHERE id = :2;",values_list[1])
        myCursor.execute("UPDATE usuarios SET password = :1 WHERE id = :2;",values_list[2])
        myCursor.execute("UPDATE usuarios SET direccion = :1 WHERE id = :2;",values_list[3])
        myCursor.execute("UPDATE usuarios SET comentarios = :1 WHERE id = :2;",values_list[4])
        myConnection.commit()

def delete():
    global myCursor, myConnection
    confirmation = askyesno("Are you sure?", "You are about to delete a record, click 'Yes' to confirm, 'No' to cancel")
    if confirmation == True:
        myCursor.execute("DELETE FROM usuarios WHERE id = ?", IdEntry.get())
        myConnection.commit()



def clear():
    IdEntry.delete(0,END)
    NombreEntry.delete(0,END)
    ApellidoEntry.delete(0,END)
    PasswordEntry.delete(0,END)
    DireccionEntry.delete(0,END)
    ComentariosEntry.delete(1.0,END)

def about():
    showinfo("About CRUD App", "As part of the 'learning python' repository, this app was developed by Guillermo Leon. Website: https//:savingl.cl")

def exit():
    confirmation = askyesno("Exit", "Do you want to exit?")
    if confirmation == True:
        raiz.quit()

""" ---------------- Menu Bar  -------------"""

menubar = Menu(raiz)
raiz.config(menu=menubar)


BBDDmenu = Menu(menubar,tearoff=0)
BBDDmenu.add_command(label="Connect", command=connect)
BBDDmenu.add_command(label="Exit", command=exit)

Borrarmenu = Menu(menubar,tearoff=0)
Borrarmenu.add_command(label="Clear fields", command=clear)

CRUDmenu = Menu(menubar,tearoff=0)
CRUDmenu.add_command(label="Create", command=create)
CRUDmenu.add_command(label="Read",command=read)
CRUDmenu.add_command(label="Update",command=update)
CRUDmenu.add_command(label="Delete",command=delete)

Ayudamenu = Menu(menubar,tearoff=0)
Ayudamenu.add_command(label="About CRUD App", command=about)


menubar.add_cascade(label="BBDD", menu=BBDDmenu)
menubar.add_cascade(label="Borrar", menu=Borrarmenu)
menubar.add_cascade(label="CRUD", menu=CRUDmenu)
menubar.add_cascade(label="Ayuda", menu=Ayudamenu)

#Alternatively to this disposition is to create two frames: one for the labels and fields and another for the buttons 

""" ---------------- Labels  -------------"""
IdLabel= Label(miFrame, text="Id")
IdLabel.grid(row = 1, column = 1, padx= 10, pady=10, columnspan=2)

NombreLabel= Label(miFrame, text="Nombre")
NombreLabel.grid(row = 2, column = 1, padx= 10, pady=10, columnspan=2)

ApellidoLabel= Label(miFrame, text="Apellido")
ApellidoLabel.grid(row = 3, column = 1, padx= 10, pady=10, columnspan=2)

PasswordLabel= Label(miFrame, text="Password")
PasswordLabel.grid(row = 4, column = 1, padx= 10, pady=10, columnspan=2)

DireccionLabel= Label(miFrame, text="Direccion")
DireccionLabel.grid(row = 5, column = 1, padx= 10, pady=10, columnspan=2)

ComentariosLabel= Label(miFrame, text="Comentarios")
ComentariosLabel.grid(row = 6, column = 1, padx= 10, pady=10, columnspan=2)


""" ---------------- Fields  -------------"""

IdEntry = Entry(miFrame)
IdEntry.grid(row = 1, column = 3, padx= 10, pady=10, columnspan=4)

NombreEntry = Entry(miFrame)
NombreEntry.grid(row = 2, column = 3, padx= 10, pady=10, columnspan=4)

ApellidoEntry = Entry(miFrame)
ApellidoEntry.grid(row = 3, column = 3, padx= 10, pady=10, columnspan=4)

PasswordEntry = Entry(miFrame)
PasswordEntry.grid(row = 4, column = 3, padx= 10, pady=10, columnspan=4)
PasswordEntry.config(show="*")

DireccionEntry = Entry(miFrame)
DireccionEntry.grid(row = 5, column = 3, padx= 10, pady=10, columnspan=4)

ComentariosEntry = Text(miFrame, width= 16, height= 5)
ComentariosEntry.grid(row = 6, column = 3, padx= 10, pady=10, columnspan=4)

scrollComentarios=Scrollbar(miFrame,command=ComentariosEntry.yview)
scrollComentarios.grid(row=6,column=5,sticky="nsew")

ComentariosEntry.config(yscrollcommand=scrollComentarios.set)

""" ---------------- Buttons line  -------------"""

ButtonCreate = Button(miFrame, text= "Create", width= 6, command=create)
ButtonCreate.grid(row = 7, column = 1, padx= 10, pady=10, columnspan= 1)

ButtonRead = Button(miFrame, text= "Read", width= 6, command=read)
ButtonRead.grid(row = 7, column = 2, padx= 10, pady=10, columnspan=1)

ButtonUpdate = Button(miFrame, text= "Update", width= 6,command=update)
ButtonUpdate.grid(row = 7, column = 3, padx= 10, pady=10, columnspan= 1)

ButtonDelete = Button(miFrame, text= "Delete", width= 6, command=delete)
ButtonDelete.grid(row = 7, column = 4, padx= 10, pady=10, columnspan= 1)

raiz.mainloop()