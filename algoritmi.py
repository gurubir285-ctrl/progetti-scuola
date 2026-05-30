# Ricerca lineare - cerca un elemento in una lista
def ricerca_lineare(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i  # restituisce la posizione
    return -1  # non trovato

# Test
numeri = [5, 3, 8, 1, 9, 2, 7]
risultato = ricerca_lineare(numeri,99)

if risultato != -1:
    print(f"Elemento trovato in posizione {risultato}")
else:
    print("Elemento non trovato")

# Bubble sort - ordina una lista
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                # scambia i due elementi
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# Test
numeri = [5, 3, 8, 1, 9, 2, 7]
print("Prima:", numeri)
ordinata = bubble_sort(numeri)
print("Dopo:", ordinata)

# Ricerca binaria - funziona solo su liste ordinate
def ricerca_binaria(lista, elemento):
    sinistra = 0
    destra = len(lista) - 1
    
    while sinistra <= destra:
        meta = (sinistra + destra) // 2
        
        if lista[meta] == elemento:
            return meta
        elif lista[meta] < elemento:
            sinistra = meta + 1
        else:
            destra = meta - 1
    
    return -1

# Test - usiamo la lista già ordinata
ordinata = [1, 2, 3, 5, 7, 8, 9]
risultato = ricerca_binaria(ordinata, 7)

if risultato != -1:
    print(f"Elemento trovato in posizione {risultato}")
else:
    print("Elemento non trovato")

# Ricerca max  nella lista
def trova_massimo(lista):
    massimo = lista[0]
    for elemento in lista:
        if elemento > massimo:
            massimo = elemento
    return massimo  # restituisce il massimo
        
# Test
numeri = [5, 3, 8, 1, 9, 2, 7]
risultato = trova_massimo(numeri)

print(f"Il valore massimo nella lista è: {risultato}")

# Ricerca minimo  nella lista
def trova_minimo(lista):
    minimo = lista[0]
    for elemento in lista:
        if elemento < minimo:
            minimo = elemento
    return minimo  # restituisce il minimo
        
# Test
numeri = [5, 3, 8, 1, 9, 2, 7]
risultato = trova_minimo(numeri)

print(f"Il valore minimo nella lista è: {risultato}")

