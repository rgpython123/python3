#!/bin/python3.6


import time


def insertion_sort(seq):
    """
    The algorithm iterates, consuming one input element each repetition, and 
    growing a sorted output list.  At each iteration, insertion sort removes 
    one element from the input data, finds the location it belongs within the 
    sorted list, and inserts it there. It repeats until no input elements 
    remain.

    Takes a list as input. sorted_length is length of sorted portion.

    O(n^2)
    """
    if len(seq) <= 1:
        return seq

    for sorted_length in range(1, len(seq)):

        insert_idx = sorted_length

        while insert_idx > 0 and seq[insert_idx] < seq[insert_idx - 1]:
            seq[insert_idx], seq[insert_idx - 1] = seq[insert_idx - 1], seq[insert_idx]
            insert_idx -= 1

    return seq


def insertion_sort_words(seq):
    """
    Takes a list of words and sorts them by thier first letter.
    O(n^2)
    """
    if len(seq) <= 1:
        return seq
    
    for sorted_length in range(1, len(seq)):

        insert_idx = sorted_length

        while insert_idx > 0 and seq[insert_idx][0] < seq[insert_idx - 1][0]:
            seq[insert_idx], seq[insert_idx - 1] = seq[insert_idx - 1], seq[insert_idx]
            insert_idx -= 1

    return seq


def insertion_sort_last_names(seq):
    """
    Takes a list of First and Last names and sorts them by last name.
    O(n^2)
    """
    if len(seq) <= 1:
        return seq

    for sorted_length in range(1, len(seq)):

        insert_idx = sorted_length

        while insert_idx > 0 and seq[insert_idx].split()[1][0] < seq[insert_idx - 1].split()[1][0]:
            seq[insert_idx], seq[insert_idx - 1] = seq[insert_idx - 1], seq[insert_idx]
            insert_idx -= 1

    return seq


def main():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("*** alist ***")
    print(alist, '\n')
    print("*** insertion_sort(alist) ***")
    print(insertion_sort(alist), '\n')

    time.sleep(1)

    words = ['zulu', 'foxtrot', 'alpha']
    print("*** words ***")
    print(words, '\n')
    print("*** insertion_sort_words(words) ***")
    print(insertion_sort(words), '\n')

    time.sleep(1)

    names = ['Adam Zysk', 'Jane Doe', 'Zeke Abbott']
    print("*** names ***")
    print(names, '\n')
    print("*** insertion_sort_last_names(names) ***")
    print(insertion_sort_last_names(names), '\n')


if __name__ == '__main__':
    main()
