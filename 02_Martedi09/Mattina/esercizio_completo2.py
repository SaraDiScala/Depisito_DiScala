
#-------------- ESERCIZIO COMPLETO 2 ---------------------------------4

while True:
    numero = int(input("Inserisci un numero positivo: "))
    
    if numero > 0:

        somma_pari = 0               
        for i in range(2, numero + 1, 2):   #Itero partendo da 2, includo il mio numero, salto di 2
            somma_pari += i                 #aggiorno la var somma
        print(f"La somma dei numeri pari da 1 a {numero} è: {somma_pari}")   
        
   
        somma_dispari = 0  
        for i in range(1, numero + 1, 2):     #Itero partendo da 1,includo il mio numero, salto di 2
            somma_dispari += i
        print(f"La somma dei numeri dispari da 1 a {numero} è: {somma_dispari}")
        
        if numero == 1:                         #Controllo se il numero è un numero primo
            print("1 non è un numero primo.")   #1 è numero  primo per eccellenza
        else:                                   #Se non è 1 controllo che numero è
            nprimo = True                      # Partiamo dal presupposto che sia primo
            
            for i in range(2, numero):
                if numero % i == 0:   #Controlla se il risultato è 0
                    nprimo = False    #Non è divisibile per se stesso
                    break             #Interrompiamo la ricerca
            
            if nprimo == True:       #Se resta True
                print(f"{numero} è un numero primo!")
            else:
                print(f"{numero} non è un numero primo.")
        break 
        
    else:
        print("Hai inserito un numero non valido. Riprova.")  #Se il numero + negativo o 0


























#EXTRA Far si che lavori su una lista 