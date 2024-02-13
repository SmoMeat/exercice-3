"""pythagorean_triples_and_armstrong_numbers.py : Imprime les tiplets pythagoriciens et les nombres d'Armstrong

Ce fichier permet d'imprimer à la console tous les triplets d'entiers pythagoriciens, c'est-à-dire qu'ils satisfont l'équation a²+b²=c²
dont l'hypothénuse est d'une longeur égale ou inférieur à c=100. De plus, ce fichier imprime à la console les nombres d'Armstrong de
trois chiffres, c'est-à-dire les nombres dont la somme de chacun des cubes de leurs chiffres vaut le nombre lui-meme.

@Date: 3 février 2024
@Author: Mathieu Ducharme
@Contact: mathieu.ducharme@umontreal.ca
@Matricule: 20297456
"""

from math import sqrt

def find_pythagorean_triples_by_ascending_while_loop(max):
    """Trouve les tiplets d'entiers pythagoriciens tels que a²+b²=c²
    où c ≤ max en utilisant une while loop itérative croissante.

    Args:
        max (int): la valeur maximale que peut prendre l'hypothénuse dans les solutions
    Returns:
        pythagorean_triples (list): contient toutes les solutions demandées sous forme de 3-uplet
    """
    pythagorean_triples = [] # Liste vierge pour accueillir les solutions
    a = b = 1

    while a <= max-2:
        while b <= max-1:
            c = sqrt(a*a + b*b)
            if c > max:
                break
            if c % 1 == 0:
                pythagorean_triples.append((a, b, int(c)))
            b += 1
        a += 1
        b = a

    return pythagorean_triples

def find_pythagorean_triples_by_descending_while_loop(max):
    """Trouve les tiplets d'entiers pythagoriciens tels que a²+b²=c²
    où c ≤ max en utilisant une while loop itérative décroissante.

    Args:
        max (int): la valeur maximale que peut prendre l'hypothénuse dans les solutions
    Returns:
        pythagorean_triples (list): contient toutes les solutions demandées sous forme de 3-uplet
    """
    pythagorean_triples = [] # Liste vierge pour accueillir les solutions
    a = b = max

    while a > 2:
        while b > 1:
            c = sqrt(a*a + b*b)
            if c % 1 == 0 and c <= max:
                pythagorean_triples.append((b, a, int(c)))
            b -= 1
        a -= 1
        b = a

    return pythagorean_triples

def find_pythagorean_triples_by_conditionned_while_loop(max):
    """Trouve les tiplets d'entiers pythagoriciens tels que a²+b²=c²
    où c ≤ max en utilisant une while loop conditionnée (do until).

    Args:
        max (int): la valeur maximale que peut prendre l'hypothénuse dans les solutions
    Returns:
        pythagorean_triples (list): contient toutes les solutions demandées sous forme de 3-uplet
    """
    pythagorean_triples = [] # Liste vierge pour accueillir les solutions
    a_below_max = b_below_max = True # Condition des while loops
    a = b = 1

    while a_below_max:
        while b_below_max:
            c = sqrt(a*a + b*b)
            if c > max:
                break
            if c % 1 == 0: # Si c est un entier
                pythagorean_triples.append((a, b, int(c)))
            b += 1
            b_below_max = b <= max-1
        a += 1
        b = a
        a_below_max = a <= max-2
        b_below_max = True

    return pythagorean_triples

def find_pythagorean_triples_by_for_loop(max):
    """Trouve les tiplets d'entiers pythagoriciens tels que a²+b²=c²
    où c ≤ max en utilisant une for loop.

    Args:
        max (int): la valeur maximale que peut prendre l'hypothénuse dans les solutions
    Returns:
        pythagorean_triples (list): contient toutes les solutions demandées sous forme de 3-uplet
    """
    pythagorean_triples = [] # Liste vierge pour accueillir les solutions

    for a in range(1, max-2):
        for b in range(a, max-1):
            c = sqrt(a*a + b*b)
            if c > max:
                break
            if c % 1 == 0:
                pythagorean_triples.append((a, b, int(c)))
    
    return pythagorean_triples

def find_armstrong_numbers():
    """Trouve tous les nombres d'Armstrong de 3 chiffres (de 100 à 999)

    Returns:
        liste de float: une liste contenant des int de tous les nombres d'Armstrong à 3 chiffres.
    """

    armstrong_numbers = []  # Liste vierge pour accueillir les nombres d'Armstrong

    # Regarde si un nombre à 3 chiffres (de 100 à 999) est un nombre d'Armstrong
    for number in range(100, 1000):
        first_digit = int(str(number)[0])   # Valeur des centaines
        second_digit = int(str(number)[1])  # Valeur des dizaines
        third_digit = int(str(number)[2])   # Valeur des unités

        if number == first_digit**3 + second_digit**3 + third_digit**3:
            armstrong_numbers.append(number)

    return armstrong_numbers

# # def debug(lists):
# #     """
# #     Permet de tester si toutes les méthodes pour trouver les triplets pythagoriciens donnent le meme résultat.
# #     À utiliser dans un but de debuggage, fonctionne seulement avec un vrai interpreteur python.
# #     """
# #     lists[0].sort()
# #     for i, list in enumerate(lists[1:]):
# #         list.sort()
# #         if lists[0] == list:
# #             print('La', str(i+2) + 'ᵉ loop donne le meme résultat que la première !')
# #         else:
# #             print('Le résultat de la première loop et de la', str(i+2) + 'ᵉ diffèrent !')

# Le programme est lancé lorsque le fichier est ouvert par lui-meme
if __name__ == '__main__':

    # Transforme une list en string en retirant les crochets '[]'
    stringied_list = lambda _list: ", ".join(map(str, _list))

    # Liste contenant les solutions des quatre méthodes
    pythagorean_triples_lists = [
        find_pythagorean_triples_by_ascending_while_loop(100),
        find_pythagorean_triples_by_descending_while_loop(100),
        find_pythagorean_triples_by_conditionned_while_loop(100),
        find_pythagorean_triples_by_for_loop(100)
    ]

    # Imprime à la console les triplets pythagoriciens
    print("Liste de triplets pythagoriciens (while-loop croissante):", stringied_list(pythagorean_triples_lists[0]), "\n")
    print("Liste de triplets pythagoriciens (while-loop décroissante):", stringied_list(pythagorean_triples_lists[1]), "\n")
    print("Liste de triplets pythagoriciens (while-loop conditionnée):", stringied_list(pythagorean_triples_lists[2]), "\n")
    print("Liste de triplets pythagoriciens (for-loop):", stringied_list(pythagorean_triples_lists[3]), "\n")

    # debug(pythagorean_triples_lists)

    # Imprime à la console les nombres d'Armstrong
    print("Les nombres d'Armstrong à 3 chiffres:", stringied_list(find_armstrong_numbers()))