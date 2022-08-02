# A Regex is a character secuence representing a search pattern. Generally used in text processing.

# We are going to use some methods of the re object
import re

cadena="Vamos a aprender expresiones regulares"
textoBuscar= "aprender"

#search receives two strings, returns an object.
#search finds a string from anyplace in the search string
print(re.search("aprender",cadena)) 
if re.search(textoBuscar,cadena) is not None:
    print("Texto encontrado")
else:
    print("Texto no encontrado")

textoEncontrado=re.search(textoBuscar,cadena)

print(textoEncontrado.start()) #returns the position of the starting character of the founded string
print(textoEncontrado.end()) #returns the position of the end character
print(textoEncontrado.span()) #.start() and .end() together.

cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"
textoBuscar = 'Python'

#findall returns a list with each occurence of the searched string
print(re.findall(textoBuscar,cadena))

#the lenght of this list can show how many occurences are.
print(len(re.findall(textoBuscar,cadena)))


