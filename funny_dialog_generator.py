# -*- coding: utf8 -*-

"""************************************************
Ce programme contient une liste de citation et une liste de personnages
inconiques de la télévision québécoise. Les fonctions choisissent une
citation et un presonnage aléatoirement qui sont affichées tant que 
l'utilisateur le souhaite, pour créer un dialogue loufoque

PAR : 	Anne-Sophie Lachapelle
POUR : 	Openclassroom, cours Démarrez votre projet avec Pyhton
DATE :	janvier 2020

************************************************"""
import random
 
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

#fonction qui choisi aléatoirement la citation
def get_random_quote(my_list):
	rand_quote = random.randint(0, len(my_list) - 1)
	quote = my_list[rand_quote]
	return quote

#fonction qui choisi aléatoirement le personnage
def get_random_character(my_list):
	rand_character = random.randint(0, len(my_list) - 1)
	characters = my_list[rand_character]
	return characters

#fonction qui construit une ligne de dialogue
def message(characters, quote):
	return "{} a dit : {}".format(characters, quote)

	

user_answer = input("Tapez entrée pour générer du dialogue ou B pour quitter")

while user_answer != "B":
	print(message(get_random_character(characters), get_random_quote(quotes)))
	user_answer = input()
