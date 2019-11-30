#!/bin/python3.6


def bubble_sort(seq):
    """
    Repeatedly iterate through a list swapping values that are not in order.
    O(n^2)
    """
    if len(seq) <= 1:
        return seq

    _sorted = False

    while not _sorted:
        _sorted = True
        for index in range(1, len(seq)):
            if seq[index] < seq[index - 1]:
                _sorted = False
                seq[index], seq[index - 1] = seq[index - 1], seq[index]
    return seq


def main():
    alist = [54,26,93,17,77,31,44,55,20]
    print("*** alist ***")
    print(alist, '\n')
    print("*** bubble_sort(alist) ***")
    print(bubble_sort(alist), '\n')


if __name__ == '__main__':
    main()
