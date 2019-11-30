#!/bin/python3.6


def sumfn_iter2(seq):
    """
    Iterates through a list of numbers and returns the sum.
    """
    index = len(seq) - 1

    result = 0
    while index >= 0:
        result += seq[index]
        index -= 1

    return result


def main():
    alist = [3, 2, 1]
    print("sumfn_iter2")
    print(sumfn_iter2(alist))


if __name__ == '__main__':
    main()
