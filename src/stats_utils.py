import numpy as np
def analyser_ventes(transactions):
    ventes = np.array(transactions)
    ventes = ventes[ventes>0]
    if len (ventes) ==0:
        return {"erreur"}

    nombre = len(ventes)
    total = np.sum(ventes)
    moyenne= np.mean(ventes)
    mediane = np.median(ventes)
    ecart_type= np.std(ventes)
    maximum = np.max(ventes)
    minimum = np.min(ventes)

    anomalies = ventes[ventes> 2*moyenne]

    return {"Nombre de ventes": int(nombre),
        "Total des ventes": float(total),
        "Moyenne": float(moyenne),
        "Médiane": float(mediane),
        "Écart-type": float(ecart_type),
        "Minimum": float(minimum),
        "Maximum": float(maximum),
        "Anomalies": anomalies.tolist()}

transactions = [150, 200, 250, 300, 400, -50, 0]

resultat = analyser_ventes(transactions)

for i, valeur in resultat.items():
    print(f"{i} : {valeur}")
