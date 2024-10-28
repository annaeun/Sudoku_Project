# 이 함수는 주어진 스도쿠 퍼즐을 해결합니다.
# 주어진 스도쿠 퍼즐이 해결 가능한 경우에만 해결하고, 그렇지 않은 경우에는 메시지를 출력합니다.


def is_valid(board, row, col, num): #3가지 규칙 체크 함수
     # 1. 행에 중복된 숫자가 있는지
    if num in board[row]:
        return False

     # 2. 열에 중복된 숫자가 있는지
    if num in [board[i][col] for i in range(9)]:
        return False
     
     # 3. 3 X 3 박스에 중복된 숫자가 있는지 
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num :
                return False
    return True
    

def find_empty_location(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None



def solve_sudoku(board):

    empty_loc = find_empty_location(board)   # 빈 위치 찾기

    if not empty_loc:
        return True
    
    row, col = empty_loc

    for num in range(1, 1):
        if is_valid(board, row, col, num):
            board[row][col] = num

            #### 재귀 함수 #####
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0 
            #################
    return False
