from tkinter import *
root=Tk()
miFrame=Frame(width="1200", height="600")
miFrame.pack()

minombre=StringVar()

cuadroemail=(Entry(miFrame,textvariable=minombre))
cuadroemail.grid(row=0,column=1, padx=10, pady=10)
cuadroemail.config(fg="red", justify="right")

cuadropass=(Entry(miFrame))
cuadropass.grid(row=1,column=1, padx=10, pady=10)
cuadropass.config(show="*") #password

textoComentario=Text(miFrame,width=16,height=5)
textoComentario.grid(row=4,column=1,padx=10,pady=10)

scrollVert=Scrollbar(miFrame,command=textoComentario.yview) #yview = scrollbaer vertical
scrollVert.grid(row=4,column=2,sticky="nsew") #nsew hace que el scroll bar se ajustea al widget al que pertenece

textoComentario.config(yscrollcommand=scrollVert.set) #Scrollbar se ajusta según texto escrito
labelEmail=Label(miFrame,text="Email")
labelEmail.grid(row=0,column=0, sticky="e", padx=10, pady=10)

labelPass=Label(miFrame,text="Contraseña")
labelPass.grid(row=1,column=0, sticky="e", padx=10, pady=10)

def codigoBoton():
    minombre.set("Guillermo")

botonEnvio=Button(root, text="Enviar", command=codigoBoton)
botonEnvio.pack()


root.mainloop()