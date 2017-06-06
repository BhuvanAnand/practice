import sys
import argparse
import math

def sum_natural(num):
    return num * (num + 1) / 2

def sum_squares(num):
    return num * (num + 1) * (2 * num + 1) / 6

def sum_cubes(num):
    return math.pow(num, 2) * math.pow(num+1, 2) / 4

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Euler6.py')
    parser.add_argument('--number', type=int, default=10, help='Number whose sums square difference tobe found')
    args = parser.parse_args(sys.argv[1:])
    difference = math.pow(sum_natural(args.number), 2) - sum_squares(args.number)
    print('Sum Square Difference of {0}: {1}'.format(args.number, int(difference)))
