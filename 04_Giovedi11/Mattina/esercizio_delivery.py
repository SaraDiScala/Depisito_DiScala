#Classe ristorante 
#Classe piatto
#Clase ordine /utente /chef 

#---------------------------------------------- ESERCIZIO DELIVERY ------------------------------------------


# --------------------- CLASSE RISTORANTE -------------------------------
class Ristorante:                                  
    tot_ristoranti = 0
                             
    def __init__(self,nome,tipo_cucina):                 #Costruttore - inizializzazione dell'oggetto con attributi
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        Ristorante.tot_ristoranti += 1
        
    
    def descrivi_ristorante():
        print("Descrizione del ristorante. Nome: " , Ristorante.self.nome , "\n Tipo di cucina: " , Ristorante.self.tipo_cucina)
        
    def stato_apertura(self):
        if self.aperto:
            print("Il ristorante è aperto ")
        else:
            print("Il ristorante è chiuso ") 
    def apri_ristorante (self):
        self.aperto = True
        print("Il ritorante adesso è eaperto")
        
    def chiudi_ristorante(self):
        self.aperto = False
        print("Il ristorante ora è chiuso")

# --------------------- CLASSE PIATTO ------------------------------------
 
class Menu:
    menu_piatti = []

    def __init__(self,piatto,prezzo):
        self.piatto = piatto
        self.prezzo = prezzo
        
    def aggiungi_al_menu(self):                  #Metodo per aggiungere piatti
        Menu.menu_piatti.append(self)             #Ogni volto che creo l'oggetto, si aggiunge alla lista 
        
    def togli_dal_menu(self):
        if self in Menu.menu_piatti:
            Menu.menu_piatti.remove(self)

    def stampa_menu(cls):
        if not cls.menu_piatti:
            print("Il menu è vuoto.")
        else:
            for p in cls.menu_piatti:
                print(p.piatto , p.rezzo)


# --------------------- CLASSE ORDINE ------------------------------------
class Ordine:
    ordine_utente = 0
    
    
    def __init__(self,id_ordine, nome_utente):
        self.id_ordine = id_ordine 
        self.nome_utente = nome_utente 
        self.stato ="in corso"
        self.piatti_ordinati = []
        Ordine.ordine_utente += 1
    
    def aggiungi_piatto(self,piatto):
        self.piatti_ordinati.append(piatto) 
        Ordine.ordine_utente += 1 
   
         
    def stato_ordine(sel, stato): 
        stati = ["in corso", "completato", "annullato"]
        if stato in stati:
            case "in corso":
                
            case "completatoi"


    
# ---------------------  TEST ------------------------------------
    

