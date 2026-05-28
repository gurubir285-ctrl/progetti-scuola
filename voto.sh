#!/bin/bash
echo "Insersci il tuo voto:"
read VOTO

if [ $VOTO -ge 6 ]
then
    echo "Promosso"
else
    echo "Bocciato"
fi


