#!/usr/bin/python3
"""N-queens problem solver"""

import sys


def is_safe(board, row, col):
    """Check if a position is safe for a queen"""
    # Check the same row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on left side
    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    # If none of the above conditions are violated, return true
    return True


def print_board(board):
    """Print the board configuration in a specific format"""
    # Create an empty list to store the positions of the queens
    positions = []

    # Loop over the board and append the positions of the queens to the list
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                positions.append([i, j])

    # Print the list of positions
    print(positions)


def solve_n_queens(board, col):
    """Solve the n-queens problem and print all solutions"""
    # If all queens are placed, print the board and return true
    if col == n:
        print_board(board)
        return True

    # Initialize a variable to store the result
    res = False

    # Try placing a queen in all rows of the current column
    for i in range(n):
        # Check if the position is safe for a queen
        if is_safe(board, i, col):
            # Place the queen on the board
            board[i][col] = 1

            # Recur to place the rest of the queens and set res
            # to true if any solution is found
            res = solve_n_queens(board, col + 1) or res

            # Backtrack and remove the queen from the board
            board[i][col] = 0

    # Return the final result
    return res


# Checking if the user called the program with the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Getting the value of n from the command line argument
# and checking if it is an integer greater or equal to 4
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

# Creating an empty n x n board
board = [[0 for i in range(n)] for j in range(n)]

# Calling the function to solve the n-queens problem and print all solutions
if not solve_n_queens(board, 0):
    print("No solution exists for n =", n)
