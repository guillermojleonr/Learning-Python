from inspect import isclass


class Persona():
    def __init__(self, nombre, edad, Lugar_residencia): #3. para finalmente ser inputeados aca
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=Lugar_residencia

    def descripcion(self):
        print("Nombre: ", self.nombre, " Edad: ", self.edad, " Residencia: ", self.lugar_residencia)

class Empleado(Persona):

    def __init__ (self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado): #1. parámetros introducidos acá
            
        #La función super llama al método de la clase padre, si queremos que
        #en una instancia de una clase hija pueda mostrar las propiedades dadas por el constructor
        #de la clase padre debemos referenciar con la función super al constructor de la clase padre
        #y obviamente pasarle los parámetros que requiera ese método constructor.

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)  #2. viajan acá
        self.salario=salario
        self.antiguedad=antiguedad
    
    def descripcion(self):
        super().descripcion() #Ejecuta la función descripción de la clase padre para que sea printeado su contenido junto con la siguiente declaración
        
        print("Salario: ", self.salario, "Antiguedad: ", self.antiguedad) #Printea las otras dos propiedades restantes

#Le paso los 5 parámetros definidos en el constructor de la clase empleado, los 
#Este constructor tuvo que adecuarse para recibir 6 parámetros: los tres del
#constructor de la clase padre más 2 propios de la clase hija

Antonio=Empleado(1500, 55, "Antonio", 28, "Venezuela") 
Antonio.descripcion() #Por sobrescritura este método llamará al método descripción perteneciente a su propia clase a pesar que también la clase padre tenga un método con el mismo nombre

#Principio de sustitución: cuando hay herencia un objeto de la subclase siempre será un objeto de la superclase.
#Se puede comprobar la pertenencia de un objeto a una clase determinada con la siguiente instrucción

print(isinstance(Antonio, Empleado)) #Devuelve true

print(isinstance(Antonio, Persona)) #Devuelve true porque el objeto perteneciente a la subclase por herencia es también perteneciente a la superclase