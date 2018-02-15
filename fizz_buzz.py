#!/usr/bin/env python


def fizz_buzz(number):
    by_3 = number % 3 == 0
    by_5 = number % 5 == 0
    response = ''

    if by_3 and by_5:
        response = 'fizz buzz'
    elif by_3:
        response = 'fizz'
    elif by_5:
        response = 'buzz'

    return response


def main(rng, verbose=False):
    if rng:
        rng += 1
    for i in range(1, rng):
        result = fizz_buzz(i)
        if verbose:
            print(f'{i}: {result}')
            continue
        if result:
            print(result)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('range', help='Positive range you would like fizz buzz to iterate through.', type=int)
    parser.add_argument('-v', '--verbose', help='Display number and response.', action='store_true')
    args = parser.parse_args()
    print(args.verbose)
    main(args.range, verbose=args.verbose)
