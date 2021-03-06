"""
Tic-tac-toe solver using minimax algorithm
"""

MAX: str  # X or O
MIN: str  # X or O

# Empty board
grid = {
    0: ' ', 1: ' ', 2: ' ',
    3: ' ', 4: ' ', 5: ' ',
    6: ' ', 7: ' ', 8: ' '}


def draw_grid():
    """Draw's the Tic-tac-toe grid"""

    print(end=None)

    for i, spot in grid.items():
        if (i + 1) % 3 == 0 and grid.get(i + 3):
            print(spot, end=f"\n{'-'*9}\n")
        elif (i - 1) % 3 == 0:
            print(f" | {spot} | ", end="")
        else:
            print(spot, end="")

    print(end=None)


def result():
    """Check if the game has been won, lost or tied"""

    positions = {MAX: set(), MIN: set()}
    col1, col2, col3 = {0, 3, 6}, {1, 4, 7}, {2, 5, 8}
    row1, row2, row3 = {0, 1, 2}, {3, 4, 5}, {6, 7, 8}
    diag1, diag2 = {0, 4, 8}, {2, 4, 6}
    wins = [col1, col2, col3, row1, row2, row3, diag1, diag2]

    for i, spot in grid.items():
        if spot == MAX: positions[MAX].add(i)
        elif spot == MIN: positions[MIN].add(i)

    for win in wins:
        if win.issubset(positions[MAX]): return +1
        elif win.issubset(positions[MIN]): return -1

    if " " not in grid.values():
        return 0


def minimax(depth: int, maximizing: bool):
    """Minimax algorithm with alpha-beta pruning"""

    if result() is not None:
        return result()

    best_score = float("-inf") if maximizing else float("inf")
    for i, spot in grid.items():
        if spot != " ": continue

        if maximizing:
            grid[i] = MAX
            score = minimax(depth + 1, False)
            grid[i] = " "
            if score > best_score: best_score = score

        if not maximizing:
            grid[i] = MIN
            score = minimax(depth + 1, True)
            grid[i] = " "
            if score < best_score: best_score = score

    return best_score


def get_chioce():
    """Get user's choice"""

    global MAX, MIN

    choice = input("\nChoose between 'X' and 'O': ").strip().upper()
    while choice not in {"X", "O"}:
        choice = input("Invalid choice, choose again: ").strip().upper()
    MIN = choice
    MAX = "O" if MIN == "X" else "X"


def get_move():
    """Get user's move"""

    move = input("\nEnter your move: ").strip()
    i = 0
    while i != 2:
        i = 0
        if move.isnumeric():
            move = int(move) - 1
            i += 1
        if grid.get(move, None) == " ":
            i += 1
        else:
            move = input("Invalid move, try again: ")

    return move


def ai_move():
    """AI's move"""

    best_score = float("-inf")
    best_move = 0
    for i, spot in grid.items():
        if spot != " ": continue
        grid[i] = MAX
        score = minimax(0, maximizing=False)
        grid[i] = " "
        if score > best_score: best_score, best_move = score, i

    return best_move


def main():
    """Alternate between AI and user moves"""

    get_chioce()
    print(f"\n1 | 2 | 3\n{'-'*9}\n4 | 5 | 6\n{'-'*9}\n7 | 8 | 9")

    while True:  # game loop

        if MAX == "X":  # AI first
            if result() is not None: break
            grid[ai_move()] = MAX
            draw_grid()
            if result() is not None: break
            grid[get_move()] = MIN

        if MIN == "X":  # User first
            if result() is not None: break
            grid[get_move()] = MIN
            if result() is not None: break
            grid[ai_move()] = MAX
            draw_grid()

    if result() == -1: print(f"{MIN} wins!\n")
    elif result() == +1: print(f"{MAX} wins!\n")
    elif result() == 0: print("Game tied!\n")
    raise SystemExit from None


if __name__ == "__main__":
    main()
