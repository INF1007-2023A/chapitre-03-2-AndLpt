#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	P = (float(voltage) ** 2) / float(resistance)
	return P


def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	v1[0] # Pour accéder au X
	v1[1] # Pour accéder au Y
	pass

	# calcul de la norme des vecteurs
	scalaire = v1[0] * v2[0] + v1[1] * v2[1]
	return scalaire == 0
	

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	liste_positive = list()
	compte = 0;
	pass # La variable v contient une valeur de la liste.
	for v in values:
		if v >= 0:
			liste_positive.append(v)
			compte += 1
	moyenne = sum(liste_positive) / compte
	return moyenne

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties = value // 20
	reste1 = value % 20
	tens = reste1 // 10
	reste2 = reste1 % 10
	fives = reste2 // 5
	reste3 = reste2 % 5
	ones = reste3 
	

	return (twenties, tens, fives, ones);

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		index = abs_value % base
		liste.append(letters[index])
		abs_value //= base
		value // base
	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		pass
	return result


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(-42, 16, "0123456789ABCDEF"))
