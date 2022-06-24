
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