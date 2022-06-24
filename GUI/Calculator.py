from tkinter import *
raiz=Tk()
miFrame=Frame(raiz)
miFrame.pack()

habilitaNuevoIngresoDeNumero = False
resultado = 0
numeroPantalla = StringVar()
signoNegativoSeleccionado = False
operacion = ""

def selectnum(num):
    global operacion, habilitaNuevoIngresoDeNumero
    if habilitaNuevoIngresoDeNumero == True:
        numeroPantalla.set(num)
        habilitaNuevoIngresoDeNumero = False
    else:
        numeroPantalla.set(numeroPantalla.get() + num) #concatena num pantalla con más numeros introducidos

def borrar():
    global resultado, operacion, habilitaNuevoIngresoDeNumero

    numeroPantalla.set('')
    resultado = 0
    operacion = ""
    habilitaNuevoIngresoDeNumero = True

def suma(num):
    global operacion, resultado, habilitaNuevoIngresoDeNumero

    habilitaNuevoIngresoDeNumero = True

    if operacion != "suma":
        totalizacion()
    if operacion == "suma":
        resultado += float(num)
        numeroPantalla.set(str(resultado))

    operacion = "suma"
    print(operacion)

def resta(num):
    global operacion, resultado, signoNegativoSeleccionado, habilitaNuevoIngresoDeNumero 
    
    signoNegativoSeleccionado = True
    habilitaNuevoIngresoDeNumero = True

    if operacion != "resta":
        totalizacion()
    if operacion == "resta":
        resultado -= float(num)
        numeroPantalla.set(str(resultado))
    
    operacion = "resta"
    print(operacion)

def totalizacion(str="regularBehaviour"):
    global resultado
    global operacion

    if operacion == "":
        resultado = float(numeroPantalla.get())
    elif operacion == "suma":
        numeroPantalla.set(resultado+float(numeroPantalla.get()))
        resultado == float(numeroPantalla.get())
        print(resultado)
    elif operacion == "resta":
        numeroPantalla.set(resultado-float(numeroPantalla.get()))
        resultado == float(numeroPantalla.get()) #el problema actual está aquí, esta variable no se actualiza no sé por qué, al parecer la instrucción de arriba se tarda en ejecutarse y por ende
        print(resultado)
    
    if str == "=":
        resultado = 0 #resetea resultado cuando se llama a totalización desde el boton "="
    

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
botonIgual=Button(miFrame,text="=", width=3, command=lambda:totalizacion("="))
botonIgual.grid(row=5, column=3)
botonSum=Button(miFrame,text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5, column=4)

"""---------------- fila 5 ----------------------"""
botonBorrar=Button(miFrame,text="C", width=3, command=borrar)
botonBorrar.grid(row=6, column=1,)

raiz.mainloop()


""" if resultado != 0:
    numeroPantalla.set(resultado-float(numeroPantalla.get()))
    resultado = float(numeroPantalla.get())
else:
    resultado = float(num) """

""" if operacion == "resta":
    resultado = variableRestaTemporal-float(numeroPantalla.get())
    numeroPantalla.set(float(resultado))
else:
    resultado = float(num) #El problema actual está aquí, a resultado se le hace un decremento automático 
    numeroPantalla.set(float(resultado)) """