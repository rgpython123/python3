#!/bin/python3.6


def selection_sort(seq):
    """
    The algorithm divides the input list into two parts: the sublist of items
    already sorted, which is built up from left to right at the front (left) 
    of the list, and the sublist of items remaining to be sorted that occupy 
    the rest of the list. Initially, the sorted sublist is empty and the 
    unsorted sublist is the entire input list. The algorithm proceeds by 
    finding the smallest element in the unsorted sublist, exchanging 
    (swapping) it with the leftmost unsorted element (putting it in sorted 
    order), and moving the sublist boundaries one element to the right.    

    Takes a list as input. sorted_length is length of sorted portion.
    min_idx is the index of smallest item found. 
    
    O(n^2)
    """
    if len(seq) <= 1:
        return seq

    sorted_length = 0
    while sorted_length < len(seq):
        min_idx = None
        for index, element in enumerate(seq[sorted_length:]):
            if min_idx == None or element < seq[min_idx]:
                min_idx = index + sorted_length
        seq[sorted_length], seq[min_idx] = seq[min_idx], seq[sorted_length]
        sorted_length += 1
    return seq


def main():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("*** alist ***")
    print(alist, '\n')
    print("*** selection_sort(alist) ***")
    print(selection_sort(alist), '\n')


if __name__ == '__main__':
    main()
