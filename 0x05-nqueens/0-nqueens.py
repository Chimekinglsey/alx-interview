#!/usr/bin/python3
"""N-Queens Solution Finder"""
import sys

solutions = []  # List of possible solutions to the N-Queens problem
n = 0  # Size of the chessboard
pos = None  # List of possible positions on the chessboard


def get_input():
    """Retrieve and validate the program's argument.
    Returns the size of the chessboard."""
    global n
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


def is_attacking(pos0, pos1):
    """Check if two queens' positions are in an attacking mode.
    Returns True if they are."""
    return (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]) or (
        abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1]))


def group_exists(group):
    """Check if a group exists in the list of solutions.
    Returns True if it exists."""
    global solutions
    return any(all(pos in stn for pos in group) for stn in solutions)


def build_solution(row, group):
    """Build a solution for the N-Queens problem."""
    global solutions, n

    if row == n:
        tmp0 = group.copy()
        if not group_exists(tmp0):
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            used_positions = any(is_attacking(pos[a], pos_b)
                                 for pos_b in group)
            if not used_positions:
                group.append(pos[a])
                build_solution(row + 1, group)
                group.pop()


def get_solutions():
    """Get solutions for the given chessboard size."""
    global pos, n
    pos = [(x // n, x % n) for x in range(n * n)]
    a = 0
    group = []
    build_solution(a, group)


n = get_input()
get_solutions()
for solution in solutions:
    print(solution)
