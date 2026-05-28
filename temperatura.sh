#!/bin/bash
echo "Inserisci la temperatura:"
read TEMP

if [ $TEMP -gt 30  ]
then
     echo "Fa caldo"
elif [ "$TEMP" -ge 15 ] && [ "$TEMP" -le 30 ]
then
    echo "Temperatura normale"
elif [ $TEMP -lt 15 ]
then
    echo "Fa freddo"

fi
