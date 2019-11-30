#!/bin/python3.6


def merge(seq1, seq2):
    """
    Takes two sorted lists and merges them together.
    """

    c = []
    seq1_idx, seq2_idx = 0, 0

    while seq1_idx < len(seq1) and seq2_idx < len(seq2):
        if seq1[seq1_idx] < seq2[seq2_idx]:
            c.append(seq1[seq1_idx])
            seq1_idx += 1
        else:
            c.append(seq2[seq2_idx])
            seq2_idx += 1

    if seq1_idx == len(seq1):
        c.extend(seq2[seq2_idx:])
    elif seq2_idx == len(seq2):
        c.extend(seq1[seq1_idx:])

    return c


def merge_sort(seq):
    """
    Takes an unsorted list and implements a divide and conquer strategy
    to sort the list.  Breaks the unsorted list down to the smallest sorted
    unit.  Then repeatedly merge the sorted sublists until you create the
    full final sorted list.
    O(n log(n))
    """

    if len(seq) <= 1:
        return seq
    else:
        midpoint_idx = len(seq)//2
        left, right = merge_sort(seq[:midpoint_idx]), merge_sort(seq[midpoint_idx:])
        return merge(left, right)


def main():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("*** alist ***")
    print(alist, '\n')
    print("*** merge_sort(alist) ***")
    print(merge_sort(alist), '\n')


if __name__ == '__main__':
    main()
