#!/usr/bin/python3
import sys
# This script prints the result of the addition of all arguments


def main():
    argv = sys.argv[1:]
    result = sum(int(arg) for arg in argv)
    print(result)


if __name__ == "__main__":
    main()
