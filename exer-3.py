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

def find_armstrong_numbers():
    armstrong_numbers = []

    for number in range(100, 1000):
        first_digit = int(str(number)[0])
        second_digit = int(str(number)[1])
        third_digit = int(str(number)[2])
        if number == first_digit**3 + second_digit**3 + third_digit**3:
            armstrong_numbers.append(number)

    return armstrong_numbers



if __name__ == '__main__':
    start = datetime.now()

    #pythagorean_triples = find_pythagorean_triples_by_descending_for_loop(100)
    #print(pythagorean_triples)

    armstrong_numbers = find_armstrong_numbers()
    print(armstrong_numbers)

    print(datetime.now() - start)