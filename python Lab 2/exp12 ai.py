board = [' '] * 9

def show():
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

player = 'X'
for _ in range(9):
    show()
    pos = int(input(f"{player} Position (0-8): "))
    if board[pos] == ' ':
        board[pos] = player
        player = 'O' if player == 'X' else 'X'

show()