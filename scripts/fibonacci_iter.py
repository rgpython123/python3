#!/bin/python3.6

def fibonacci_iter():
    """
    Iterative: Display Fibonacci sequence using a generator.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    print("*** fibonacci_iter() ***")
    fib = fibonacci_iter()
    for i in range(11):
        print(fib.__next__(), ' ', end='')
    print("\n\n")


if __name__ == '__main__':
    main()
