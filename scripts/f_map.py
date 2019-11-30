#!/bin/python3.6


def mapfn(fn, seq):
    """
    Applies a function to each item in the list.
    """

    result = []

    for item in seq:
        result.append(fn(item))

    return result


def main():
    f = (lambda x: x * x)
    alist = [3, 2, 1]
    print(mapfn(f, alist))


if __name__ == '__main__':
    main()
