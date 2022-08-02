# Match and search functions
import re

nombre1="Sandra López"
nombre2="Antonio Gómez"
nombre3="María Lopez"

if re.match("Sandra",nombre1): #match finds at the begining of the string
    print("nombre encontrado")
else:
    print("nombre no encontrado")

if re.match("Sandra",nombre1,re.IGNORECASE): #ignores case sensitivity
    print("nombre encontrado")
else:
    print("nombre no encontrado")

if re.match(".Ara",nombre1,re.IGNORECASE): #scaping character
    print("nombre encontrado")
else:
    print("nombre no encontrado")

cadena1="Sandra López"
cadena2="555447855"
cadena3="a55877455"

if re.match("\d",cadena2): #match if starts with a digit
    print("cadena encontrada")
else:
    print("cadena no encontrado")