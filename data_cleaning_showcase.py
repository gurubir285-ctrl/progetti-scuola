"""
Data Cleaning Showcase
========================
Questo script dimostra un tipico workflow di pulizia dati con Pandas:
rimozione duplicati, gestione valori mancanti, normalizzazione formati,
e validazione finale del dataset.

Autore: Gurbir Singh
Percorso: Data Science & Machine Learning - ITIS Montani
"""

import pandas as pd
import numpy as np


def crea_dataset_esempio() -> pd.DataFrame:
    """
    Genera un dataset finto che simula problemi comuni:
    - righe duplicate
    - email con maiuscole/minuscole miste
    - valori numerici mancanti
    - formati data incoerenti
    - valori testuali mancanti
    """
    dati = {
        "nome": ["Mario Rossi", "Anna Bianchi", "Mario Rossi", "Luca Verdi", None, "Sara Neri"],
        "email": ["mario@email.com", "ANNA@EMAIL.COM", "mario@email.com",
                  "luca@email.com", "sara@email.com", None],
        "vendite": [150, 200, 150, np.nan, 300, 175],
        "data": ["2024-01-15", "15/01/2024", "2024-01-15",
                 "2024-01-16", "2024-01-17", "2024-01-18"],
    }
    return pd.DataFrame(dati)


def pulisci_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applica una pipeline di pulizia standard al dataset:

    1. Rimuove le righe duplicate basandosi sull'email
    2. Rimuove le righe con nome o email mancanti (dati non utilizzabili)
    3. Normalizza le email in minuscolo
    4. Sostituisce i valori numerici mancanti con la media della colonna
    5. Uniforma il formato delle date in YYYY-MM-DD

    Parameters
    ----------
    df : pd.DataFrame
        Il dataset originale, potenzialmente "sporco"

    Returns
    -------
    pd.DataFrame
        Il dataset pulito, pronto per l'analisi
    """
    df_pulito = df.copy()

    # 1. Rimuovi duplicati basati sull'email
    df_pulito = df_pulito.drop_duplicates(subset="email")

    # 2. Rimuovi righe con dati essenziali mancanti
    df_pulito = df_pulito.dropna(subset=["nome", "email"])

    # 3. Normalizza le email
    df_pulito["email"] = df_pulito["email"].str.lower()

    # 4. Gestisci valori numerici mancanti (media della colonna)
    media_vendite = df_pulito["vendite"].mean()
    df_pulito["vendite"] = df_pulito["vendite"].fillna(media_vendite)

    # 5. Uniforma il formato delle date
    df_pulito["data"] = pd.to_datetime(df_pulito["data"], format="mixed", dayfirst=False)
    df_pulito["data"] = df_pulito["data"].dt.strftime("%Y-%m-%d")

    # Reset dell'indice per un output più pulito
    df_pulito = df_pulito.reset_index(drop=True)

    return df_pulito


def valida_dataset(df: pd.DataFrame) -> None:
    """
    Esegue controlli di qualità di base sul dataset pulito
    e stampa un report riassuntivo.
    """
    print("\n--- Report di validazione ---")
    print(f"Righe totali: {len(df)}")
    print(f"Valori mancanti per colonna:\n{df.isna().sum()}")
    print(f"Email duplicate: {df['email'].duplicated().sum()}")
    print(f"Range vendite: {df['vendite'].min()} - {df['vendite'].max()}")


def main():
    print("=== DATASET ORIGINALE (sporco) ===")
    df_sporco = crea_dataset_esempio()
    print(df_sporco)

    print("\n=== DATASET PULITO ===")
    df_pulito = pulisci_dataset(df_sporco)
    print(df_pulito)

    valida_dataset(df_pulito)


if __name__ == "__main__":
    main()
