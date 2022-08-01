#Upper order functions, allows to do functional programming

#Checks if all the elements of a secuencie match with a condition if do returns only the matching elements.

""" def numero_par(num):
    if num % 2 == 0:
        return True

numeros = [17,24,7,39,8,51,92] 

print(list(filter(numero_par,numeros))) """

#Example with lambda function

""" print(list(filter(lambda numero_par_argument:numero_par_argument%2==0,numeros)))
"""

class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre,self.cargo,self.salario)