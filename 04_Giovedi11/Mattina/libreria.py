#--------------- MODULO LIBRERIA ------------------------
import libro                        #Importo modulo libro 

class Libreria:
    def __init__(self):
        self.catalogo = []              #Lista vuota 
    
    def aggiungi_libro(self,libro):     #Funzione per aggiungere libro al catalogo
        self.catalogo.append(libro)     #Aggiungo in lista il nuo oggetto
        return "Libro aggiunto al catalogo"
    
    def rimovi_libro(self, ISBN):             #Rimuovo dalla lista l'oggetto con id ISBN
        for libro in self.catalogo:
            if libro == ISBN:
                self.catalogo.remove(libro)
                return "Libro rimosso dal catalogo"
            
    def cerca_per_autore(self,titolo_da_cercare):                #Ricerca nel catalogo per titolo e inserito in  una lista 
        lista_libri = []
        
        for libro in self.catalogo:                        #Itero sulla classe libro alla ricerca del titolo 
            if libro.self.catalogo == titolo_da_cercare:
                lista_libri.append(libro)
        return lista_libri


    def mostra_catalogo(self):                   #Stampo il catalogo
        print(self.catalogo)
        