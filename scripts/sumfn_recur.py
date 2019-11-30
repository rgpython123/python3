#!/bin/python3.6


def sumfn_recur(seq):
    """
    Using Recursion, sum a list of numbers.
    """
    if len(seq) == 0:
        return 0
    else:
        return seq[0] + sumfn_recur(seq[1:])


def main():
    alist = [3, 2, 1]
    print("sumfn_recur")
    print(sumfn_recur(alist))


if __name__ == '__main__':
    main()
