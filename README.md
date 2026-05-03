# 🔬 Optical Signal Monitoring & Defect Detection
### LabVIEW + Python Project 

⸻

## 📌 Project Overview
Ce projet présente le développement d'un système d'instrumentation virtuelle pour le monitoring en temps réel et la détection de défauts sur un signal laser simulé. 

Le système combine la puissance de deux environnements complémentaires :
* **LabVIEW** : Pour l'acquisition, le contrôle-commande et le monitoring temps réel.
* **Python** : Pour l'analyse statistique avancée et la visualisation scientifique des données.

Ce travail s'inspire d'applications concrètes en métrologie optique, photonique, systèmes de détection nucléaire et contrôle qualité industriel.

⸻

## 🎯 Objectives
* **Simuler** un signal laser réaliste intégrant du bruit gaussien.
* **Monitorer** le signal via une interface utilisateur dynamique.
* **Détecter** automatiquement les anomalies via un seuil critique.
* **Calculer** des indicateurs statistiques clés (Moyenne, RMS).
* **Analyser** et comparer les signatures des signaux (Normal vs Défaut) sous Python.

⸻

## ⚙️ Technologies Used
* **LabVIEW 2026** (Instrumentation Virtuelle)
* **Python 3.x** (Bibliothèques : NumPy, Matplotlib)
* **Spyder IDE**

⸻

## 🧠 System Architecture

### Part 1 – LabVIEW (Real-Time Monitoring)
L'instrument virtuel (VI) développé comprend :
* **Waveform Chart** : Affichage dynamique du flux de données.
* **Commandes de contrôle** : Puissance Laser, Niveau de Bruit.
* **Sécurité** : Réglage du Seuil Critique et Indicateur LED d'Alarme.
* **Statut du système** : Affichage textuel (NORMAL / DEFECT DETECTED).
* **Indicateurs numériques** : Calcul en temps réel de la valeur Moyenne et RMS.

### Part 2 – Python (Data Analysis)
Le script Python permet de traiter les données hors-ligne pour :
* Identifier précisément les écarts statistiques entre un signal sain et un signal défaillant.
* Générer des histogrammes de distribution pour valider la nature du bruit.

⸻

## 🧪 Scientific Approach
Le signal est modélisé par l'équation suivante :
**$Signal = Laser Power + Noise$**

* **Noise** : Suit une distribution normale (Gaussienne).
* **Mean** : Représente le niveau moyen du signal laser.
* **RMS** : Représente la puissance efficace du signal.

**Logique de détection :**
Une alerte est déclenchée lorsque :  
`Signal < Critical Threshold` (Simulant une baisse de performance ou une obstruction du faisceau).

⸻

## 📈 Key Results
* Visualisation claire du signal bruité sur le Waveform Chart.
* Déclenchement instantané de l'alarme lorsque la puissance chute sous le seuil.
* L'analyse Python montre un décalage net de l'histogramme en cas de défaut.

⸻

## 📂 Project Files & Resources
* **[📄 Consulter le Rapport Technique Complet (PDF)](Rapport_LabVIEW.pdf)**
* **[🐍 Voir le Code Python d'Analyse](analysis.py)**

⸻

## 🚀 How to Run
1.  **LabVIEW** : Ouvrez le fichier `.vi`, réglez vos paramètres (Power, Noise) et cliquez sur la flèche blanche **Run**.
2.  **Python** : Exécutez le script dans Spyder ou VS Code. Assurez-vous d'avoir installé les dépendances : `pip install numpy matplotlib`.

⸻

## 👤 Author
**Babacar Ndiaye** Master 2 Physique Appliquée – Nanophysique et Optique Avancée

⸻
*Ce projet démontre une capacité à concevoir des systèmes de mesure complexes alignés sur les défis industriels de l'instrumentation de pointe.*
