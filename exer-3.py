from datetime import datetime
import math


def find_pythagorean_triples_by_ascending_while_loop(max: int) -> [tuple]:
    pythagorean_triples = []
    a = 1
    b = 1

    while a <= max-2:
        while b <= max-1:
            c = math.sqrt(a*a + b*b)
            if c > max:
                break
            if c % 1 == 0:
                pythagorean_triples.append((a, b, c))
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
            c = math.sqrt(a*a + b*b)
            if c % 1 == 0 and c <= max:
                pythagorean_triples.append((a, b, int(c)))
            b -= 1
        a -= 1
        b = a

    return pythagorean_triples


def find_pythagorean_triples_by_ascending_for_loop(max: int) -> [tuple]:
    pythagorean_triples = []

    for a in range(1, max-2):
        for b in range(a, max-1):
            c = math.sqrt(a*a + b*b)
            if c > max:
                break
            #if c % 1 == 0:
            if c.is_integer():
                pythagorean_triples.append((a, b, int(c)))
    
    return pythagorean_triples

def find_pythagorean_triples_by_descending_for_loop(max: int) -> [tuple]:
    pythagorean_triples = []

    for a in range(1, max-2):
        for b in range(a, max-1):
            c = math.sqrt(a*a + b*b)
            if c > max:
                break
            #if c % 1 == 0:
            if c.is_integer():
                pythagorean_triples.append((a, b, int(c)))
    
    return pythagorean_triples


if __name__ == '__main__':
    start = datetime.now()
    my_list = []

    pythagorean_triples = find_pythagorean_triples_by_descending_for_loop(100)
    print(pythagorean_triples)

    print(datetime.now() - start)



# def find_pythagorean_triples_by_ascending_for_loop(max: int):
#     for b in range(1, max):
#         for a in range(1, b):
#             c = math.sqrt(a*a + b*b)
#             if c % 1 == 0:
#                 my_list.append((a, b, int(c)))
    
#     print(my_list)