class Coche():
    #Propiedades de la clase
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False

    #Metodos de la clase 
    def arrancar(self):
        self.enmarcha=True

    #Parametro self hace referencia a la instancia del mismo objeto
    #es un parámetro obligatorio. Al ejecutar el método recibirá por
    #parámetro a la instanciación del mismo objeto.

    def estado(self):
        if(self.enmarcha): #Si no se coloca True o False se sobreentiende True
            return "el coche está en marcha"
        else:
            return "El coche está parado"

#Instanciar una clase (crear un objeto)
miCoche=Coche()

print("El largo del coche es:",miCoche.anchoChasis)
print("El coche tiene ", miCoche.ruedas, " ruedas")
miCoche.arrancar()
print(miCoche.estado())

print("-------------------A continuación creamos el segundo objeto")

miCoche2=Coche()
print("El largo del coche es:",miCoche.anchoChasis)
print("El coche tiene ", miCoche.ruedas, " ruedas")
print(miCoche.estado())
