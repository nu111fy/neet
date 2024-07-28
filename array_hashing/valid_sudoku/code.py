class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets to keep track of numbers in each row, column, and 3x3 square
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        # Iterate through each cell in the 9x9 board
        for i in range(9):
            for j in range(9):
                # Skip empty cells (represented by '.')
                if board[i][j] == '.':
                    continue

                # Check if the number already exists in the current row, column, or 3x3 square
                if (board[i][j] in rows[i]) or \
                   (board[i][j] in cols[j]) or \
                   (board[i][j] in squares[i//3][j//3]):
                    return False

                # If the number is valid, add it to the corresponding sets
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[i//3][j//3].add(board[i][j])

        # If we've made it through all checks, the board is valid
        return True
