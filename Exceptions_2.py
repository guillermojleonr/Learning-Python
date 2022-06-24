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
    
divide()

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
