#---------- CLAUSOLE CONTROLLO DI FLUSSO --------------



for i in range(5):
    if i == 3:
        print(i)
    elif i % 2 == 0:
        print(f"Ecco i numeri pari: {i}")
        continue    
    elif i == 4:
        pass
    else i % 3 == 0:
        print(f"Ecco i numeri dispari: {i}")
        break

#--------------- SPLAT * ----------------
numeri = [*range(1,11)]
print(numeri)