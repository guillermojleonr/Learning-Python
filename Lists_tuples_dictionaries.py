# Listas, arrays, vectores. 

# Permiten almacenar valores de distintos tipos
# Se pueden expandir dinamicamente 

""" 
lista1 = [7.5,2,"sandra",4,True]

print(lista1[2]) #acceder a un único elemento
print(lista1[0:3]) #acceder a una porción
print(lista1[:3]) #acceder desde el primero hasta el índice seleccionado
print(lista1[2:]) #acceder desde el seleccionado hasta el último.

lista1.append(6) #agrega elemento al final
print(lista1)

lista1.insert(2,7) #agrega elemento en el índice seleccionado
print(lista1)

lista1.extend([30,23]) #agrega varios elementos (concatenar)
print(lista1)

print(lista1.index(23)) # índice de un elemento (primero que encuentre)

print(23 in lista1) #elemento en lista

lista1.remove(23) #remover elemento
print(lista1)

lista1.pop #elimina último elemento

lista2 = ["lopez", "perez"]
lista3 = lista1 + lista2 #concatenar listas
print(lista3) 

"""

# Tuplas 
# 
# listas inmutables, al extraer porción, se crea una tupla nueva, permiten comprobar
# sus elementos. Son más rápidas, ocupan menos espacio, formatean strings,
# pueden utilizarse como claves de diccionario.

""" 
miTupla = (1,2,3) #crear una tupla = empaquetado de tupla

miLista = list(miTupla) #convertir tupla en lista
print(miLista)

miLista = tuple(miTupla) #convertir lista en tupla

miTupla.count(3) #contar repeticiones de un elemento

len(miTupla) #longitud de tupla

miTupla2 = ("juan",) #tupla unitaria (un sólo elemento)

miTupla3 = ("guillermo", 1,12,1993)
nombre, dia, mes, agno = miTupla3 #desempaquetado de tupla, asignar valores de tupla a variables
print(nombre)
"""

# Diccionarios
#  # Almacena datos, listas, o otros diccionarios en formato "clave":"valor"
# Los elementos no están ordenados porque existe una clave única por cada valor

""" 
miDiccionario = {"Alemania":"Berlin", "Francia":"Paris", "España":"Madrid"}
print(miDiccionario["Francia"]) #Imprime un valor: proporciona clave, obtén valor

miDiccionario["Italia"]="Lisboa" #agrega elemento a diccionario
print(miDiccionario)

miDiccionario["Italia"]="Roma" #al sobreescribir elemento se reemplaza
print(miDiccionario)

del miDiccionario["Francia"] #Elimina elemento
print(miDiccionario)

miDiccionario2 = {"Alemania":"Berlin", 23:"Italia", "España":54} #Admiten claves de tipo string y numérico

miTupla = (1,2,3)
miDiccionario3 = {miTupla[0]:"Madrid",miTupla[1]:"Paris",miTupla[2]:"Roma"} #Admite valores de tupla como clave
print(miDiccionario3)

miDiccionario4 = {"Alemania":"Berlin", 23:"Italia", "España":[1991,1992,1993]} #Admite tuplas, listas y otros diccionarios como valores

print(miDiccionario.keys()) # sólo las claves
print(miDiccionario.values()) #sólo los valores

print(len(miDiccionario)) #longitud de un diccionario 
"""