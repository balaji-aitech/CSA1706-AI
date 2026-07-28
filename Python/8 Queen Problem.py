N = 8

# Create an empty 8x8 chessboard filled with 0s
# 0 = Empty cell, 1 = Queen placed
board = [[0 for _ in range(N)] for _ in range(N)]

# Function to check whether a queen can be placed safely
def isSafe(board, row, col):

    # Check the left side of the current row
    for i in range(col):
        if board[row][i]:
            return False

    # Check the upper-left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check the lower-left diagonal
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    # Safe position found
    return True

# Recursive function to solve the problem using Backtracking
def solve(board, col):

    # Base case: If all queens are placed successfully
    if col >= N:
        return True

    # Try placing the queen in each row of the current column
    for i in range(N):

        # Check if placing the queen is safe
        if isSafe(board, i, col):

            # Place the queen
            board[i][col] = 1

            # Recursively place queens in the next column
            if solve(board, col + 1):
                return True

            # Backtracking:
            # Remove the queen if it doesn't lead to a solution
            board[i][col] = 0

    # No valid position found in this column
    return False

# Start solving from the first column (column 0)
if solve(board, 0):

    # Print the solution
    print("Solution:")
    for row in board:
        print(row)

else:
    # If no solution exists
    print("Solution does not exist")
