# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""
from labyrinthe import *


class Carte:

	"""Objet de transition entre un fichier et un labyrinthe."""



	def __init__(self, nom,chaine):

		self.nom = nom
		chaine = spawn(chaine)
		lab = Labyrinthe("X","O",chaine,nom)
		self.labyrinthe=lab
		self.carte = chaine

	def __repr__(self):
		return "<Carte {}>".format(self.nom)