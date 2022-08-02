""" Ejercicio: Comprobar si un email está bien escrito """

print("Hola, gracias por ejecutarme")
nombre = input("Dime, ¿cuál tu nombre? ")
print("Perfecto ",nombre, "gracias por ejecutarme.")
print("Bien, ¿que hace este programa?, valida direcciones de email para verificar que esté escrito correctamente: ")
print("1. Si escribes un email con más de 1 '@', por ejemplo 'email@@dominio.com'\n2. Si escribes un email con más de un '.' en el dominio, por ej: email@dominio..com")
print("3. Si colocas la arroba en un lugar incorrecto, por ej: '@tuemail' o 'tuemail@'")
print("Si incurres en alguna de éstas faltas recibirás un error y estarás obligado/a a reintentar hasta escribir uno correcto. Sin más preámbulo:")

countArroba = 0
countDot = 0
arrobaLocationValidation = 0
emailvalidator = 0

while emailvalidator == 0:

    email = input ("Introduce tu email ")

    # El email debe tener una sola arroba: recorremos el string buscándola y debe ser una sola
    for i in email:
        if i == "@":
            countArroba += 1

    #Verifica que la posición de la @ sea correcta

    if email.find('@') > 0 and email.find('@') < len(email) - 1:
        arrobaLocationValidation = 0
    else: 
        arrobaLocationValidation = 1

    #Verifica cantidad de '.' en el área del dominio
    dominio = email.rpartition('@')[2]

    for i in dominio:
        if i == '.':
            countDot += 1

    if countArroba > 1 or countDot > 1 or arrobaLocationValidation == 1:
        emailvalidator = 0
        
        print(nombre,"parece que estas cometiendo un error, tu email tiene ", countArroba," arroba, ", countDot, " puntos en el área del dominio y la arroba puede que no esté en el lugar correcto")
        
        countArroba = 0
        countDot = 0
        arrobaLocationValidation = 0
    else:
        print("Muy bien", nombre, "te mereces un premio, has escrito un email válido, ¿quieres intentarlo otra vez?. ")
        otravez = input(" S/N ")

        if otravez == "S":
            emailvalidator = 0
        else:
            emailvalidator = 1
