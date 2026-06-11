#-------------------------------- AMMINISTRAZIONE ----------------------
""""3.Amministrazione:
Gli amministratori possono visualizzare un rapporto delle vendite.
Gli amministratori possono visualizzare lo stato corrente dell'inventario.
Il sistema tiene traccia dei guadagni totali.
Puoi pre inserire gli amministratori non i clienti
"""
import clienti
import inventario


class Amministrazione:
    pass

    def __init__(self):
        pass
    
    def report_vednite():
        pass
    
    def guadagni_tot():
        pass

class Amministratori:
    
    def __init__(self,nome,ruolo,email,id_amministratore):
        self.profilo = {
        "nome" : nome,
        "ruolo" : ruolo,
        "email": email,
        "id_amministratore": id_amministratore
    }
    