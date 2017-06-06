import sys
import argparse

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Euler5.py')
    parser.add_argument('--start', type=int, default=1, help='List of multiples starting from \'start\'')
    parser.add_argument('--end', type=int, default=20, help='List of multiples ending with \'end\'')
    args = parser.parse_args(sys.argv[1:])

    least_multiple = 1
    for at in range(args.start, args.end + 1):
        least_multiple = lcm(least_multiple, at)

    print('Least Multiple of numbers in range {0} - {1}: {2}'.format(args.start, args.end, least_multiple))
