""" Title: Create, Reed, Update, Detele app
    Author: Guillermo Leon
    website: https://savingl.cl

    To do:
        -GUI
            menubar
"""

from tkinter import *
raiz=Tk()
raiz.title("CRUD App")

miFrame=Frame(raiz)
miFrame.pack()


""" ---------------- Menu Bar  -------------"""

menubar = Menu(raiz)
raiz.config(menu=menubar)


BBDDmenu = Menu(menubar)
BBDDmenu.add_command(label="Connect")
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

ButtonCreate = Button(miFrame, text= "Create", width= 6)
ButtonCreate.grid(row = 7, column = 1, padx= 10, pady=10, columnspan= 1)

ButtonRead = Button(miFrame, text= "Read", width= 6)
ButtonRead.grid(row = 7, column = 2, padx= 10, pady=10, columnspan= 1)

ButtonUpdate = Button(miFrame, text= "Update", width= 6)
ButtonUpdate.grid(row = 7, column = 3, padx= 10, pady=10, columnspan= 1)

ButtonDelete = Button(miFrame, text= "Delete", width= 6)
ButtonDelete.grid(row = 7, column = 4, padx= 10, pady=10, columnspan= 1)






raiz.mainloop()