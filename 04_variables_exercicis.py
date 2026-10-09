###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom_encaminador= "Router casa"
ubicacio="Habitació"
ports= 3
ences= bool=True

print(f"Nom encaminador: {nom_encaminador}. Ubicació: {ubicacio}. Nombre de ports: {ports}. Esta encès?: {ences}")

# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
gb_pla= 20
gb_consumits= 10
print(f"Et queden: {gb_pla - gb_consumits} GB")
gb_consumits = 5
print(f"Et queden: {gb_pla - gb_consumits} GB")