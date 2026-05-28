#!/bin/bash

somma() {
	echo $(( $1 + $2 ))
}
sottrai() {
        echo $(( $1 - $2 ))
}
moltiplica() {
        echo $(( $1 * $2 ))
}
dividi() {
        echo $(( $1 / $2 ))
}

while true
do
	echo "=== Calcolatrice ==="
	echo "Inserisci primo numero:"
	read A
	if [ $A -eq 0 ]
	then
    	    echo "Arrivederci! "
	    break
	fi
	echo "Inserisci secondo numero:"
	read B
	echo "Scegli operazione (1=somma 2=sottrai 3=moltiplica 4=dividi):"
	read OP
	if [ $OP -eq 1 ]
	then
    	    echo "Risultato: $(somma $A $B)"
	elif [ $OP -eq 2 ]
	then
    	    echo "Risultato: $(sottrai $A $B)"
	elif [ $OP -eq 3 ]
	then
    	    echo "Risultato: $(moltiplica $A $B)"
	elif [ $OP -eq 4 ]
	then
    	    echo "Risultato: $(dividi $A $B)"
	else
    	    echo "Operazione non valida"
	fi
done
