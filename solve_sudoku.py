# 이 함수는 주어진 스도쿠 퍼즐을 해결합니다.
# 주어진 스도쿠 퍼즐이 해결 가능한 경우에만 해결하고, 그렇지 않은 경우에는 메시지를 출력합니다.


def solve_sudoku(board):
    empty_loc = find_empty_location(board)

    if not empty_loc:
        return True
    
    row, col = empty_loc

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False
