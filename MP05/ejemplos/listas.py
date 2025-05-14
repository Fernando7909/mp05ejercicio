# Definició de punts d'interès
punt1 = ("Plaça Catalunya", (41.387, 2.169))
punt2 = ("Sagrada Família", (41.403, 2.174))
punt3 = ("Parc Güell", (41.414, 2.152))
punt4 = ("Mataró", (42.236, 2.147))

# Llista de punts
punts_interes = [punt1, punt2, punt3]
punts_interes.insert(0, punt4)

# Mostra els punts
for nom, coordenades in punts_interes:
    print(f"{nom} està situat a les coordenades {coordenades}.")
