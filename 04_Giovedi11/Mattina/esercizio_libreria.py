#------------------ ESERCIZIO LIBRERIA -----------------
import libro              #Importo i moduli 
import libreria


libro_a = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", "978884593")      #Inserisco manualmente dei libri 
libro_b = Libro("Harry Potter e la Pietra Filosofale", "J.K. Rowling", "978886715")
libro_c = Libro("Lo Hobbit", "J.R.R. Tolkien", "978884594")

print(libro_a.decrizione_libro())      #stampo la decsrzione di ciascun libro richiamando la funzione del modulo libro 
print(libro_b.decrizione_libro())
print(libro_c.decrizione_libro())

mia_libreria = libreria.Libreria()     #Istanzio l'oggetto libreria e inserisco i libri nel catalogo richiamando la funzione del modulo libreria
mia_libreria.aggiungi_libro(libro_a)        #aggiungo i libri 
mia_libreria.aggiungi_libro(libro_b)
mia_libreria.aggiungi_libro(libro_c) 

mia_libreria.mostra_catalogo()      #stampo catalogo libreria 

ricerca_libro = "Potter"                                       #effettuo ricerca per titolo 
libri_trovati = mia_libreria.cerca_per_titolo(ricerca_libro)       #inserisco il titolo in una variabile per la stampa 

print("Risultati ricerca:" , libri_trovati)       #stampo libro trovato 

mia_libreria.rimuovi_libro("978886715") # Rimuoviamo Harry Potter          #Rimozione con la funzione del modulo libreria
mia_libreria.mostra_catalogo()