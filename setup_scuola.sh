#!/bin/bash
ANNO=2026
MATERIE="python c linux arduino data_science"

echo "Setup cartelle anno $ANNO"

for MATERIA in $MATERIE
do 
	mkdir -p $ANNO/$MATERIA
	echo "Creata cartella: $ANNO/$MATERIA"
done

echo "Fatto"
