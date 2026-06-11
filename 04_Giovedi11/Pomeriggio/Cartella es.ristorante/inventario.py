#----------------------- INVENTARIO ----------------------
"""2.Gestione dell'Inventario:
Gli articoli in magazzino sono elencati con il nome, il prezzo e la quantità.
È possibile aggiungere nuovi articoli all'inventario.
Gli articoli possono essere rimossi o aggiornati (ad es., cambiare prezzo o
quantità).


I clienti possono visualizzare gli articoli disponibili in inventario.
I clienti possono selezionare e acquistare articoli dall'inventario.


Gli amministratori possono visualizzare lo stato corrente dell'inventario.

"""

import clienti
import amministrazione


class Inventario:
    def __init__(self):
        self.catalogo = []    #Catalogo nuovo che raccoglie gli articoli 
        
        
    def elenco_articoli()                #visualizzare articoli disponibili
        for a in self.catalogo:
            if a a.articolo["nome"] != "":
                print("Nel tuo catalogo ci sono questi titoli: ", self.catalogo)
    
    def stato():
        pass

        

class Articoli:
    def __init__(self,nome,prezzo,quantita):   #Parametri che accetta per l'aggiunta
        self.articolo = {                         #Dizionario che raccoglie i dati input
            "nome": nome,
            "prezzo" : prezzo,
            "quantita": quantita
        }
    
    def aggiungi_articolo(self,articolo):
        self.catalogo.append(articolo)           #Aggiungo articolo all'inventario 
        print("Articolo caricato con successo")
    
    def aggiorna_articolo(self,nome_a,prezzo_a,quantita_a):  #Cambio i valori (?)
        for a in  self.catalogo:
            if a.articolo["nome"] == nome_a:     #A per iterare - articolo è il parametro passato per aggiungere artciolo in catalogo 
                a.articolo["prezzo"] = prezzo_a
                a.articolo["quantita"] = quantita_a
                return "Articolo aggiornato"             #Esce dal flusso e ritorna
                
        
    def articoli_venduti():
    
    
    
    #---------------------------------------------------#