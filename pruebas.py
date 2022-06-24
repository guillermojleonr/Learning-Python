from tkinter import *
raiz=Tk()
miFrame=Frame(raiz)
miFrame.pack()

operacion = ""
ultOperacion = ""
resultado = 0
numeroPantalla = StringVar()
signoNegativoSeleccionado = False

def selectnum(num):
    global operacion
    if operacion != "":
        numeroPantalla.set(num)
        operacion = "" 
    else:
        numeroPantalla.set(numeroPantalla.get() + num) #concatena num pantalla con más numeros introducidos

def borrar():
    global resultado
    global operacion
    global ultOperacion

    numeroPantalla.set('')
    resultado = 0
    operacion = ""
    ultOperacion = ""

def suma(num):
    global operacion
    global resultado
    global ultOperacion
    operacion = "suma"
    ultOperacion = "suma"
    resultado += float(num)
    
    numeroPantalla.set(str(resultado))

def resta(num):
    global operacion, resultado, ultOperacion, signoNegativoSeleccionado 
    if ultOperacion == "resta":
        resultado -= float(num)
    else:
        resultado = float(num)
    
    signoNegativoSeleccionado = True
    operacion = "resta"
    ultOperacion = "resta"

def totalizacion():
    global resultado
    global operacion
    if ultOperacion == "suma":
        numeroPantalla.set(resultado+float(numeroPantalla.get())) 
    elif ultOperacion == "resta":
        numeroPantalla.set(resultado-float(numeroPantalla.get()))
    
    resultado = 0 #resetea resultado para que no siga operando

def comaDecimal():
    if numeroPantalla.get().find('.') >= 0:
        pass
    else:
        numeroPantalla.set(numeroPantalla.get() + '.')


""" ---------------Pantalla ------------------- """
pantalla=Entry(miFrame,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10, columnspan=4)
pantalla.config(bg="black", fg="#03f943", justify="right")

"""---------------- fila 1 ----------------------"""

boton7=Button(miFrame,text="7", width=3, command=lambda:selectnum("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame,text="8", width=3, command=lambda:selectnum("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame,text="9", width=3,  command=lambda:selectnum("9"))
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame,text="/", width=3)
botonDiv.grid(row=2, column=4)

"""---------------- fila 2 ----------------------"""

boton4=Button(miFrame,text="4", width=3, command=lambda:selectnum("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame,text="5", width=3, command=lambda:selectnum("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame,text="6", width=3, command=lambda:selectnum("6"))
boton6.grid(row=3, column=3)
botonMult=Button(miFrame,text="x", width=3)
botonMult.grid(row=3, column=4)

"""---------------- fila 3 ----------------------"""

boton1=Button(miFrame,text="1", width=3, command=lambda:selectnum("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame,text="2", width=3, command=lambda:selectnum("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame,text="3", width=3, command=lambda:selectnum("3"))
boton3.grid(row=4, column=3)
botonRest=Button(miFrame,text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=4, column=4)

"""---------------- fila 4 ----------------------"""

boton0=Button(miFrame,text="0", width=3, command=lambda:selectnum("0"))
boton0.grid(row=5, column=1)
botonComa=Button(miFrame,text=",", width=3, command=comaDecimal)
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame,text="=", width=3, command=lambda:totalizacion())
botonIgual.grid(row=5, column=3)
botonSum=Button(miFrame,text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)

"""---------------- fila 5 ----------------------"""
botonBorrar=Button(miFrame,text="C", width=3, command=borrar)
botonBorrar.grid(row=6, column=1,)

raiz.mainloop()