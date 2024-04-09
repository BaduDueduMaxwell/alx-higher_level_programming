#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """ Check if it's safe to place a queen at board[row][col] """

    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check for queens in the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check for queens in the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, row, N, solutions):
    """ Recursive utility function to solve N Queens problem """

    # If all queens are placed, add the solution to the list of solutions
    if row == N:
        queens_positions = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    queens_positions.append([i, j])
        solutions.append(queens_positions)
        return

    # Try placing a queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            # Place the queen
            board[row][col] = 1

            # Recur to place queens in the remaining rows
            solve_nqueens_util(board, row + 1, N, solutions)

            # Backtrack and remove the queen from this position
            board[row][col] = 0


def solve_nqueens(N):
    """ Solve N Queens problem """

    # Initialize the chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    # Start with the first row and solve recursively
    solve_nqueens_util(board, 0, N, solutions)

    return solutions


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem
    solutions = solve_nqueens(N)

    # Print each solution
    for sol in solutions:
        print(sol)
