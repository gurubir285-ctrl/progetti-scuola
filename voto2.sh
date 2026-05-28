#!/bin/bash
echo "Inserisci il tuo voto:"
read VOTO

if [ $VOTO -ge 8 ]
then
    echo "Ottimo"
elif [ $VOTO -ge 6 ]
then
    echo "Promosso"
else
    echo "Bocciato"
fi

