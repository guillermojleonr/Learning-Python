import math

def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
# Bloque try/except realiza la captura del error y continúa la ejecucion.
    try: 
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    return "Operacion erronea"

def divide():
    try:
        op1=(float(input("Introduce el primer numero")))
        op2=(float(input("Introduce el segundo numero")))
        print("La division es: " + str(op1/op2))
    #Se pueden capturar varias excepciones consecutivas
    except ValueError:
        print("El valor introducido es erroneo")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")

    """ #Permite capturar todas las excepciones
    except: 

        print("Ha ocurrido un error general")
        
    #Permite ejecutar un bloque sin importar que hayan excepciones o no.
    finally:
        print("Esta linea se ejecutara siempre") """


def evaluaEdad(edad):
    if edad<0:
        #Levanta una excepción TypeError de forma intencionada si se
        #si se cumple la condición. No sirve para excepciones personalizadas
        #sólo para excepciones que ya existan.
        raise TypeError("No se permiten edades negativas")
    
    if edad<20:
        return "eres muy joven"
    elif edad<40:
        return "eres joven"
    elif edad<65:
        return "eres maduro"
    elif edad<100:
        return "Cuidate"


def CalculaRaiz(num1):
    if num1<0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(num1)

# Bucle infinito, si al ejecutar el try hay una excepcion, saltará hacia el except
# si no la hay pasará por el break y saldrá del bucle while.
while True:
    try:
        op1=(int(input("Introduce el primer numero: ")))

        op2=(int(input("Introduce el segundo numero: ")))		
        
        break
    except ValueError:
        print("Los valores indicados no son correctos, introducelos de nuevo")

operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operacion no contemplada")


print("Operacion ejecutada. Continuacion de ejecucion del programa ")

divide()

op1=(int(input("Introduce un numero: ")))
print(CalculaRaiz(op1))