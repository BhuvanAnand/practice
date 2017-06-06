import argparse
import sys
import math

def is_prime(num):
    for i in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1

    return num

def prime_factors(num, startwith=2):
    factors = list()

    while num % startwith == 0:
        factors.append(startwith)
        num //= startwith

    for at in range(next_prime(startwith + 1), int( math.sqrt(num)), startwith):
        while num % at == 0:
            factors.append(at)
            num //= at

    if num > 2:
        factors.append(num)

    return factors

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Euler3.py')
    parser.add_argument('--number', type=int, default=100, help='Print the largest prime factor for \'number\'')
    args = parser.parse_args(sys.argv[1:])

    factors = prime_factors(args.number)
    print("Prime Numbers: {0}".format(' '.join(map(lambda x: str(x), factors))))
    print("Largest Prime Factor: {0}".format(max(factors)))
