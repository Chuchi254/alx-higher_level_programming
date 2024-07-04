#!/usr/bin/python3
import sys
import importlib.util

# This script prints all the names defined by the compiled module hidden_4.pyc


def main():
    spec = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    names = dir(hidden_4)

    filtered_names = [name for name in names if not name.startswith("__")]

    for name in sorted(filtered_names):
        print(name)


if __name__ == "__main__":
    main()
