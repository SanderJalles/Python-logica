def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def check_winner(board):

    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]


    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]


    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    current_player = "X"
    winner = None

    while not winner and not is_board_full(board):
        print_board(board)

        row = int(input("Digite o número da linha (0, 1 ou 2): "))
        col = int(input("Digite o número da coluna (0, 1 ou 2): "))

        if board[row][col] != " ":
            print("Essa posição já está ocupada. Tente novamente.")
            continue

        board[row][col] = current_player
        winner = check_winner(board)

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    print_board(board)

    if winner:
        print("Parabéns, o jogador", winner, "venceu!")
    else:
        print("Empate!")

play_game()