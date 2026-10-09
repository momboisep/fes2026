###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
tecnic= input("Posa el nom d'un tècnic: ")
xarxa= input("Posa el nom de la xarxa: ")
print(f"El nom del tècnic és {tecnic} i el nom de la xarxa {xarxa}")

# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
longitud=input("Posa la longitud d'un enllaç de fibra en quilòmetres: ")
velocitat=input("Posa la velocitat de transmissió en Gbps: ")
segons= 8/float(velocitat)
print(f"La longitud és de {longitud}km i caldrien {segons} segons per transmetre 1GB")

# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores_feina=float(input("Posa el nombre d'hores de feina: "))
preu= float(input("Posa el preu per hora d'una instal·lació de xarxa: "))
preu_material= float(input("Posa el preu material: "))
cost= hores_feina*preu + preu_material
print(f"El cost total és {cost}")