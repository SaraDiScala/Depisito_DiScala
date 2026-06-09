#----------- ESERCITAZIONE  ------
import random 


def lista_numeri_interi(n):
    for _ in range(n):
        yield random.randint(1,n)   #La lista la crea quando richiamo il metodo    

def somma_pari(p):
    somma_p = 0
    for numero in lista:
        if numero % 2== 0:
            somma_p += 1
    print("La somma dei nuemri pari è: ", somma_p)

def stampa_dispari(d):
    somma_d = 0
    for numero in lista:
        if numero % 3 == 0:
            somma_d += 1
    print("La somma dei numeri dispari è: ", somma_d)
 

def numero_primo(np):
    if np == 1 or np % i == 0:
        print("E' un numero primo")
        return True
    else:
        print("Non è un numero primo")
        return False

def stampa_nprimi(lista):
    for npp in lista:
        if numero_primo(npp):
            print("Lista dei numeri primi: ", npp)


def richiesta_numero():
    while True:
        n = int(input("Inserisci un numero intero positivo n: "))
        if n > 0:
            return n
        else:
            print("Errore: il numero deve essere maggiore di zero! Riprova.")

def controlla_somma_totale(lista):
    somma_totale = sum(lista)
    print(f"La somma di tutti i numeri nella lista è: {somma_totale}")
    
    if numero_primo(somma_totale):
        print("Esito: La somma totale è un NUMERO PRIMO! 👑")
    else:
        print("Esito: La somma totale NON è un numero primo.")


# -------------------------------------------------------------------------

print("Benvenuto nel menu")
print("""  Elenco comandi:
       A - Inserisci numero
       B - Calcola somma dei numeri pari
       C - Stampa numeri pari
       D - Stampa numeri dispari
       E - Controllare se la somma della lista è pari
       """)
scelta = (input("Scegli quale comando eseguire: ")).lower() 

match scelta:
    case A: 
        n = richiesta_numero()
        lista = lista_numeri_interi(n)  #
        print("Ecco la tua lista: ", lista)
    case B: 
        sp = somma_pari(lista)
        print("La somma dei numeri pari è: ", sp)
    case C:
        snp = stampa_nprimi(lista)
        print("Ecco i numeri primi: ", snp)   
    case D:
        sd = stampa_dispari(lista)  
        print("Ecco i numeri dispari: ", sd)
    case E:
       controllo =  controlla_somma_totale(lista)
       print("Controllo la somma: ", controllo)

    case _:
        print("Non hai effettuato alcuna scelta!")
