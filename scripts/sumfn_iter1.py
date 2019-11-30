#!/bin/python3.6


def sumfn_iter1(seq):
    """
    Iterates through a list of numbers and returns the sum.
    """
    result = 0

    for n in seq:
        result += n

    return result


def main():
    alist = [3, 2, 1]
    print("sumfn_iter1")
    print(sumfn_iter1(alist))


if __name__ == '__main__':
    main()
