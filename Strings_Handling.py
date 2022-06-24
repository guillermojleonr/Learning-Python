"""
Los strings son objetos por lo tanto  
upper() #todo en mayusculas
lower() #todo en minusculas
capitalize() #capitaliza la primera letra
count() #cuenta cantidad de caracteres
find() #ubica el indice de posición de un caracter
isdigit() #es digito o no
isalum() #es alfanumerico o no
isalpha() #es alfa o no
split() #separa palabras con espacios
strip() #borra espacios sobrantes al principio y al final
replace() #reemplaza un caracter
rfind() #lo mismo que find() pero cuenta desde atrás

http://pyspanishdoc.sourceforge.net/lib/lib.html
 """

nombreUsuario=input("Introduce tu nombre de usuario: ")

print("El nombre es: ", nombreUsuario.upper())
print("El nombre es: ", nombreUsuario.lower())
print("El nombre es: ", nombreUsuario.capitalize())

edad=input("Introduce la edad: ") #todo lo que se introduce en un input es texto

print(int(edad))

