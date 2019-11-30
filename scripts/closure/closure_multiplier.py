#!/usr/bin/python3

def multiplier(num):

    def product(number):
        """This is a closure."""
        return num * number

    return product


def main():
    num2 = multiplier(2)
    print(num2(11))

    num3 = multiplier(3)
    print(num3(11))


if __name__ == '__main__':
    main()
