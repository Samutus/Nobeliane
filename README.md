# Nobeliane
projet NSI Renan Mathéo Samuel 2022

## Comment le démarrer ?
Pour pouvoir démarrer le fichier main.py dans un éditeur, il faut entrer les trois commandes suivantes dans une console python :
	- pip install pygame
	- pip install pytmx
	- pip install pyscroll
Une fois ces bibliothèques installées, le fichier main.py devrait être exécutable dans un éditeur et lancer le jeu.


## Astuces
Le plein écran est le format le plus adapté au jeu.
Pour fermer le jeu, il faut exécuter le raccourci Alt + F4 ou le fermer par un autre moyen.


## Créer le fichier .exe sous Windows 10
- Ouvrir PowerShell
- lancer la commande : `pip install -U pyinstaller`
- se rendre dans les sources avec l'explorateur de fichier
- Shift + clic droit : cliquer sur "Ouvrir la fenêtre PowerShell ici"
- Adapter puis lancer la commande : `C:\Users\samuel\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts\pyinstaller.exe main.py -n nobeliane -F`