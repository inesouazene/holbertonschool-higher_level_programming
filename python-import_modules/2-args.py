#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_args = len(argv) - 1
    if num_args > 0:
        if num_args == 1:
            print("{:d} argument:\n1: {:s}".format(num_args, argv[1]))
        else:
            print("{:d} arguments:".format(num_args))
            for i in range(num_args):
                print("{:d}: {:s}".format(i + 1, argv[i + 1]))
    else:
        print("{:d} arguments.".format(num_args))
