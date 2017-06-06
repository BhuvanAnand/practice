import argparse
import sys
import math

def is_palindrome(number, base=10):
    num = number
    reverse = 0
    while num > 0:
        reverse = (reverse * base) + (num % 10)
        num //= base
    return reverse == number

def largest_palindrome(num_digits, base=10):
    max_number = int( math.pow(base, num_digits) - 1)
    least_number = int( math.pow(base, num_digits - 1))
    largest = -1

    for i in range(max_number, least_number-1, -1):
        if i * i < largest:
            break
        for j in range(i, least_number-1, -1):
            value = i * j
            if value < largest:
                break
            if is_palindrome(value):
                largest = value
                break
    return largest

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Euler4.py', help='Display the largest palindrome made from product of \'num_digits\'')
    parser.add_argument('num_digits', type=int, default=3, help="Number of digits")
    args = parser.parse_args(sys.argv[1:])
    print('Largest palindrome: {0}'.format(largest_palindrome(args.num_digits)))
