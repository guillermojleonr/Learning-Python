#Phases: create, open, manipulate, close

from io import open

#Write on a file
""" archivo_texto=open("archivo.txt", "w") #opens and create the file at the same time
frase ="frase de prueba"
archivo_texto.write(frase) #escribir
archivo_texto.close """

#Read a file
""" archivo_texto=open("archivo.txt", "r")
texto=archivo_texto.read()
archivo_texto.close
print(texto) """

#Read file as a list
""" archivo_texto=open("archivo.txt", "r")
lineas_texto=archivo_texto.readlines()
archivo_texto.close()
print(lineas_texto) """

#Add info to an existing file at the end
""" archivo_texto=open("archivo.txt", "a")
archivo_texto.write("\n nueva linea")
archivo_texto.close()
 """
""" archivo_texto=open("archivo.txt", "r")
nuevo_texto=archivo_texto.read()
archivo_texto.close()
print(lineas_texto)
 """
#Modify pointer position

archivo_texto.seek(0) #move pointer to first position

archivo_texto.seek(len(archivo_texto.read())/2) #move pointer to the middle of a file

archivo_texto.seek(len(archivo_texto.readline())) #move to the end of the first line

# Read-write permission

archivo_texto=open("archivo.txt", "r+")

archivo_texto.writelines(list1) #write a list inside a file