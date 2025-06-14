import tkinter as tk


class FullColumnError(Exception):
    pass


WIN_SLOTS = 4


def create_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def place_player_choice(ma, c, player_n):
    for r in range(len(ma) - 1, -1, -1):
        if ma[r][c] == 0:
            ma[r][c] = player_n
            return r, c
    raise FullColumnError


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
    return filled >= slots


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
    return filled >= slots


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
    return filled >= slots


def is_winner(ma, r, c, player_n, slots=WIN_SLOTS):
    return any([
        is_vertical_win(ma, r, c, player_n, slots),
        is_horizontal_win(ma, r, c, player_n, slots),
        is_right_diagonal_win(ma, r, c, player_n, slots),
        is_left_diagonal_win(ma, r, c, player_n, slots)
    ])


def handle_column_click(ma, labels, column_num, player_num, counter, rows, cols, slots_to_win, info_label, buttons):
    try:
        row, col = place_player_choice(ma, column_num, player_num)
        color = "red" if player_num == 1 else "blue"
        labels[row][col].config(bg=color)

        if is_winner(ma, row, col, player_n=player_num, slots=slots_to_win):
            info_label.config(text=f"Player {player_num} wins!", fg=color)
            disable_all_buttons(buttons)
            return player_num, counter

        counter += 1
        if counter == rows * cols:
            info_label.config(text="Draw!", fg="black")
            disable_all_buttons(buttons)
            return player_num, counter

        next_player = 2 if player_num == 1 else 1
        info_label.config(text=f"Player {next_player}'s turn")
        return next_player, counter

    except FullColumnError:
        info_label.config(text="Column is full! Choose another one.", fg="orange")
        return player_num, counter


def disable_all_buttons(buttons):
    for btn in buttons:
        btn.config(state="disabled")


def create_ui(root, rows, cols, slots_to_win):
    root.grid_rowconfigure(tuple(range(rows + 3)), weight=1)
    root.grid_columnconfigure(tuple(range(cols)), weight=1)

    matrix = create_matrix(rows, cols)
    labels = [[tk.Label(root, text=" ", bg="white", relief="solid", font=("Arial", 20))
               for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            labels[r][c].grid(row=r + 1, column=c, sticky="nsew", padx=1, pady=1)

    game_state = {"player_num": 1, "counter": 0}

    info_label = tk.Label(root, text="Player 1's turn", font=("Arial", 18))
    info_label.grid(row=rows + 2, column=0, columnspan=cols, sticky="nsew")

    buttons = []

    def make_click_handler(column_num, btns):
        return lambda: (
            game_state.update({
                "player_num": handle_column_click(
                    matrix, labels, column_num,
                    game_state["player_num"], game_state["counter"],
                    rows, cols, slots_to_win, info_label, btns
                )[0],
                "counter": game_state["counter"] + 1 if matrix[0][column_num] == 0 else game_state["counter"]
            })
        )

    for col in range(cols):
        btn = tk.Button(root, text="↓", font=("Arial", 16), bg="yellow")
        btn.config(command=make_click_handler(col, buttons))
        btn.grid(row=0, column=col, sticky="nsew", padx=1, pady=1)
        buttons.append(btn)


def start_game():
    root = tk.Tk()
    root.title("Connect Four")
    root.state("zoomed")
    rows, cols, slots_to_win = 6, 7, 4
    create_ui(root, rows, cols, slots_to_win)
    root.mainloop()


if __name__ == "__main__":
    start_game()
