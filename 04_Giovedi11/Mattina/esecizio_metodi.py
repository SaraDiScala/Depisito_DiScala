#-------------------------- ESERCIZIO 5 @STATICMETHOD -------------------------------

class Convertitore:
    
    @staticmethod                        #Creo un metodo static
    def euro_in_dollaro(euro):           #Nome del metodo 
        return euro *1.08                #Cosa ritorna direttamente il metodo
    
    @staticmethod
    def km_in_miglia(km):
        return km * 0.621371
    
conversione_ed = int(input("Inserisci un valore in euro: "))   #Variabile per chiedere input 
conversione_k = int(input("Inserisci un valore in Km: "))

conversione_dollaro = Convertitore.euro_in_dollaro(conversione_ed)   #Variabile convertita - richiamo direttamente il metodo statico
conversione_miglia =Convertitore.km_in_miglia(conversione_k)
print(conversione_dollaro)                        #Srampo conversione 
print(conversione_miglia)


    
    
 #----------- Ragionamento sbagliato xxxxxx ------------------------   
    
"""   def euro_in_dollari():
        euro = int(input("Inserisci importo in euro: "))
        
        while True: 
             euro = int(input("Inserisci importo in euro: "))
                if euro == int:
                    dollaro += euro(float)* 1.08
                    print("Il tuo valore in dollaro è: ", dollaro)
                    break 
                else:
                    print("Il valore inserito non è in euro")
    
    """
#-------------------------- ESERCIZIO 6 @CLASSMETHOD -------------------------------

class Animale:
    numero_animali = 0    #Attributo claasse
    
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie
        Animale.numero_animali += 1
    
    @classmethod
    def quanti_animali(cls):                                  #cls = richiama la classe stessaa
        print("Numero di animali creati: " , cls.numero_animali )

animale1 = Animale("Simba", "Leone")                     #Popolo con 3 dati manualmente 
animale2 = Animale("Willy", "Delfino")
animale3 = Animale("Bugs Bunny", "Coniglio")



nome_animale = input("Inserisci nome animale: ")        # Richiesta dei dati dall'utente 
specie_animale = input("Inserisci specie animale: ")

animale_input = Animale(nome_animale,specie_animale)      #Carico i dati inseriti dall'utente 

print(Animale.quanti_animali())               #stampo classmethod direttamente per ricevere i dati 


 #----------- Ragionamento sbagliato xxxxxx ------------------------   


""" def __init__ (self, nome,specie):
        self.nome = nome
        self.specie = specie 
        Animale.numero_animali += 1    #Aumento ogni volta che aggiungo animali 
        
        while True:
            domanda = print("Vuoi aggiungere un animale? :").lower()
            if domanda == "si" 
            """