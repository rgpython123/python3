#!/usr/bin/python3


def decorator_sample(func):
    
    def decorator_hook(*args, **kwargs):
        print("Before function call.")
        result = func(*args, **kwargs)
        print("After function call.")

        return result

    return decorator_hook


@decorator_sample
def product(x, y):
    return x * y


def main():
    print(product(2, 3))


if __name__ == '__main__':
    main()
