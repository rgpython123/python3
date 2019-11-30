#!/bin/python3.6


from random import randint


def quicksort(seq):
    """O(n log(n))"""

    if len(seq) <= 1:
        return seq

    smaller, equal, larger = [], [], []
    pivot = seq[randint(0, len(seq) - 1)]

    for x in seq:
        if x < pivot:     smaller.append(x)
        elif x == pivot:  equal.append(x)
        else:             larger.append(x)

    return quicksort(smaller) + equal + quicksort(larger)


def main():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("*** alist ***")
    print(alist, '\n')
    print("*** quicksort(alist) ***")
    print(quicksort(alist), '\n')


if __name__ == '__main__':
    main()
