import numpy as np
import pandas as pd

sales=pd.read_csv("data/sales.csv")   ### Import du fichier sales.csv

def analyser_ventes(ventes, montant):  ## On définit la fonction
    if len(ventes)==0:
     print("erreur")
     return{"erreur"}
    
    else: 
        nombre=len(ventes)
        nombre = len(ventes)
        total = np.sum(ventes[montant])
        moyenne= np.mean(ventes[montant])
        mediane = np.median(ventes[montant])
        ecart_type= np.std(ventes[montant])
        maximum = np.max(ventes[montant])
        minimum = np.min(ventes[montant])
        anomalies = ventes[ventes[montant]>2*moyenne][montant]

    resultat = {"Nombre de ventes": int(nombre),    ###On récupère les valeurs et on les stocke dans un dictionnaire
        "Total des ventes": float(total),
        "Moyenne": float(moyenne),
        "Médiane": float(mediane),
        "Écart-type": float(ecart_type),
        "Minimum": float(minimum),
        "Maximum": float(maximum),
        "Anomalies": anomalies.tolist()}


    for i, valeur in resultat.items():   ###Affichage ligne par ligne
        print(f"{i}:{valeur}")

    return resultat


analyser_ventes(sales, "montant")  ###On execute la fonction