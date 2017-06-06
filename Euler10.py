import argparse
import sys
import math

import Euler3

class PrimeGenerator():
    def __init__(self, start=2, max=None):
        self.current = start
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.max and self.current >= self.max:
            raise StopIteration
        else:
            present = self.current
            self.current = Euler3.next_prime(present)
            return present

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Euler10.py')
    parser.add_argument('--number', type=int, default=100, help='Print the sum of all primes below \'number\'')
    args = parser.parse_args(sys.argv[1:])

    prime_gen = PrimeGenerator(max=args.number)
    prime_sum = sum(prime_gen)
    print("Sum of prime numbers less than {0}: {1}".format(args.number, prime_sum))
