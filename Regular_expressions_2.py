# Metacharacters
import re


lista_nombres = [
    'Ana Gomez',
    'María Martín',
    'Sandra López',
    'Santiago Martín',
    'Sandra Fernandez'
    ]

for elemento in lista_nombres:
    if re.findall('^Sandra', elemento): #starting with 'Sandra'
        print(elemento)

for elemento in lista_nombres:
    if re.findall('Martín', elemento): #ending with 'Martín'
        print(elemento)

#Usefull to search URL's, domains

lista_nombres = [
    'http://pildorasinformaticas.es',
    'ftp://pildorasinformaticas.es',
    'http://pildorasinformaticas.com',
    'ftp://pildorasinformaticas.com'
    ]

for elemento in lista_nombres:
    if re.findall('^ftp', elemento):
        print(elemento)

for elemento in lista_nombres:
    if re.findall('.com$', elemento):
        print(elemento)

lista_nombres = [
    'http://informaticaenespaña.es',
    'ftp://pildorasinformaticas.es',
    'http://pildorasinformaticas.com',
    'ftp://pildorasinformaticas.com'
    ]

for elemento in lista_nombres:
    if re.findall('[ñ]', elemento): #finds the occurence with ñ
        print(elemento)

lista_nombres = [
    'hombres',
    'mujeres',
    'niños',
    'niñas'
    ]

for elemento in lista_nombres:
    if re.findall('niñ[oa]s', elemento): #searchs for an occurence switching letters
        print(elemento)


lista_nombres = [
    'Ana',
    'Pedro',
    'María',
    'Rosa',
    'Sandra',
    'Celia'
    ]
for elemento in lista_nombres:
    if re.findall('[o-t]', elemento): #searchs for an occurence switching letters
        print(elemento)

for elemento in lista_nombres:
    if re.findall('^[O-T]', elemento): #it's case sensitive
        print(elemento)

lista_nombres = [
    'Ma1',
    'Se1',
    'Ma2',
    'Ba1',
    'Ma3',
    'Va1',
    'Va2',
    'Ma4',
    'MaA',
    'MaB',
    'MaC'
    ]

for elemento in lista_nombres:
    if re.findall('Ma[0-3]', elemento): #number ranges
        print(elemento)

for elemento in lista_nombres:
    if re.findall('Ma[^0-3]', elemento): #negated range, finds the opposite.
        print(elemento)

for elemento in lista_nombres:
    if re.findall('Ma[0-3A-B]', elemento): # number ranges and letter ranges at the same time
        print(elemento)

for elemento in lista_nombres:
    if re.findall('.:]', elemento): #special characters
        print(elemento)