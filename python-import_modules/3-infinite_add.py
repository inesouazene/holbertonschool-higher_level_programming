#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = 0
    num_args = len(argv) - 1
    for i in range(num_args):
        total += int(argv[i + 1])
    print("{:d}".format(total))
