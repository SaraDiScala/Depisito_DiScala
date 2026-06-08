numero = 10 

# -----------------     IF  --------------------------------------
if numero > 0:                           #Controllo del flusso - se è True entra nel flusso ed esegue il blocco sotto
    print("Il numero è positivo")        #è True quindi esegue il codice


#----------------- IF - ELSE  ---------------------------------- 
if numero > 0:                           #Controllo del flusso - se è True entra nel flusso ed esegue il blocco sotto
    print("Il numero è positivo")        #è True quindi esegue il codice
else:
    print("Il numero non è positivo")    #La condizione è Falsde e quindi esegue il blocco alternativo
    
#-----------------  IF - ELIF - ELSE ---------------------------------- 
if numero > 0:                           
    print("Il numero è positivo") 
    if numero == 100:                  #Verificata la condizione precedente, controlla una seconda condizione
        print("Wow")  
elif numero < 0:                       #Condizione alternativa al 1 if
    print("Il numero è negativo")     
else:
    print("Il numero è zero") 
    

#----------------------------------   ESERCIZI FLUSSO IF ---------------------------------- 

# ------ 1 ------

var_numero = int(input("Inserici numero da 1 a 3: "))

if var_numero == 3:
    print("Numero primo")
if var_numero == 2:
    print("Numero divisibile per se stesso")
if var_numero == 1:
    print("Numero semplice")


# ------ 2 ------
lista_colori = ["rosa","verde","marrone"]
var_colore = input("Inserici un colore: ")

if var_colore == "bianco":
    print("Colore neutro")
    lista_colori.append(var_colore)
    print(lista_colori)
elif var_colore == "nero":
    print("Colore scuro")
    lista_colori.append(var_colore)
    print(lista_colori)
elif var_colore == "rosso":
    print("Colore acceso")
    lista_colori.append(var_colore)
    print(lista_colori)
elif var_colore == "giallo":
    print("Colore brillante")
    lista_colori.append(var_colore)
    print(lista_colori)
else:
    print("Colore non presente nella lista")
    lista_colori.remove(var_colore)
    print(lista_colori)


# ------ 3 ------

utente = input("Hai un account?: ")    #Input all'utente
id_utente = 0                          #Variabile id parte da 0
dati_utente = []                       #Lista vuota da popolare

if utente == "no":                        #Se è true entro nel flusso
    print("Creazione account")
    nome = input("Inserire nome: ")         #Richiesta dati all'utente
    psw = input("Inserire password: ")
    id_utente += 1                                   #Icremento la variabile id
    dati_utente.append([nome,psw,id_utente])        #Popolo la lista coi dati fortniti 
    print(f"Benvenuto {nome}! Il tuo account è stato creato. Questi sono i tuoi dati: {dati_utente}") #F print
else:
    print("Registrati")                          #Alternativa se False

# -------------------------------------------------------------------------------------------------------


#-------------------------------- MATCH ---------------------------------------------------
comando = input("Inserisci comando: ")

match comando:                                        #Cerca i casi associati
    case "start":
        print("Avvio del programma")
    case "stop":
        print("Chiusura del programma")
    case "pausa":
        print("Programma in pausa")
    case _:
        print("Comando non riconosciuto")       # Il trattino rappresenta il Default


#-------------------------------- ESERCIZIO MATCH ---------------------------------------------------

# ------ 1 ------
eta = int(input("Inserisci la tua eta: "))

match eta: 
    case 18:                                          #Inserire if eta > 18 peer renderla funzionale
        print("Puoi accedere ai contenuti")
    case 18:
        print("Mi dispiace, non puoi vedere questo film")
    case _:
        print("Errore inserimento")
        
# ------ 2 ------
n1 = int(input("Inserisci un numero: "))
n2 = int(input("Inserisci altro numero: "))

operazione = input("Quale operazione vuoi eseguire? ")

match operazione:
    case "+":
        risultato = n1+n2
    case "-":
        risultato = n1-n2
    case "/":
        if n2 == 0:      #Controllo prima che il secondo numero sia 0 o diverso 
            risultato = "Errore: Divisione per zero"
        else:
            risultato = n1 / n2
    case "*":
        risultato = n1*n2
    case _:
        risultato = "operazione non valida"

print(f"Il risulatato della tua operazione è {risultato}")

