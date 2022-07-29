""" Title: Create, Reed, Update, Detele app
    Author: Guillermo Leon
    website: https://savingl.cl

    To do:
"""

from tkinter import *
import sqlite3

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

def read():
    global myCursor

    id_value = IdEntry.get()

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

def update():
    global myCursor, myConnection
    #We need to create a tuple that contains the field name and the field value, this is the tuple that we are going to iterate in the executemany method.

    myCursor.execute("UPDATE usuarios SET nombre = ? WHERE id = ?",id_value)

    




""" ---------------- Menu Bar  -------------"""

menubar = Menu(raiz)
raiz.config(menu=menubar)


BBDDmenu = Menu(menubar)
BBDDmenu.add_command(label="Connect", command=connect)
BBDDmenu.add_command(label="Exit", command=raiz.quit)

Borrarmenu = Menu(menubar)
Borrarmenu.add_command(label="Clear fields")

CRUDmenu = Menu(menubar)

CRUDmenu.add_command(label="Create")
CRUDmenu.add_command(label="Read")
CRUDmenu.add_command(label="Update")
CRUDmenu.add_command(label="Delete")

Ayudamenu = Menu(menubar)
Ayudamenu.add_command(label="About CRUD App")


menubar.add_cascade(label="BBDD", menu=BBDDmenu)
menubar.add_cascade(label="Borrar", menu=Borrarmenu)
menubar.add_cascade(label="CRUD", menu=CRUDmenu)
menubar.add_cascade(label="Ayuda", menu=Ayudamenu)


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

ButtonUpdate = Button(miFrame, text= "Update", width= 6)
ButtonUpdate.grid(row = 7, column = 3, padx= 10, pady=10, columnspan= 1)

ButtonDelete = Button(miFrame, text= "Delete", width= 6)
ButtonDelete.grid(row = 7, column = 4, padx= 10, pady=10, columnspan= 1)

raiz.mainloop()