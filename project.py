# Game board representation (using a list)
board = [' '] * 9

def display_board(board):
  """Prints the current state of the Tic-Tac-Toe board."""
  for i in range(3):
    print('|', board[i*3], '|', board[i*3+1], '|', board[i*3+2], '|')
  print('-' * 11)

def is_space_free(board, move):
  """Checks if the specified move (index) on the board is empty."""
  return board[move] == ' '

def make_move(board, player, move):
  """Places the player's mark (X or O) on the board at the specified move."""
  board[move] = player

def check_win(board, player):
  """Checks if the specified player has achieved a winning condition."""
  win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6))
  for row in win_conditions:
    if all(board[i] == player for i in row):
      return True
  return False

def is_board_full(board):
  """Checks if all spaces on the board are filled."""
  return all(space != ' ' for space in board)

def choose_random_move(board, computer_symbol):
  """Selects a random empty space on the board for the computer's move."""
  possible_moves = [i for i, space in enumerate(board) if space == ' ']
  return random.choice(possible_moves)

def player_move(board):
  """Gets a valid move from the human player."""
  while True:
    try:
      move = int(input("Enter your move (1-9): ")) - 1
      if 0 <= move <= 8 and is_space_free(board, move):
        return move
      else:
        print("Invalid move. Please try again.")
    except ValueError:
      print("Invalid input. Please enter a number.")

def play_game():
  """Main game loop that handles turns, win conditions, and overall game flow."""
  current_player = 'X'
  game_on = True

  while game_on:
    display_board(board)

    # Human vs. Human
    if current_player == 'X':
      player_name = 'Player 1 (X)'
    else:
      player_name = 'Player 2 (O)'
    move = player_move(board) if choose_human_vs_human else choose_random_move(board.copy(), current_player)

    make_move(board, current_player, move)

    if check_win(board, current_player):
      display_board(board)
      print(f"{player_name} wins!")
      game_on = False
    elif is_board_full(board):
      display_board(board)
      print("It's a tie!")
      game_on = False

    # Switch players
    current_player = 'O' if current_player == 'X' else 'X'

  # Ask if players want to play again
  while True:
    play_again = input("Play again? (y/n): ").lower()
    if play_again == 'y':
      reset_board(board)
      play_game()
      break
    elif play_again == 'n':
      break
    else:
      print("Invalid input. Please enter y or n.")

def reset_board(board):
  """Resets the game board to its initial empty state."""
  for i in range(len(board)):
    board[i] = ' '

# Choose human vs. human or human vs. computer
choose_human_vs_human = True
while True:
  game_mode = input("Choose game mode (human vs. human or human vs. computer) (h/c): ").lower()
  if game_mode == 'h':
    choose_human_vs_human = True
    break
  elif game
