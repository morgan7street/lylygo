# Compteur de Mouvements ESP32‑S3

Ce dépôt contient une simple application MicroPython pour la carte Waveshare **ESP32‑S3 Touch LCD 1.28"**. Le programme lit les données de mouvement du capteur **QMI8658** (accéléromètre/gyroscope) et affiche un compteur sur l'écran rond 1,28" (GC9A01A).

L'application est pensée pour le suivi d'exercices fitness. Portez l'appareil sur la poitrine ou le bras pendant vos entraînements. Chaque mouvement détecté incrémente le nombre affiché.

## Installation

1. Flashez le firmware MicroPython fourni sur le [wiki du produit](https://www.waveshare.com/wiki/ESP32-S3-Touch-LCD-1.28) à l'aide d'`esptool.py`.
2. Installez `mpremote` (inclus dans les versions récentes de MicroPython) sur votre ordinateur :
   ```bash
   pip install mpremote
   ```
3. Clonez ce dépôt et copiez `main.py` et `qmi8658.py` sur la carte :
   ```bash
   mpremote connect /dev/ttyACM0 fs cp main.py :/main.py
   mpremote connect /dev/ttyACM0 fs cp qmi8658.py :/qmi8658.py
   ```
   Remplacez le port série par celui détecté sur votre système.

## Utilisation

1. Redémarrez ou alimentez la carte.
2. L'écran affiche le nombre de mouvements détectés à partir de zéro.
3. Faites vos exercices. À chaque mouvement complet détecté par l'algorithme, le compteur augmente.

## Configuration

Les seuils de détection définis dans `main.py` peuvent nécessiter des ajustements selon l'exercice et la manière dont la carte est portée. Modifiez `THRESH_HIGH` et `THRESH_LOW` pour obtenir de meilleurs résultats.

## Fichiers

- `main.py` – point d'entrée de l'application ; initialise l'écran et l'IMU puis met à jour le compteur.
- `qmi8658.py` – pilote minimal pour l'accéléromètre/gyroscope QMI8658.

