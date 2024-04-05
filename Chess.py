import pandas as pd
import time

def is_safe(chess_board, row, col):
    # Проверка вертикали
    for i in range(row):
        if chess_board[i][col] == 'Q':
            return False

    # Проверка главной диагонали
    i, j = row, col
    while i >= 0 and j >= 0:
        if chess_board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Проверка побочной диагонали
    i, j = row, col
    while i >= 0 and j < 8:
        if chess_board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def atack_queens(chess_board, row):
    if row == 8:
        return True

    for col in range(8):
        if is_safe(chess_board, row, col):
            chess_board[row][col] = 'Q'
            if atack_queens(chess_board, row + 1):
                return True
            chess_board[row][col] = '*'

    return False

chess_board = [['*' for i in range(8)] for j in range(8)]

start_time_chess = time.perf_counter()
if atack_queens(chess_board, 0):
    print("Размещение 8 ферзей на шахматной доске:")
    chess_board = pd.DataFrame(chess_board)
    chess_board.index = ['8', '7', '6', '5', '4', '3', '2', '1']
    chess_board.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    print(chess_board)
finish_time_chess = time.perf_counter() - start_time_chess
print("\nВремя выполнения")
print("--- {0} ms ---\n".format(round(finish_time_chess * 1000)))

