#!/bin/bash

somma() {
	RISULTATO=$(( $1 + $2 ))
	echo "Somma: $RISULTATO"
}
moltiplica() {
	RISULTATO=$(( $1 * $2 ))
        echo "Moltiplicazione: $RISULTATO"
}
sottrai() {
        RISULTATO=$(( $1 - $2 ))
        echo "Sottrazione: $RISULTATO"
}

dividi() {
        RISULTATO=$(( $1 / $2 ))
        echo "Divisione: $RISULTATO"
}

somma 5 3
moltiplica 4 6
sottrai 10 4
dividi 20 4
