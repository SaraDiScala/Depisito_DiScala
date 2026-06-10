#-------------------- ESERCIZIO RIASSUNTIVO 1 ----------------------

'''  TRACCIA
Sistema che registra in entrata input da parte dell'utente. 
1. Registrazione dati utente       [Lista dati]
2. Ideazione guidata del personaggio [Lista dati] [Flusso]
3.Percorso guidato al raggiungimento dello stemma finale [Lista dati] [Cicli] [Funzione?]
'''

#--------------------------------- REGISTRAZIONE UTENTE ----------------------------------


#------------ FUNZIONE CREA UTENTE ----------------------------------------
def crea_utente():
    while True:
        nome = input("Inserisci il tuo nome: ")
        if nome == "":
            print("Campo obbligatorio!")
            continue
        username = input("Inserisci il tuo username: ")
        if username == "":
            print("Campo obbligatorio!")
            continue
        eta = int(input("Inerisci la tua eta: "))
        if eta == "":
            print("Campo obbligatorio!")
            continue
        citta = input("Inserisci la tua citta: ")
    
        utente = [nome,username,eta,citta]
        return utente
    
#---------------------------------------------------------------------------


lista_utenti = []   
id_utenti = 0

while True:
    print("REGISTRAZIONE UTENTE ")
    dati_utente = crea_utente()
    id_utenti += 1
    dati_utente.append(id_utenti)
    lista_utenti.append(dati_utente)

    print("Id creato automaticamente!")
    print(lista_utenti)

    nuovo_utente = input("Vuoi registrare un nuovo utente?: ").lower()

    if nuovo_utente != "si":
        break



#-------------------- IDEAZIONE PERSONAGGIO  -------------------


#------------ FUNZIONE CREA PERSONAGGIO ----------------------------------------

def crea_personaggio():
    print("CREAZIONEPERSONAGGIO")

    while True:
        scelta = input("Uomo: 1 --- Donna: 2 ").strip()   #Elimina eventuali spazi
        if scelta == "1":
            genere = "uomo"
            break
        elif scelta == "2":
            genere = "donna"
            break
        else:
            print("Scelta non valida")
            continue                                      #Riporta sopra

    while True:
        scelta = input("Bambino: 1 --- Adulto:  2 ").strip()
        if scelta == "1":
            fascia_eta = "bambino"
            break
        elif scelta == "2":
            fascia_eta= "adulto"
            break
        else:
            print("Scelta non valida")
            continue                                      

    while True:
        scelta = input("Magro: 1 --- Grasso: 2 ").strip()
        if scelta == "1":
            costituzione = "magro"
            break
        elif scelta == "2":
            costituzione = "grasso"
            break
        else:
            print("Scelta non valida")
            continue                                      

    while True:
        scelta = input("Basso: 1 ---  Alto: 2 ").strip()
        if scelta == "1":
            altezza = "basso"
            break
        elif scelta == "2":
            altezza = "alto"
            break
        else:
            print("Scelta non valida")
            continue                                      

    while True:
        scelta = input("Buono: 1 ---  Cattivo: 2  ").strip()
        if scelta == "1":
            allineamento = "buono"
            break
        elif scelta == "2":
            allineamento = "cattivo"
            break
        else:
            print("Scelta non valida")
            continue                                       

    personaggio = [genere, fascia_eta, costituzione, altezza, allineamento]   #Inserimento dati nella lista 
    return personaggio

# ---------------------------------------------------------------------------


lista_personaggi = []   
id_personaggi = 0

while True:
    print("CREAZIONE GUIDATA DEL PERSONAGGIO")
    
    dati_personaggio = crea_personaggio()
    id_personaggi += 1
    dati_personaggio.append(id_personaggi)
    lista_personaggi.append(dati_personaggio)

    print("Personaggio creato con successo!")
    print("ID assegnato automaticamente!")
    print(lista_personaggi)
    
    nuovo_personaggio = input("Vuoi ideare un nuovo personaggio?: ").lower().strip()
    if nuovo_personaggio != "si":
        break

#-------------------- RAGGIUNGIMENTO STEMMA  -------------------
