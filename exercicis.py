###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

from xml.etree.ElementTree import PI


print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

### Completa aquí

print("Patricia")
print("Sabadell")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print("type (a):", type(a))
print("type (b):", type(b))
print("type (c):", type(c))
print("type (d):", type(d))
print("type (e):", type(e))

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

### Completa aquí

a="12345"
print("type(a):", type(int((a))))
print("type(a):", type(float(a)))

b=float(3.99)
print("type(b):", type(int(b)))
print(int(b))
#Al convertir un float a un enter el sistema fa troncament

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 38 anys i faig 1.75 metres"
#name = "Marc"
#age = 38

### Completa aquí
nom= "Patricia"
edat= 19
alçada= 1.67
print(f"Hola! Em dic {nom}, tinc {edat} anys i faig {alçada} metres")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

import math
pi=math.pi
pi_redondeat= round(pi)
resultat= pi_redondeat//2
print(f"Resultat: {resultat}")

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

### Completa aquí

temp=input("Posa una temperatura en graus Celsius:")
c= float(temp)
f= (c * 9/5) + 32
print(f"La temperatura en Fahrenheit és: {f}")


print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

### Completa aquí

total,percentatge=input("Quin és el total del compte i el percentatge de propina?:").split()
propina = float(total) * float (percentatge)/100
resultat_final=float(total)+propina
print(f"La propina és: {propina: .2f}")
print(f"El resultat és: {resultat_final: .2f}")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

### Completa aquí
contrasenya= input("Posa una contrasenya: ")
mesura= len(contrasenya)
if mesura >= 8:
    print("Contrasenya vàlida")
print("Contrasenya no vàlida")