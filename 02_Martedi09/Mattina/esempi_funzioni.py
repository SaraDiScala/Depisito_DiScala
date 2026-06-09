#------------------------- FUNZIONI -----------------

def saluta(nome):
    print(f"Ciao {nome}")


def somma(a,b):
    risultato = a+b
    print(f"La somma è: {risultato}")
    
    
#-------RICHIAMO DELLA FUNZIONE PASSANDO DEI PARAMETRI ---------   
saluta("Sara")
somma(5,4)

#--------------------TIPI DI PARAMETRI------------------
 def saluta(nome:str, messaggio="Ciao"):

saluta("Sara")
saluta("Sara", messaggio = "Bentornata")


#------------------------ FUNZIONE CON RETURN---------------
def quadrato(numero):
    return numero * numero 

risultato = quadrato(4)
print(risultato)


