# Tic Tac Toe Game in Python
import random
import time

# Initial empty board with position numbers
board = [
    ["1", "2", "3"],
    ["4", "5", "6"],    
    ["7", "8", "9"]
]

# Draw the board nicely
def draw_board(board):
    print("┌───┬───┬───┐")
    for i in range(3):
        print(f"│ {board[i][0]} │ {board[i][1]} │ {board[i][2]} │")
        if i != 2:
            print("├───┼───┼───┤")
    print("└───┴───┴───┘")

# Convert 1-9 input to board position (row, col)
def get_position(choice):
    choice = int(choice) - 1  # Convert to 0–8
    row = choice // 3
    col = choice % 3
    return row, col

# look for unoccupied positions and return them
def get_unoccupied_positions(board):
    unoccupied = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ["X", "O"]:
                unoccupied.append((i, j))
    return unoccupied

# Computer's move logic
# Randomly selects an unoccupied position
def computer_move(board):
    free = get_unoccupied_positions(board)
    if free:
        row, col = random.choice(free)
        board[row][col] = "O"
        print(f"🤖 Computer placed 'O' at position {row * 3 + col + 1}.")


# Typing effect for messages
def typing_effect(message, delay=0.5):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


# check for a win condition
def check_winner(board, symbol):
    # check for row, column wins
    for i in range(3):
        if all (board[i][j] == symbol for j in range(3)):
            return True
        if all (board[j][i] == symbol for j in range(3)):
            return True 
        
    # check for diagonal wins 
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    
    return False

# show player win
def show_player_win():
    print("\n🎉🎉🎉 Congratulations! 🎉🎉🎉")
    message = "✨ You have WON the game! ✨"
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print("\n🏆 Victory is yours! 🏆\n")

# show computer win
def show_computer_win():
    print("\n🤖💥 Beep boop...")
    time.sleep(1)
    print("☠️  The computer has outsmarted you. ☠️")
    message = "😈 You lost this round..."
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print("\nTry again if you dare! 🤖🔥\n")

# show draw
def show_draw():
    print("\n😐 It's a draw!")
    message = "🌀 No winner this time... but well played!"
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

# Main game loop
def play_game():
    current_player = "X"
    moves = 0

    while moves < 9:
        draw_board(board)
        choice = input(f"Player {current_player}, enter a position (1-9): ")

        if not choice.isdigit() or int(choice) not in range(1, 10):
            print("❌ Invalid input. Choose a number from 1 to 9.")
            continue

        row, col = get_position(choice)

        # Check if position is already taken
        if board[row][col] in ["X", "O"]:
            print("⛔ That spot is already taken. Choose another.")
            continue

        board[row][col] = current_player
        moves += 1
        draw_board(board)

        # ✅ Check if player wins
        if check_winner(board, current_player):
            show_player_win()
            return

        if moves == 9:
            break

        # computer's turn
        if moves < 9:
            print("🤖 Computer's turn", end="", flush=True)
            typing_effect("...", delay=0.2)
            time.sleep(1)
            computer_move(board)
            moves += 1
        
        # ✅ Check if computer wins
        if check_winner(board, "O"):
            show_computer_win()
            return

    # If we reach here, it's a draw
    show_draw()

# Start the game
print("Welcome to Tic Tac Toe!")
play_game() 