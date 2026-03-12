import pandas as pd
import numpy as np
import string

#Lecture du fichier (dataset) 
def charger_dataset():
    try: 
        with open('dataset.csv', 'r') as dataset:
            data = dataset.read()
        print("Fichier chargé avec succès")
        print(data)

    except FileNotFoundError: 
        print("Erreur, fichier non trouvé")

    except Exception as e:
        print("Une erreur est survenue")   

charger_dataset()

#Preprocessing, data cleaning

def nettoyer_phrase():  #lowercase puis supprimer ponctuation, et enfin split la phrase
    ponctuation = string.punctuation
    phrase = str(input("Entrez une commande:\n")).lower()
    for symbole in ponctuation:
        phrase = phrase.replace(symbole,"")
    resultat = phrase.split()
    print(resultat)
    
nettoyer_phrase()