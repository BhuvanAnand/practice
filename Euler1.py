import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Euler1.py', description='''

    Eg: python Euler1.py --numbers 3 5 --lt 1000 --sum
        233168
    ''')
    parser.add_argument('--numbers', type=int, nargs='+', help='List of integers', required=True)
    parser.add_argument('--lt', type=int, help='Consider multiples less than "lt"', default=100)
    parser.add_argument('--sum', dest='action', action='store_const', const=sum, default=max, help='Action to be done on the list of multiples')

    args = parser.parse_args(sys.argv[1:])
    args.numbers = sorted(args.numbers)
    predicate = lambda x: any( map( lambda multiple: x % multiple == 0, args.numbers))
    result = args.action([x for x in range(args.numbers[0], args.lt) if predicate(x)])
    print(result)
