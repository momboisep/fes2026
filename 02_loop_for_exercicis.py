###
# EXERCICIS (for)
###

# Exercici 1: Imprimir números parells
# Imprimeix tots els números parells del 2 al 20 (inclosos) fent servir un bucle for.
numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for parells in numeros:
    if parells%2==0:
        print(parells)

# Exercici 2: Calcular la mitjana d'una llista
# Donada la llista de números següent:
# numeros = [10, 20, 30, 40, 50]
# Calcula la mitjana dels números fent servir un bucle for.
numeros = [10, 20, 30, 40, 50]
suma=0
for numero in numeros:
    suma= suma+numero
mitjana=suma/len(numeros)
print(mitjana)

# Exercici 3: Buscar el màxim d'una llista
# Donada la llista de números següent:
# numeros = [15, 5, 25, 10, 20]
# Troba el número màxim de la llista fent servir un bucle for.
numeros = [15, 5, 25, 10, 20]
maxim=0
for numero in numeros:
    if numero > maxim:
        maxim=numero
print(f"El maxim es {maxim}")

# Exercici 4: Filtrar cadenes per longitud
# Donada la llista de paraules següent:
# paraules = ["casa", "arbre", "sol", "elefant", "lluna"]
# Crea una llista nova que contingui només les paraules amb més de 5 lletres
# fent servir un bucle for i list comprehension.
paraules=["casa", "arbre", "sol", "elefant", "lluna"]
longitud=5
llista=[]
for paraula in paraules:
    if len(paraula)>= longitud:
        llista=[paraula]+llista

print(f"Llista paraules amb més de 5 lletres: {llista}")

# Exercici 5: Comptar paraules que comencen per una lletra
# Donada la llista de paraules següent:
# paraules = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
# Demana a l'usuari que introdueixi una lletra.
# Compta quantes paraules de la llista comencen per aquesta lletra (sense diferenciar majúscules/minúscules).
paraules=["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
lletra= input("Introdueix una lletra: ")
comptador=0
for paraula in paraules:
    if paraula.lower().startswith(lletra):
        comptador+=1
print(f"Hi ha {comptador} paraules que comencen amb {lletra}")

# Exercici 6: Mesures de tensió d'un sensor
# Durant una prova s'han registrat les tensions següents (en volts):
# tensions = [4.8, 5.0, 5.1, 4.9, 5.2]
# Fent servir un bucle for, calcula la tensió mitjana i imprimeix-la.
tensions=[4.8,5.0,5.1,4.9,5.2]
mitjana=0
suma=0
for tensio in tensions:
    suma+=tensio
mitjana=suma/len(tensions)
print(f"La mitjana es {mitjana}")

# Exercici 7: Corrent en resistències
# En un circuit s'aplica una tensió de 12 V a aquestes resistències:
# resistencies = [100, 220, 470, 1000]
# Fent servir la llei d'Ohm (I = V / R) i un bucle for, calcula i imprimeix
# el corrent que circula per cada resistència, en ampers.
resistencies=[100,220,470,1000]
intensitats=[]
for resistencia in resistencies:
    intensitat=resistencia/12
    intensitats=[intensitat]+intensitats
print(f"Les intensitats de cada resistencia són: {intensitats}")

# Exercici 8: Mostres que superen el llindar de soroll
# Un receptor ha mesurat aquests nivells de soroll (en dBm):
# nivells_soroll = [-92, -85, -78, -95, -81, -88]
# Compta, amb un bucle for, quantes mostres superen el llindar de -80 dBm
# (és a dir, tenen un valor més gran que -80) i imprimeix el resultat.
nivells_soroll=[-92,-85,-78,-95,-81,-88]
comptador=0
for nivell_soroll in nivells_soroll:
    if nivell_soroll >= -80:
        comptador+=1
print(f"Superen el llindar de -80 dBm {comptador} nivells de soroll ")

# Exercici 9: Càlcul de la taxa d'error de bits
# Compara els bits transmesos i rebuts:
# bits_transmesos = [1, 0, 1, 1, 0, 0, 1, 0]
# bits_rebuts =     [1, 0, 0, 1, 0, 1, 1, 0]
# Fent servir un bucle for i els índexs de les llistes, compta quants bits
# són diferents. Calcula i imprimeix la taxa d'error (bits diferents / total de bits).
bits_transmesos = [1, 0, 1, 1, 0, 0, 1, 0]
bits_rebuts = [1, 0, 0, 1, 0, 1, 1, 0]
bits_diferents=0
index_1=0
index_2=0
for bit_transmes in bits_transmesos:
    index_1+=1
    for bit_rebut in bits_rebuts:
        index_2+=1
        if bit_transmes!= bit_rebut:
            bits_diferents+=1
total_bits= index_1+index_2
taxa_error=bits_diferents/total_bits
print(f"La taxa d'error és {taxa_error}")

# Exercici 10: Període d'un senyal
# Donades les freqüències següents, en hertzs:
# frequencies = [50, 100, 500, 1000]
# Fent servir un bucle for, calcula el període de cada senyal amb la fórmula
# T = 1 / f i imprimeix cada freqüència amb el seu període en segons.
frequencies = [50, 100, 500, 1000]
periodes=[]
for frecuencia in frequencies:
    periode=1/frecuencia
    periodes= [periode]+periodes
print(f"Els periodes de cada frecuencia són: {periodes}")