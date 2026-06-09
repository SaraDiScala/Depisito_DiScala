#------------- GENERATORI -----------------
#Genera una serie di valori - yield 

def fibonacci(n):
    a, b = 0, 1
    
    while a < n:
        yield a
        a, b = b, a + b

coll = [*fibonacci(2)]   #Melgio inseirre una lista poichè sono tanti valori 
coll2 = list(fibonacci(3))
coll3 = []


for fb in fibonacci(12): #Devo creare un ciclo poich+ genera più valori 
    print(fb)
    coll3.append(fb)   #Posso anche metterli in una lista vuota 
    
    
print(coll)


#-------------- DECORATORI -----------------

def decoratore(funzione):
    def wrapper():    #Va sempre messo!!!
        print("Prima dell'esecuzione della funzione")
        funzione()
        print("Dopo l'esecuzione della funzione")
    return wrapper

@decoratore
def saluta():
    print("Ciao")

saluta()
        
#----- ES SOMMA ------
def decoratore_con_argomenti(funzione_somma):
    def wrapper(*args, **kwargs):
        print("Prima")
        risultato = funzione_somma(*args, **kwargs)
        print("Dopo")
        return risultato
    return wrapper


@decoratore_con_argomenti
def somma(a, b):
    print(a+b)
    return a + b


print("risultato è ", somma(3, 4))

#----- ES TIME -----
import time

def calcola_tempo(funzione_calcolo_lento):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        risultato = funzione_calcolo_lento(*args, **kwargs)
        end_time = time.time()
        print(f"Tempo di esecuzione: {end_time - start_time} secondi")
        return risultato
    return wrapper

@calcola_tempo
def calcolo_lento():
    time.sleep(2)
    print("Calcolo completato")

# Chiamata alla funzione decorata

calcolo_lento()
        
#------ ES  AI-----
# 1. Questo è il nostro "assistente" (il decoratore)
def aggiungi_panna(funzione_base):
    def guscio():
        # Azione PRIMA
        print("[Barista]: Prendo la tazza e metto lo zucchero...") 
        
        # Facciamo fare il lavoro al robot base
        funzione_base() 
        
        # Azione DOPO
        print("[Barista]: Ci spruzzo sopra una montagna di panna! 🍦")
        
    return guscio


# 2. Questo è il nostro robot che sa fare solo il caffè liscio
@aggiungi_panna
def prepara_caffe():
    print("[Robot]: Spillo il caffè espresso caldo... ☕")


# --- ORDINIAMO IL CAFFÈ ---
prepara_caffe()