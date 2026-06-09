#----------- ESERCIZIO COMPLETO   -----------

esercizio = int(input("Vuoi svolgere l'esercizio 1 , 2 o 3?: "))

match esercizio:
    case 1:
        numero = int(input("Inserisci un numero: "))
        if numero % 2 == 0:
            print(f"{numero} è un numero pari")
        else:
            print(f"{numero} è dispari")
    case 2:
        n = int(input("Inserisci un numero intero: "))
        while True :
            for i in range(n,-1,-1):
                print(i)
                print("Riparte ciclo infinito")
    case 3:
        lista = []
        for i in range(5):
            numeri = int(input("Inserisci un numero: "))
            lista.append(numeri)
        print(f"La tua lista è: {lista}" )
        
                                                                 #Altrimenti posso anche --  lista_quadrato = []
        for numeri in lista:
            quadrato = numeri **2                                 #  lista_quadrato.append(quadrato) 
            print(f"Il quadrato dei tuoi numeri è: {quadrato}")
    case _:
        print("Effettuva una scelta")
    
#----------- ESERCIZIO EXTRA   -----------
lista_4 = []
for i in range(5):
    numeri = int(input("Inserisci un numero: "))
    lista_4.append(numeri)
    print(f"La tua lista è: {lista_4}" )

for i in range(lista_4):
    
        