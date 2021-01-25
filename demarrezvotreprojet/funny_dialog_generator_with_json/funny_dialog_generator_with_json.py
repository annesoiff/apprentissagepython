# -*- coding: utf8 -*-

"""************************************************
Ce programme contient une fonction qui va lire une liste de citation
et de personnages dans des fichiers SJON. Les fonctions suivantes
choisissent  une citation et un presonnage aléatoirement qui sont
affichées tant que l'utilisateur le souhaite, pour créer un dialogue
loufoque

PAR : 	Anne-Sophie Lachapelle
POUR : 	Openclassroom, cours Démarrez votre projet avec Pyhton
DATE :	janvier 2020

************************************************"""
import random
import json

"""
Fontion inutiles puisque stocké dans fichiers externes. 
quotes = [
    "La nuit porte de garage", 
    "Ah, come one Carl",
    "Drop ton gun !",
    "Persécution !"
	]

characters = [
    "Capitaine Patenaude", 
    "Leo Rivard, directeur technique", 
    "Ben Chartier", 
    "Manolo Laporte Carpentier"
    ]
    """


# fonction qui va chercher les données dans un fichier JS
def read_values_from_json(file, key):
    # Create a new empty list
    values = []
    # open a json file with my objects
    with open(file) as f:
        # load all the data contained in this file
        data = json.load(f)
        for entry in data:
            # add each item in my list
            values.append(entry[key])
    # return my completed list
    return values


# fonction qui construit une ligne de dialogue
def message(characters, quote):
    return "{} a dit : {}".format(characters, quote)


# fonction pour retourner une valeur aléatoire dans un fichier de données JSON
def get_random_item_in(my_list):
    rand_item = random.randint(0, len(my_list) - 1)
    item = my_list[rand_item]
    return item


# fonction qui choisi aléatoirement la citation

def get_random_quote():
    all_values = read_values_from_json('quotes.json', 'quote')
    return get_random_item_in(all_values)


# fonction qui choisi aléatoirement le personnage
def get_random_character():
    all_values = read_values_from_json('characters.json', 'character')
    return get_random_item_in(all_values)


user_answer = input("Tapez entrée pour générer du dialogue ou B pour quitter")

while user_answer != "B":
    print(message(get_random_character(), get_random_quote()))
    user_answer = input()
