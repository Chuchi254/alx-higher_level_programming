#!/usr/bin/python3
import sys
# This script prints the number of arguments and lists them


def main():
    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print("0 arguments.")
    else:
        if argc == 1:
            print("1 argument:")
        else:
            print(f"{argc} arguments:")

        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    main()
