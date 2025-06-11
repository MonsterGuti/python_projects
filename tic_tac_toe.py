class InvalidNumberValueError(Exception):
    pass


class InvalidNumberRangeError(Exception):
    pass


class PositionAlreadyTakenError(Exception):
    pass


position_mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}


def read_players_data():
    f_player_name = input("Player №1 name: ")
    s_player_name = input("Player №2 name: ")
    f_player_sign = input(f"{f_player_name}, what sign do you choose - X or O? -> ").upper()

    while f_player_sign not in "XO":
        print("Your sign must be X or O: ")
        f_player_sign = input(f"{f_player_name}, what sign do you choose - X or O? -> ").upper()
    s_player_sign = "X" if f_player_sign == "O" else "O"

    print(f"{f_player_name} will play with '{f_player_sign}'")
    print(f"{s_player_name} will play with '{s_player_sign}'")

    return [(f_player_name, f_player_sign), (s_player_name, s_player_sign)]


def presenting_the_matrix():
    print("This is a numeration of the board")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")


def check_position(position, board):
    try:
        position = int(position)
    except ValueError:
        raise InvalidNumberValueError

    if position not in range(1, 10):
        raise InvalidNumberRangeError

    row_index, col_index = position_mapper[position]
    if board[row_index][col_index] != " ":
        raise PositionAlreadyTakenError
    print()
    return [row_index, col_index]


def print_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")


def is_row_winner(board, current_sign):
    for row in board:
        if row.count(current_sign) == 3:
            return True
    return False


def is_col_winner(board, current_sign):
    for col_index in range(len(board)):
        col_signs = 0
        for row_index in range(len(board)):
            if board[row_index][col_index] == current_sign:
                col_signs += 1
        if col_signs == 3:
            return True
    return False


def is_main_diagonal_winner(board, current_sign):
    sign_count = 0
    for index in range(len(board)):
        if board[index][index] == current_sign:
            sign_count += 1
    if sign_count == 3:
        return True
    return False


def is_opposite_diagonal_win(board, current_sign):
    sign_count = 0
    for index in range(len(board)):
        if board[index][len(board) - 1 - index] == current_sign:
            sign_count += 1
    if sign_count == 3:
        return True
    return False


def is_winner(board: list[list[str]], current_sign: str) -> bool:
    if is_row_winner(board, current_sign) or \
            is_col_winner(board, current_sign) or \
            is_main_diagonal_winner(board, current_sign) or \
            is_opposite_diagonal_win(board, current_sign):
        return True
    return False


my_board = [[" ", " ", " "] for _ in range(3)]

player1_data, player2_data = read_players_data()
print(f"{player1_data[0]} starts first!")

turns = 1
presenting_the_matrix()

while True:
    current_player_name, current_player_sign = player1_data if turns % 2 != 0 else player2_data
    my_position = input(f"{current_player_name}р select position between [1-9]: ")

    try:
        curr_row_index, curr_col_index = check_position(my_position, my_board)
    except(InvalidNumberValueError, InvalidNumberRangeError):
        print("Please enter a number between 1 and 9")
        continue
    except PositionAlreadyTakenError:
        print("Please select an empty position")
        continue
    else:
        my_board[curr_row_index][curr_col_index] = current_player_sign
        print_board(my_board)
        turns += 1

    if turns > 5 and is_winner(my_board, current_player_sign):
        print(f"{current_player_name} won!")
        break

    if turns == 10:
        print(f"Draw! No winner this game!")
        break
