#!/bin/bash
DATA=$(date +%Y-%m-%d)
ORIGINE="/mnt/c/Users/Lenovo/progetti_scuola"
DESTINAZIONE="/mnt/c/Users/Lenovo/backup_$DATA"
mkdir -p $DESTINAZIONE
cp -r $ORIGINE/* $DESTINAZIONE

echo "Backup completato in: $DESTINAZIONE"


