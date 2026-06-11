#------------------------- COLLEZIONI -----------------------
#------------------------ TUPLE ----------------------------------

punto = (3, 4) # tupla
colore_rgb = (255,128,0)
informazioni_persona = ("Alice",25,"Femmina")


#-------------------- ACCEDERER AGLI ELEMENTI CON INDICI ------------------
punto = (3,4)
print(punto[0]) # 3
print(punto[1]) # 4


#-----------------------------------------------
punto = 3,4
x,y = punto
print(x) # 3    
print(punto) # (3, 4)


set1 = set([1, 2, 3,4,5])
set2 = set([4, 5, 6,7,8])
#------------------ OPERAZIONI SUI SET ----------------------
print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) # {4, 5} 
print(set1.difference(set2)) # {1, 2, 3}
print(set1.symmetric_difference(set2)) # {1, 2, 3, 6, 7, 8}

#------------------- DIZIONARI ----------------------
studente = {
    "nome": "Alice",
    "età": 20,
    "sesso": "Femmina"
}
print(studente["nome"]) # Alice
print(studente["età"]) # 20
print(studente["sesso"]) # Femmina
studente["corso"] = "Matematica"
print(studente) # {'nome': 'Alice', 'età': 20, 'sesso': 'Femmina', 'corso': 'Matematica'}

studente["età"] = 21
print(studente) # {'nome': 'Alice', 'età': 21, 'sesso': 'Femmina', 'corso': 'Matematica'}

studente["città"] = "Roma"    #Se c'è cambia il valore, se non c'è lo aggiunge
print(studente) # {'nome': 'Alice', 'età': 21, 'sesso': 'Femmina', 'corso': 'Matematica', 'città': 'Roma'}

#------------------ METODO ---------------------
print(studente.keys()) # dict_keys(['nome', 'età', 'sesso', 'corso', 'città'])
print(studente.values()) # dict_values(['Alice', 21, 'Femmina',
# 'Matematica', 'Roma'])
print(studente.items()) # dict_items([('nome', 'Alice'), ('età', 21), ('sesso', 'Femmina'), ('corso', 'Matematica'), ('città', 'Roma')])

#------------------ CICLO FOR SUI DIZIONARI ----------------------
for x,y in studente.items():    ##cicla su ogni coppia chiave-valore del dizionario, assegnando la chiave a x e il valore a y
    print(x,y)
