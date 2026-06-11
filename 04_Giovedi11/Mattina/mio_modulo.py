#------------------------ MODULI --------------------
def saluta(nome):
    print("Ciao", nome)
    
PI = 3.14159

class Cerchio:
    def __init__(self,raggio):
        self.raggio = raggio

    def are(self):
        return PI * self.raggio*2
    