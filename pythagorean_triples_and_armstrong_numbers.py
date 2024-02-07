"""pythagorean_triples_and_armstrong_numbers.py : Imprime les tiplets pythagoriciens et les nombres d'Armstrong

Ce fichier permet d'imprimer à la console tous les triplets d'entiers pythagoriciens dont l'hypothénuse est d'une
longeur égale ou inférieur à c=100. De plus, ce fichier imprime à la console les nombres d'Armstrong de trois
chiffres, c'est-à-dire les nombres dont la somme de chacun des cubes de leurs chiffres vaut le nombre lui-meme.

@Date: 3 février 2024
@Author: Mathieu Ducharme
@Contact: mathieu.ducharme@umontreal.ca
@Matricule: 20297456
"""

from math import sqrt


def find_pythagorean_triples_by_ascending_while_loop(max: int) -> [tuple]:
    pythagorean_triples = []
    a = 1
    b = 1

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

def find_pythagorean_triples_by_descending_while_loop(max: int) -> [tuple]:
    pythagorean_triples = []
    a = max
    b = a

    while a > 2:
        while b > 1:
            c = sqrt(a*a + b*b)
            if c % 1 == 0 and c <= max:
                pythagorean_triples.append((a, b, int(c)))
            b -= 1
        a -= 1
        b = a

    return pythagorean_triples

def find_pythagorean_triples_by_conditionned_while_loop(max: int) -> [tuple]:
    pythagorean_triples = []
    a_below_max = True
    b_below_max = True
    a = 1
    b = 1
    print('ok1')
    while a_below_max:
        while b_below_max:
            c = sqrt(a*a + b*b)
            if c > max:
                break
            if c % 1 == 0:
                pythagorean_triples.append((a, b, c))
            b += 1
            b_below_max = b <= max-1
        a += 1
        b = a
        a_below_max = a <= max-2
        b_below_max = True

    return pythagorean_triples

def find_pythagorean_triples_by_for_loop(max: int) -> [tuple]:
    pythagorean_triples = []

    for a in range(1, max-2):
        for b in range(a, max-1):
            c = sqrt(a*a + b*b)
            if c > max:
                break
            #if c % 1 == 0:
            if c.is_integer():
                pythagorean_triples.append((a, b, int(c)))
    
    return pythagorean_triples

def find_armstrong_numbers():
    """
    Cette fonction retourne une liste contenant tous les nombres d'Armstrong à 3 chiffres.
    Returns:
        liste de float: une liste contenant des int de tous les nombres d'Armstrong à 3 chiffres.
    """

    armstrong_numbers = []

    # Regarde si un nombre à 3 chiffres (de 100 à 999) est un nombre d'Armstrong
    for number in range(100, 1000):
        first_digit = int(str(number)[0])
        second_digit = int(str(number)[1])
        third_digit = int(str(number)[2])
        if number == first_digit**3 + second_digit**3 + third_digit**3:
            armstrong_numbers.append(number)

    return armstrong_numbers



if __name__ == '__main__':

    pythagorean_triples1 = find_pythagorean_triples_by_ascending_while_loop(100)
    pythagorean_triples2 = find_pythagorean_triples_by_descending_while_loop(100)
    pythagorean_triples3 = find_pythagorean_triples_by_conditionned_while_loop(100)
    pythagorean_triples4 = find_pythagorean_triples_by_for_loop(100)

    pythagorean_triples = [pythagorean_triples1, pythagorean_triples2, pythagorean_triples3, pythagorean_triples4]

    x = [print(str(len(pythagorean_triples[i])) + '\n') for i in range(4)]
    #(pythagorean_triples1, pythagorean_triples2, pythagorean_triples3, pythagorean_triples4)

    armstrong_numbers = find_armstrong_numbers()
    print(armstrong_numbers)