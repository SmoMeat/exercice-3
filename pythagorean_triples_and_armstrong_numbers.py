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
    pythagorean_triples = []
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
    pythagorean_triples = []
    a = b = max

    while a > 2:
        while b > 1:
            c = sqrt(a*a + b*b)
            if c % 1 == 0 and c <= max:
                pythagorean_triples.append((a, b, int(c)))
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
    pythagorean_triples = []
    a_below_max = b_below_max = True
    a = b = 1

    while a_below_max:
        while b_below_max:
            c = sqrt(a*a + b*b)
            if c > max:
                break
            if c % 1 == 0:
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
    pythagorean_triples = []

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

    armstrong_numbers = []

    # Regarde si un nombre à 3 chiffres (de 100 à 999) est un nombre d'Armstrong
    for number in range(100, 1000):
        first_digit = int(str(number)[0])   # Valeur des centaines
        second_digit = int(str(number)[1])  # Valeur des dizaines
        third_digit = int(str(number)[2])   # Valeur des unités

        if number == first_digit**3 + second_digit**3 + third_digit**3:
            armstrong_numbers.append(number)

    return armstrong_numbers


# Le programme est lancé lorsque le fichier est ouvert par lui-meme
if __name__ == '__main__':
    pythagorean_triples = [
        find_pythagorean_triples_by_ascending_while_loop(100),
        find_pythagorean_triples_by_descending_while_loop(100),
        find_pythagorean_triples_by_conditionned_while_loop(100),
        find_pythagorean_triples_by_for_loop(100)
    ]

    x = [print(str(len(pythagorean_triples[i])) + '\n') for i in range(4)]
    print(pythagorean_triples)

    armstrong_numbers = find_armstrong_numbers()
    print(armstrong_numbers)