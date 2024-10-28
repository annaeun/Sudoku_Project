# 이 함수는 빈 스도쿠 보드를 생성합니다.
# 스도쿠 보드는 9X9 크기의 2차원 리스트로 표현됩니다.
# 빈 칸은 0으로 표시됩니다.

def initialize_board():
    return [[0] * 9 for _ in range(9)]
