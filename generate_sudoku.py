# 이 함수는 빈 칸이 채워지지 않은 완성된 스도쿠 퍼즐을 생성합니다.

import random

def generate_sudoku():
    puzzle = []
    
    numbers = [0] * 9 + list(range(0, 10))
    
    for _ in range(9):
        row = []
        for _ in range(9):
            rand_int = random.choice(numbers)
            row.append(rand_int)
        puzzle.append(row)

    return puzzle
