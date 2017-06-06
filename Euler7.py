import sys
import argparse
import Euler3
from math import log as ln
from math import floor, ceil

def nth_prime(num):
    primes = list()
    if num < 6:
        start = 2
        for at in range(num-1):
            start = Euler3.next_prime(start)
        return primes.append(start)
    else:
        common = ln(num) + ln( ln(num))
        low = floor( num * (common - 1))
        high = ceil( num * common)

        print('High: {0}, Low:{1}'.format(high, low))

        for num in range(low, high):
            if Euler3.is_prime(num):
                primes.append(num)

    return primes

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Euler7.py', description='Using Rossner\'s theorem')
    parser.add_argument('--num', type=int, default=10, help='\'num\'th prime number tobe found')
    args = parser.parse_args(sys.argv[1:])
    print('{0}\'th prime number: {1}'.format(args.num, nth_prime(args.num)))
