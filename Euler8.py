import sys
import os
import argparse

from functools import reduce

def largest_product(number, adigits):
    if len(number) <= adigits:
        return ''.join([str(d) for d in number]), reduce(lambda x, y: x * y, number, 1)
    else:
        largest = 1
        sequence = list()
        for at in range(0, len(number) - adigits + 1):
            prod = reduce(lambda x, y: x * y, number[at: at + adigits], 1)
            if prod > largest:
                largest = prod
                sequence = number[at: at + adigits]
        return ''.join([str(d) for d in sequence]), largest

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Euler8.py')
    parser.add_argument('--file', required=True, help='File containing the number')
    parser.add_argument('--adjacent_digits', required=True, type=int, help='Number of adjacent digits whiose product is maximum')
    args = parser.parse_args(sys.argv[1:])

    number = list()
    if os.path.exists(args.file):
        with open(args.file, 'r') as fd:
            for part in fd.readlines():
                number.extend( list( map( lambda char: int(char), part.strip())))
    print( largest_product( number, args.adjacent_digits))
