# =============================================
# ALGORITMI DI BASE - Python
# ITIS Montani - Data Science e Machine Learning
# =============================================

# --- RICERCA LINEARE ---
# Scorre la lista elemento per elemento finché non trova quello cercato
def ricerca_lineare(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i  # restituisce la posizione trovata
    return -1  # restituisce -1 se non trovato

# Test
numeri = [5, 3, 8, 1, 9, 2, 7]
risultato = ricerca_lineare(numeri, 9)
if risultato != -1:
    print(f"Ricerca lineare: elemento trovato in posizione {risultato}")
else:
    print("Ricerca lineare: elemento non trovato")


# --- BUBBLE SORT ---
# Confronta elementi vicini e li scambia finché la lista è ordinata
def bubble_sort(lista):
    n = len(lista)  # lunghezza della lista
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                # scambia i due elementi adiacenti
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista  # restituisce la lista ordinata

# Test
numeri = [5, 3, 8, 1, 9, 2, 7]
print("Bubble sort - Prima:", numeri)
ordinata = bubble_sort(numeri)
print("Bubble sort - Dopo:", ordinata)


# --- RICERCA BINARIA ---
# Funziona solo su liste ordinate, divide la lista a metà ogni volta
# Molto più veloce della ricerca lineare su liste grandi
def ricerca_binaria(lista, elemento):
    sinistra = 0
    destra = len(lista) - 1

    while sinistra <= destra:
        meta = (sinistra + destra) // 2  # indice di mezzo

        if lista[meta] == elemento:
            return meta  # trovato
        elif lista[meta] < elemento:
            sinistra = meta + 1  # cerca nella metà destra
        else:
            destra = meta - 1  # cerca nella metà sinistra

    return -1  # non trovato

# Test - usiamo la lista già ordinata
ordinata = [1, 2, 3, 5, 7, 8, 9]
risultato = ricerca_binaria(ordinata, 7)
if risultato != -1:
    print(f"Ricerca binaria: elemento trovato in posizione {risultato}")
else:
    print("Ricerca binaria: elemento non trovato")


# --- TROVA MASSIMO ---
# Scorre la lista tenendo traccia del valore più grande trovato
def trova_massimo(lista):
    massimo = lista[0]  # partiamo dal primo elemento
    for elemento in lista:
        if elemento > massimo:
            massimo = elemento  # aggiorniamo il massimo
    return massimo  # restituisce il valore massimo

# Test
numeri = [5, 3, 8, 1, 9, 2, 7]
risultato = trova_massimo(numeri)
print(f"Massimo: {risultato}")


# --- TROVA MINIMO ---
# Scorre la lista tenendo traccia del valore più piccolo trovato
def trova_minimo(lista):
    minimo = lista[0]  # partiamo dal primo elemento
    for elemento in lista:
        if elemento < minimo:
            minimo = elemento  # aggiorniamo il minimo
    return minimo  # restituisce il valore minimo

# Test
numeri = [5, 3, 8, 1, 9, 2, 7]
risultato = trova_minimo(numeri)
print(f"Minimo: {risultato}")


# --- SELECTION SORT ---
# Trova il minimo nella parte non ordinata e lo mette in posizione
def selection_sort(lista):
    n = len(lista)  # lunghezza della lista

    for i in range(n):
        min_indice = i  # assumiamo che il minimo sia in posizione i

        # cerchiamo il minimo nel resto della lista
        for j in range(i+1, n):
            if lista[j] < lista[min_indice]:
                min_indice = j  # aggiorniamo l'indice del minimo

        # scambiamo il minimo trovato con l'elemento in posizione i
        lista[i], lista[min_indice] = lista[min_indice], lista[i]

    return lista  # restituisce la lista ordinata

# Test
numeri = [5, 3, 8, 1, 9, 2, 7]
print("Selection sort - Prima:", numeri)
ordinata = selection_sort(numeri)
print("Selection sort - Dopo:", ordinata)