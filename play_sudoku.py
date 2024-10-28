# 이 함수는 사용자에게 스도쿠 게임을 플레이할 기회를 제공합니다.
# 게임은 사용자가 잘못된 이동을 하거나 스도쿠를 완성할 때까지 진행됩니다.

def play_sudoku():
    board = generate_sudoku()
    solved_board = [row[:] for row in board]  # 정답 보드 복사
    solve_sudoku(solved_board)  # 정답을 구함

    print("스도쿠 게임을 시작합니다!")
    while True:
        print_board(board)
        try:
            row = int(input("행을 입력하세요 (1-9): ")) - 1
            col = int(input("열을 입력하세요 (1-9): ")) - 1
            num = int(input("숫자를 입력하세요 (1-9): "))

            if board[row][col] != 0:
                print("이미 숫자가 있는 칸입니다. 게임을 종료합니다.")
                continue

            if is_valid(board, row, col, num):
                board[row][col] = num
                if all(0 not in row for row in board):
                    print("축하합니다! 스도쿠를 완료했습니다!")
                    break
            else:
                print("잘못된 이동입니다.")

        except ValueError:
            print("유효하지 않은 입력입니다. 숫자를 입력해야 합니다. 게임을 종료합니다.")
            break
