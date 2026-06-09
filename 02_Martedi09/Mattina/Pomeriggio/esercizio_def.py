#-------------ES.1 INDOVINA IL NUMERO ------------------
#import random per provare con random 

numero_segreto = 56

def numero(numero_s, numero_segreto):
   # if numero_s == numero_segreto:
       # print("Hai indovinato il numero segreto!")
    if numero_s < numero_segreto:
        print("Il numero segreto è più alto!")
        return richiesta()   #False
    elif numero_s > numero_segreto:
        print("Il numero segreto è più basso")
        return richiesta()
    elif numero_s > 50 and numero_segreto < 60:
        print("Sei vicino a scoprire il numero segreto!")
        return richiesta()
    else:
        print("Hai indovinato il numero segreto!")
        #Return true 

def richiesta():
    scelta = int(input("Inserisci un numero da 1 a 100: "))
    return scelta
    
while True:
    numero_scelto = richiesta()
    if numero_scelto <= 0 or numero_scelto > 100 :
        print("Il numero inserito non è valido")
    else:
        vittoria = numero(numero_scelto, numero_segreto)
        if vittoria == True:
            break



#-------------ES.2 SEQUENZA DI FIBONACCI ------------------