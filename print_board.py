# 이 함수는 현재 스도쿠 보드를 출력합니다.

def print_board(board):
    for row in board:
        print(" ".join(map(str, row))) 
