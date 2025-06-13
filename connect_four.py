class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


WIN_SLOTS = 4


def create_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def validate_column_choice(column, max_index_column):
    if not (0 <= column <= max_index_column):
        raise InvalidColumnError()


def place_player_choice(ma, c, player_n):
    for r in range(len(ma) - 1, -1, -1):
        if ma[r][c] == 0:
            ma[r][c] = player_n
            return r, c
    raise FullColumnError


def print_matrix(ma):
    for line in ma:
        print(line)


def is_player_num(ma, r, c, player_n):
    try:
        return ma[r][c] == player_n
    except IndexError:
        return False


def is_vertical_win(ma, r, c, player_n, slots):
    return all(is_player_num(ma, r + idx, c, player_n) for idx in range(slots))


def is_horizontal_win(ma, r, c, player_n, slots):
    filled = 1
    for idx in range(1, slots):
        if is_player_num(ma, r, c + idx, player_n):
            filled += 1
        else:
            break
    for idx in range(1, slots):
        if is_player_num(ma, r, c - idx, player_n):
            filled += 1
        else:
            break

    if filled >= 4:
        return True
    return False


def is_right_diagonal_win(ma, r, c, player_n, slots):
    filled = 1
    for idx in range(1, slots):
        if is_player_num(ma, r - idx, c + idx, player_n):
            filled += 1
        else:
            break
    for idx in range(1, slots):
        if is_player_num(ma, r + idx, c - idx, player_n):
            filled += 1
        else:
            break

    if filled >= slots:
        return True
    return False


def is_left_diagonal_win(ma, r, c, player_n, slots):
    filled = 1
    for idx in range(1, slots):
        if is_player_num(ma, r + idx, c + idx, player_n):
            filled += 1
        else:
            break
    for idx in range(1, slots):
        if is_player_num(ma, r - idx, c - idx, player_n):
            filled += 1
        else:
            break

    if filled >= slots:
        return True
    return False


def is_winner(ma, r, c, player_n, slots=WIN_SLOTS):
    return any([
        is_vertical_win(ma, r, c, player_n, slots),
        is_horizontal_win(ma, r, c, player_n, slots),
        is_right_diagonal_win(ma, r, c, player_n, slots),
        is_left_diagonal_win(ma, r, c, player_n, slots)
    ])


rows_count = 6
cols_count = 7
turns = 1
player_num = 1
matrix = create_matrix(rows_count, cols_count)

f_player = input("Player №1, please enter your name: ")
s_player = input("Player №2, please enter your name: ")
print_matrix(matrix)

players = [
    {"name": f_player, "symbol": 2},
    {"name": s_player, "symbol": 1}
]

while True:
    current = players[turns % 2 != 0]
    try:
        column_num = int(input(f"{current['name']} ({current['symbol']}), choose a column (1-{cols_count}): ")) - 1
        validate_column_choice(column_num, cols_count - 1)
        row, col = place_player_choice(matrix, column_num, current["symbol"])
        print_matrix(matrix)
        if is_winner(matrix, row, col, current["symbol"]):
            print(f"{current['name']} won the game!")
            break
    except InvalidColumnError:
        print(f"Please, enter a valid column position between 1 and {cols_count}.")
    except FullColumnError:
        print("The column is full! Choose other position.")
    except ValueError:
        print("Please enter a valid number!")

    turns += 1

    if turns == rows_count * cols_count:
        print("Game over! DRAW!")
        break
