#!/usr/bin/python3
"""
Solves the N queens problems.
"""


import sys


def print_usage_and_exit():
    """Prints the usage message and exits with status 1."""
    print("Usage: nqueens N")
    sys.exit(1)


def print_number_error_and_exit():
    """Prints the number error message and exits with status 1."""
    print("N must be a number")
    sys.exit(1)


def print_size_error_and_exit():
    """Prints the size error message and exits with status 1."""
    print("N must be at least 4")
    sys.exit(1)


def is_safe(board, row, col):
    """Checks if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens(board, col, solutions):
    """Uses backtracking to solve the N queens problem."""
    if col >= len(board):
        solutions.append([[i, row.index(1)] for i, row in enumerate(board)])
        return
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1, solutions)
            board[i][col] = 0


def main():
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_number_error_and_exit()

    if N < 4:
        print_size_error_and_exit()

    board = [[0 for _ in range(N)] for _ in range(N)]
    soltuions = []
    solve_nqueens(board, 0, solutions)
    for solution in solutions:
        print(solution)

    if __name__ == "__main__":
        main()
