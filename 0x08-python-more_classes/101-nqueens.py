#!/usr/bin/python3

import sys

solutions = []


def place(X, col):
    if X is None:
        return True

    current_row = len(X)

    if col in X:
        return False

    """diagonal"""
    d = 1
    for prev_row in range(current_row - 1, -1, -1):
        if X[prev_row] == col - d:
            return False
        d += 1

    """off-diagonal"""
    d = 1
    for prev_row in range(current_row - 1, -1, -1):
        if X[prev_row] == col + d:
            return False
        d += 1

    return True


def solve_nqueens(X, row, N):
    global solutions
    print(X)
    print(row)
    print(N)

    if(row == N):
        solutions += [X]
        return True

    for col in range(0, N):
        if place(X, col):
            Y = X[:]
            Y += [col]
            solve_nqueens(Y, row + 1, N)
        else:
            continue

    return False


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    for i in sys.argv[1]:
        if i < '0' or i > '9':
            print("N must be a number")
            exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)

    X = []

    N = int(sys.argv[1])

    solve_nqueens(X, 0, N)

    print(solutions)
