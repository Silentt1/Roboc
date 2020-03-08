# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

import pickle,random


def murer(nv_pos,grille):
	listett = list(grille[0])
	if listett[nv_pos] == '.':
		return True

def percer(nv_pos,grille):
	listett = list(grille[0])
	if listett[nv_pos] == 'O':
		return True

def spawn(chaine):
	compteur = -1
	compteur2 = 0
	chaine = list(chaine)
	nbspace = chaine.count(' ')
	selection = random.randint(0, nbspace - 1)
	for lettre in chaine:
		if lettre == " ":
			compteur += 1
			if compteur == selection:
				chaine[compteur2] = "X"
				break
		compteur2 += 1
	chainel = ''.join(chaine)
	return chainel


"""retourne le nombre de fois que la boucle devra executer le mouvement ou 1 par défaut """

def nombre(choix):
	try:
		choix[1]
		if choix[1] in '123456789':
			a = choix[1]
			a = int(a)
		if choix[1] in 'neso':
			a = 1
	except :
		a = 1
	return a

"""va renvoyer une liste sous forme ['s','2'] par exemple"""

def choixdirection():
	while True:
		try:
				choix=input("Choisissez une direction : ")
				choix=choix.lower()
				choix=list(choix)
				assert choix[0] in 'nesoqmp' and len(choix) < 3
				if len(choix) == 2 and choix[1] not in '123456789neso':
					raise AssertionError
				break
		except AssertionError:
				print("Le premier caractère doit être une lettre (n,s,o,e,m ou q) et vous pouvez egalement rajouter\n un numero pour indiquer le nombre de cases a parcourir")
		except IndexError:
				print("Le premier caractère doit être une lettre (n,s,o,e,m ou q) et vous pouvez egalement rajouter\n un numero pour indiquer le nombre de cases a parcourir")
	return choix

class Labyrinthe:

	"""Classe représentant un labyrinthe."""

	def __init__(self, robot, obstacles, labyrinthe,nom):
		self.robot = robot
		self.grille = []
		self.grille.append(labyrinthe)
		self.porte = False
		self.nom = nom
		self.victoire=False
	def __repr__(self):
		return self.grille[0]

	"""vérifie si le prochain mouvement va rencontrer un obstacle"""

	def check_obstacle(self,nv_pos):
		listet = list(self.grille[0])
		if listet[nv_pos] == "O":
			return True

	"""vérifie si la prochaine case est la sortie """

	def check_victoire(self,nv_pos):
		listet = list(self.grille[0])
		if listet[nv_pos] == "U":
			return True


	"""sauvegarde la partie en cours"""

	def enregistrement(self):
		contenu = self.grille[0]
		nom = self.nom
		listepickle = [contenu,nom]
		with open('parties','wb') as fichier:
			pickler = pickle.Pickler(fichier)
			pickler.dump(listepickle)

	"""déplace le robot et vérifie les obstacles,victoire ou enregistre le partie si l'utilisateur a appuyé sur 'q' """

	def move(self,choix):
		percage = False
		mur = False
		porte = False
		poss = self.grille[0].find(self.robot)
		sliced = self.grille[0].split('\n')
		longueur = len(sliced[0])

		if choix[0] == 'm':
			choix[0] = choix[1]
			mur = True

		if choix[0] == 'p':
			choix[0] = choix[1]
			percage = True

		if choix[0] == 'p':
			choix[0] = choix[1]
		if choix[0] == 's':
			nv_pos = int(poss) + int(longueur) + 1
		if choix[0] == 'n':
			nv_pos = int(poss) - int(longueur) - 1
		if choix[0] == 'e':
			nv_pos = int(poss) + 1
		if choix[0] == 'o':
			nv_pos = int(poss) - 1

		if percage is True:
			percheck = percer(nv_pos, self.grille)
			if percheck is True:
				listet = list(self.grille[0])
				listet[nv_pos] = "."
				listet = ''.join(listet)
				labfinal = Labyrinthe("X", "O", listet, self.nom, )
				return labfinal

		if mur is True:
			murok = murer(nv_pos,self.grille)
			if murok is True:
				listet = list(self.grille[0])
				listet[nv_pos] = "O"
				listet = ''.join(listet)
				labfinal = Labyrinthe("X", "O", listet, self.nom,)
				return labfinal

		obstacle = self.check_obstacle(nv_pos)
		test = str(self.grille[0]) ; test = Labyrinthe("X","O",test,self.nom)
		if obstacle is True: return test
		victoire = self.check_victoire(nv_pos)
		if victoire is True:
			listet = list(self.grille[0])
			nv_pos = self.grille[0].find("U")
			listet[nv_pos] = self.robot
			listet[poss] = " "
			listet = ''.join(listet)
			labfinal = Labyrinthe("X", "O", listet, self.nom,)
			labfinal.victoire = True
			return labfinal

		listet = list(self.grille[0])
		if self.porte is True:
			listet[nv_pos] = self.robot
			listet[poss] = "."
			listet = ''.join(listet)
			labfinal = Labyrinthe("X", "O", listet,self.nom)
			labfinal.porte = False
			return labfinal

		if listet[nv_pos] == '.': porte = True
		listet[nv_pos]=self.robot
		listet[poss] = " "
		listet = ''.join(listet)
		labfinal = Labyrinthe("X", "O", listet, self.nom)
		if porte is True : labfinal.porte = True
		return labfinal

