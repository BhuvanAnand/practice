import sys
import math
import argparse

from functools import reduce

def pythagorean_triplets(sum):
    predicate = lambda a, b, c: (sum * c + a * b) == math.floor( math.pow(sum, 2)/2)
    for a in range(1, sum):
        for b in range(a, sum - a):
            c = sum - a - b
            if predicate(a, b, c):
                return a, b, c
    return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Euler9.py', description='Pythagorean triplets')
    parser.add_argument('--sum', type=int, required=True, help='Sum of pythagorean triplets')
    args = parser.parse_args(sys.argv[1:])

    triplets = pythagorean_triplets(args.sum)
    print( reduce(lambda x, y: x * y, triplets, 1))
