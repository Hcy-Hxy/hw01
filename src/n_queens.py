from typing import List, Optional


def is_safe(board: List[int], row: int, col: int) -> bool:
    for prev_row in range(row):
        prev_col = board[prev_row]
        if prev_col == col or abs(prev_col - col) == abs(prev_row - row):
            return False
    return True


def solve_n_queens(n: int) -> Optional[List[List[int]]]:
    solutions: List[List[int]] = []
    board: List[int] = [-1] * n

    def backtrack(row: int) -> None:
        if row == n:
            solutions.append(board.copy())
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions if solutions else None


def solve_n_queens_single(n: int) -> Optional[List[int]]:
    board: List[int] = [-1] * n

    def backtrack(row: int) -> bool:
        if row == n:
            return True
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                if backtrack(row + 1):
                    return True
                board[row] = -1
        return False

    if backtrack(0):
        return board
    return None
