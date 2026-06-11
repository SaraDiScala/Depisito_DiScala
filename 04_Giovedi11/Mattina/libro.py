#--------------- MODULO LIBRO ------------------------

class Libro:
    def __init__(self,titolo,autore,ISBN):      #Istanzio l'oggetto libro 
        self.titolo = titolo
        self.autore = autore
        self.ISBN = ISBN
    def decrizione_libro(self):    #Stampo la descrizione
        return "Titolo del libro: "+ self.titolo + "---- Autore: " + self.autore + "----ISBN : " + self.ISBN
    