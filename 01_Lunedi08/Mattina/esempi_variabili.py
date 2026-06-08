variabile_nome = "Sara"                        #Creazione variabile stringa 
variabile_codice_corso = 30568                 #Creazione variabile int
print("Nome studente ", variabile_nome , "codice corso ", variabile_codice_corso)  #Stampare le variabili 


richiesta_nome = input("Inserisci nome:")                            #Richiesta input all'utente di un valore stringa
richiesta_corso = int(input("Inserisci codice: "))                   #Richiesta input all'utente di un valore int 
print("Ciao" + richiesta_nome + "Benvenuto al corso numero: " , richiesta_corso)   #Stampa dei valori input


print(1+5)         #Somma
print(6-5)         #Sottrazione
print(3*2)        #Moltiplicazione
print(4/2)        #Divisione
print(3**2)       #Esponente

#VARIABILI NUMERICI 
x = 10     #Intero positivo
y = -5     #Interop negativo 

#VARIABILI FLOAT
x2 = 10.5    #Float positivo
y2 = -6.7    #Float negativo

#VARIABILE STRINGA 
striga_nome = "Sara"
stringa_cognome = 'Di Scala'
s = "sara"
print(s[0])     #Stampa il carattere/valore in posizione 0 (s)
print(s[3])     #Stampa il carattere/valore in posizione 3 (a)
print("Ciao"+ s + stringa_cognome)   #Stampa i valori delle stringhe concatenate

#METODI DELLE STRINGHE
s2 = "Ciao e benvenuto!"   #Variabile stirnga
print(len(s2))             #Output:17 - Funzione che restituisce la lunghezza della stringa (caratterie e spazi)
print(s2.upper())          #Outupt: CIAO E BENVENUTO  - Metodo che riestituisce la stringa tutta in maiuscolo 
print(s2.split(','))       #Output: [Ciao], [e] , [Benvenuto] - Metodo che restituisce valori singoli divisi da , 
print(s2.replace('Ciao', 'buongiorno'))   #Output: buongiorno e benvenuto - Metodo che sostituisce un valore con un altro

#VARIABILE BOOLENA
var_booleana = True     #Rappresenta un valore 1 
var_boolena2 = False    #Rappresenta un valore 0 

#OPERATORI DI CONFRONTO CON VALORI BOOLEANI

a = 5
b = 10
c = "10"

print(a == y)        #Output: False  - Sono due valori diversi 
print(a != b)        #Output:True - Sono due valori diversi 
print(a < b)        #Output:True -  a è minore di b
print(a == c)        #Output:False - Sono due valori diversi poichè sono due tipi di dato diversi (int e stringa)

#OPERATORI LOGICI CON VALORI BOOLEANI
a = 5
b = 10
d = 7

print(a < b and b > d)  #Output: True   - and restituisce True se entrambi i confronti sono true 
print(a < b or d > b )  #Output: True   - or restituisce True se almeno un confronto è true
print(not(a < b))       #Output:False   - not restituisce False poichè il valore confrontato è True , cioè restituisce l'opposto

#COLLEZIONI IN PYTHON

#LISTA []
numeri = [1,2,3,4,5]                    #Lista di int
nomi = ["Sara", "Carlo"]                #Lista di stringhe
misto = [1, "due", 3, "quattro", 3.4 ]  #Lista stringa,int,float

print(numeri[2])      #Output:3    
print(misto[1])       #Output:Carlo
print(misto[0])       #Output:1
print(misto[4])       #Output:3.4

#LISTE CON METODI
numeri = [1,2,3,4,5] 

print(len(numeri))    #Output:5 - Stampa la lunghezza della lista

numeri.append(6)      #Output:[1,2,3,4,5,6] - Aggiunge un valore alla fine della lista
print(numeri)

numeri.insert(2,10)   #Output:[1,2,10,4,5]  - Inserisce in posizione [2] il valore 10 
print(numeri)

numeri.remove(4)      #Output:[1,2,10,5] - Rimuove il valore 4
print(numeri)

numeri.sort()         #Output: [1,2,5,10] - Mette in ordine la lista 
print(numeri)


