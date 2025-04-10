# Sonification de données météo

## Bibliothèques nécéssaires

Pour exécuter le projet il faut télécharger les bibliothèques suivantes:
- random
- numpy
- requests
- tkinter
- re
- playsound
- gtts
- speech_recognition

  Vous pouvez faire (conseil: installer tout dans un venv):
  
  ```pip install numpy requests playsound gTTS SpeechRecognition```


## Lancer le projet

explications: Notre projet a une interface sonore, cependant on peut aussi personnaliser le résultat ce qui ouvre une interface graphique:

```python3 main.py```

## Interagir dans le main

La première question est:
"Est ce que vous voulez personnaliser l'audio final ?"
il faut répondre : oui / non

la deuxième question est:
"La météo de quelle ville vous interesse-t-elle ?"
il faut dire le nom d'une ville française

Vous obtenez un fichier midi
