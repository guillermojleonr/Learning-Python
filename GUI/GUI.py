from tkinter import *
raiz = Tk()
raiz.title("Titulo ventana")
#raiz.resizable(True,False) #impide que se redimensione una ventana
raiz.iconbitmap() #Cambia icono ventana
raiz.geometry("650x350") #dimensiones de la ventana
raiz.config(bg ="blue") #permite cambiar fondo entre otras cosas

miFrame = Frame() #widget organizador de otros widgets
miFrame.pack(side="right",anchor="n",fill="x") #empaqueta el frame dentro de la raiz y se le pasan otras configuraciones. Fill y Expand permite redimensionar el frame junto con la raiz, frame.pack() ayuda a que los widgets de una GUI se ubiquen, pero deshabilita las dimensiones que se prefijaron a la ventana
miFrame.config(bg="red")
miFrame.config(width="650", height="350") #El tamaño de la raiz se adapta al tamaño del frame y no alrevez.
miFrame.config(relief="groove") #establece un borde
miFrame.config(cursor="pirate") #cambia la forma del cursor

raiz.mainloop() #Debe estar siempre a la escucha en un bucle infinito

#Guardando el archivo con extensión .pyw evita que se abra la consola detrás de la ventana

#Metodo grid() convierte en una grilla la ventana donde ubicar widgets, pady y padx ayudan a separar los elementos unos de otros, sticky (alineación)