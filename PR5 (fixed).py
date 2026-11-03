def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


def is_safe(board, row, col, n):
    # Check row on both left and right
    for j in range(n):
        if j != col and board[row][j] == 1:
            return False

    # Check column on both up and down
    for i in range(n):
        if i != row and board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower-left diagonal
    i, j = row + 1, col - 1
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    # Check lower-right diagonal
    i, j = row + 1, col + 1
    while i < n and j < n:
        if board[i][j] == 1:
            return False
        i += 1
        j += 1

    return True


def solve_n_queens_with_first_placed(board, col, n, first_col):
    # If all columns are processed, return True
    if col >= n:
        return True

    # If this column already has the first queen placed, skip to next column
    if col == first_col:
        return solve_n_queens_with_first_placed(board, col + 1, n, first_col)

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_n_queens_with_first_placed(board, col + 1, n, first_col):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter dimension N of board: "))
    board = [[0 for _ in range(n)] for _ in range(n)]

    print(f"Enter position for the 1st Queen (0 to {n-1}):")
    first_row = int(input("Row: "))
    first_col = int(input("Column: "))

    board[first_row][first_col] = 1

    print("\nInitial Board:")
    print_board(board, n)

    if solve_n_queens_with_first_placed(board, 0, n, first_col):
        print("\nFinal Solution Matrix:")
        print_board(board, n)
    else:
        print("\nNo solution exists with the first queen placed at this position.")
