# -*-coding:Utf-8 -*
"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""
import os, pickle ,sys

from carte import *

cartes = []
for nom_fichier in os.listdir("cartes"):
	if nom_fichier.endswith(".txt"):
		chemin = os.path.join("cartes", nom_fichier)
		nom_carte = nom_fichier[:-3].lower()
		with open(chemin, "r") as fichier:
			contenu = fichier.read()
			carte=Carte(nom_carte,contenu)
			cartes.append(carte)



"""Vérfie si une partie a eté sauvegardée et propose de la continuer"""

if os.path.isfile('parties')is True:
	continuer = input("Une partie a eté trouvée souhaitez vous continuer ? o/n")
	if continuer == 'o':
		with open('parties', 'rb') as fichier:
			depickler = pickle.Unpickler(fichier)
			anc_partie = depickler.load()
			contenu = anc_partie[0]
			nom = anc_partie[1]
			carte=Carte(nom,contenu)
			cartes.clear()
			if nom == 'facile.':
				cartes.append(carte)
				choixcarte = '1'
			if nom == 'prison.':
				cartes.append(contenu)
				cartes.append(carte)
				choixcarte = '2'

"""propose de choisir une carte """

if 'choixcarte' not in locals():
	print("Labyrinthes existants :")
	for i, carte in enumerate(cartes):
		print("  {} - {}".format(i + 1, carte.nom))
	choixcarte=''
	while True:
		choixcarte=input("Entrez un numero de labyrinthe pour commencer a jouer : \n")
		if choixcarte in '12':
			break

#gère la carte facile

if choixcarte == "1":
	facile = cartes[0]
	print(facile.labyrinthe)
	while True:
		choix = choixdirection()
		a = nombre(choix)
		for i in range(a):
			facile.labyrinthe = facile.labyrinthe.move(choix)
			if facile.labyrinthe == 42:
				print("la partie a été enregistrée avec succès")
				sys.exit(0)
			if facile.labyrinthe.victoire is True: break
			if facile.labyrinthe.porte is True: break
		if facile.labyrinthe.victoire is True: break
		print(facile.labyrinthe)

#gère le carte prison

elif choixcarte == "2":
	prison = cartes[1]
	print(prison.labyrinthe)
	while True:
		choix = choixdirection()
		a = nombre(choix)
		for i in range(a):
			prison.labyrinthe = prison.labyrinthe.move(choix)
			if prison.labyrinthe == 42:
				print("la partie a été enregistrée avec succès")
				sys.exit(0)
			if prison.labyrinthe.victoire is True: break
			if prison.labyrinthe.porte is True: break
		if prison.labyrinthe.victoire is True: break
		print(prison.labyrinthe)

if prison.labyrinthe.victoire is True:
	print("Felicitations ! Vous êtes sorti du labyrinthe ! ")
if os.path.isfile('parties')is True:
	os.remove('parties')
input()
