# 이 함수는 빈 칸이 채워지지 않은 완성된 스도쿠 퍼즐을 생성합니다.

import random

def generate_sudoku():
    board = initialize_board()
    solve_sudoku(board)

    for _ in range(40):
        row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0

    return board
