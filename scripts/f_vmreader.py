#!/bin/python3.6


import sys


def vm_reader():
    while True:
        line = sys.stdin.readline()
        free_memory = line.split()[3]
        if free_memory.isdigit():
            if int(free_memory) < 333:
                print("ALERT: Free Memory ({}) is below Threshold!!!".format(free_memory))
            else:
                print("Memory OK: ({}).".format(free_memory))


def main():
    vm_reader()


if __name__ == '__main__':
    main()
