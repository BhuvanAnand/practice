import argparse
import sys

class Fibonacci():
    def __init__(self, a, b, max):
        self.a = a
        self.b = b
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        current_value = self.a
        self.a, self.b = self.b, self.a + self.b

        if current_value <= self.max:
            return current_value
        else:
            raise StopIteration

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Euler2.py')
    parser.add_argument('--max', help='Return sum of even valued numbers in fibonacci sequence less than \'max\'', type=int, default=1000)
    args = parser.parse_args(sys.argv[1:])

    fib = Fibonacci(1, 2, args.max)
    print( sum( filter( lambda x: x%2 == 0, fib)))
