#!/bin/python3.6


def binary_bisection_search(seq, n):
    """
    Performs a Binary/Bisection divide and conquer approach to searching
    for an item in a list.  O(log n).
    The list has to be sorted.
    """

    if len(seq) == 0 or (len(seq) == 1 and seq[0] != n):
        return False

    midpoint_idx = len(seq)//2
    midpoint_value = seq[midpoint_idx]

    if n == midpoint_value:
        return True
    elif n < midpoint_value:
        return binary_bisection_search(seq[:midpoint_idx], n)
    elif n > midpoint_value:
        return binary_bisection_search(seq[midpoint_idx + 1:], n)


def main():
    alist = [17, 20, 26, 31, 44, 54, 55, 77, 93]
    print("*** alist ***")
    print(alist, '\n')
    print("*** binary_bisection_search(alist, 93) ***")
    print(binary_bisection_search(alist, 93), '\n')
    print("*** binary_bisection_search(alist, 13) ***")
    print(binary_bisection_search(alist, 13), '\n')


if __name__ == '__main__':
    main()
