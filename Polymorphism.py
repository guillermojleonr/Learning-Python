""" 
Debido a que Python es un lenguaje de tipado dinámico no estamos 
obligados a definir de que tipo es un objeto cuando lo instanciamos lo cual
permite cambiar el tipo del objeto instanciado y a su vez cambiar sus propiedades
y métodos.
 """

class Coche():
    def desplazamiento(self):
        print("Me desplazo con 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo con 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo con 6 ruedas")

#En lugar de instanciar y acceder a cada objeto de esta forma
""" miVehiculo=Moto()
miVehiculo.desplazamiento()

miVehiculo=Coche()
miVehiculo.desplazamiento()

miVehiculo=Camion()
miVehiculo.desplazamiento() """

""" 
Mediante una función podemos hacer uso del polimorfismo
Pasarle por parámetro el tipo de objeto que se quiere utilizar
Y de esa forma acceder a los métodos y propiedades de cualquier objeto
El objeto "cambia de forma" al cambiar el parámetro de la función que hace uso de el.
 """

 #Con las dos lineas de código de esta función nos ahorramos muchas que instanciarian a cada objeto que queramos utilizar
def desplazamientoVehiculo(vehiculo): #En python no tenemos que especificar de qué tipo este parámetro, es genérico.
    vehiculo.desplazamiento()

miVehiculo=Camion()

desplazamientoVehiculo(miVehiculo)
