def check_winner(board):
    n = len(board)
    for i in range(n):
        # Проверка строк
        if board[i] == ['X'] * n:
            return 'X'
        elif board[i] == ['O'] * n:
            return 'O'

        # Проверка столбцов
        if [board[j][i] for j in range(n)] == ['X'] * n:
            return 'X'
        elif [board[j][i] for j in range(n)] == ['O'] * n:
            return 'O'

    # Проверка диагоналей
    if [board[i][i] for i in range(n)] == ['X'] * n:
        return 'X'
    elif [board[i][i] for i in range(n)] == ['O'] * n:
        return 'O'
    if [board[i][n - i - 1] for i in range(n)] == ['X'] * n:
        return 'X'
    elif [board[i][n - i - 1] for i in range(n)] == ['O'] * n:
        return 'O'

    return 'Ничья'
board = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['_', '_', 'X']
]

winner = check_winner(board)
print(f"Победитель: {winner}")