class Coche():
    #Método constructor que especifica el estado inicial de cada instanciación
    def __init__(self):

        self.__largoChasis=250 #Se encapsula la propiedad para que no se pueda modificar desde fuera de la clase.
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar(self, estado_arranque):
        self.__enmarcha= estado_arranque

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche está en marcha"
        elif(self.__enmarcha and chequeo == False):
            return "Algo ha ido mal en el chequeo, no podemos arrancar"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, "y un largo de",
        self.__largoChasis)
    
    def __chequeo_interno(self): #Encapsulamos el metodo chequeo_interno porque no tiene sentido que pueda ser invocado desde fuera de la clase por el usuario, su finalidad radica en que pueda ser invocado sólo por otro método que reside en la definición de la clase.
        print("realizando chequeo interno")
        self.gasolina="mal"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

miCoche=Coche()
print(miCoche.arrancar(True))
print(miCoche.estado())

print("-------------------A continuación creamos el segundo objeto")

miCoche2=Coche()
print(miCoche.arrancar(False))
print(miCoche.estado())
