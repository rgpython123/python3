#!/bin/python3.6


def fibonacci_recur(n):
    """
    Recursive: Display Fibonacci sequence.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)


def main():
    print("*** fibonacci_recur() ***")
    for i in range(11):
        print(fibonacci_recur(i), ' ', end='')
    print("\n")


if __name__ == '__main__':
    main()
