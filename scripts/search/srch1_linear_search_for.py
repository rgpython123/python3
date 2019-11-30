#!/bin/python3.6


import time


def linear_sequential_search_for_1(seq, item):
    """
    O(n)
    Searches entire list for multiple matches.
    """

    found = False

    for index in range(len(seq)):
        if seq[index] == item:
            found = True
            print("Index: {}".format(index))

    return found


def linear_sequential_search_for_2(seq, item):
    """
    O(n)
    Searches list until it finds a match and then exits.
    """

    found = False

    for index in range(len(seq)):
        if seq[index] == item:
            found = True
            print("Index: {}".format(index))
            if found:
                return found

    return found


def main():
    alist = [1, 2, 32, 13, 8, 17, 19, 42, 13, 0]
    print("*** alist ***")
    print(alist, '\n')
    print("*** linear_sequential_search_for_1(alist, 3) ***")
    print(linear_sequential_search_for_1(alist, 3), '\n')
    print("*** linear_sequential_search_for_1(alist, 13) ***")
    print(linear_sequential_search_for_1(alist, 13), '\n')

    print('\n')
    time.sleep(1)

    alist = [1, 2, 32, 13, 8, 17, 19, 42, 13, 0]
    print("*** alist ***")
    print(alist, '\n')
    print("*** linear_sequential_search_for_2(alist, 3) ***")
    print(linear_sequential_search_for_2(alist, 3), '\n')
    print("*** linear_sequential_search_for_2(alist, 13) ***")
    print(linear_sequential_search_for_2(alist, 13), '\n')


if __name__ == '__main__':
    main()
