''' Write a program to implement solveNQueens(n: int) -> List[List[str]] function taking board dimension N and
returning all valid N x N board layout configurations.'''

from typing import List
def solveNQueens(n: int) -> List[List[str]]:
    result = []
    board = [["."] * n for _ in range(n)]

    def backtrack(row):
        if row == n:
            result.append(["".join(r) for r in board])
            return

        for col in range(n):
            # Check column and diagonals
            safe = True

            for r in range(row):
                c = board[r].index("Q")

                if c == col or abs(c - col) == abs(r - row):
                    safe = False
                    break

            if safe:
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

    backtrack(0)
    return result
# Main program
n = 4
solutions = solveNQueens(n)
print("Total solutions:", len(solutions))
for solution in solutions:
    for row in solution:
        print(row)
    print()
