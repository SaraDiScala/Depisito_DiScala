#---------------------GESTIONE CLIENTI ---------------------
"""1.Gestione Clienti:
I clienti possono visualizzare gli articoli disponibili in inventario.
I clienti possono selezionare e acquistare articoli dall'inventario.
Il sistema tiene traccia degli acquisti dei clienti.

Puoi pre inserire gli amministratori non i clienti
    """

import amministrazione
import inventario

   
class Cliente:
    
    def __init__(self, nome, citta, eta, email, id_cliente):
        self.profilo = {
        "nome" : nome,
        "citta" : citta,
        "eta" : eta,
        "email": email,
        "id_cliente": id_cliente
    }
    def acqusiti():
        pass
    
