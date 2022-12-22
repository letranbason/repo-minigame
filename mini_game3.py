def tic_tac_toe():
  # Set up the game board
  board = [[" " for _ in range(3)] for _ in range(3)]

  # Set up the game variables
  current_player = "X"
  game_over = False

  # Welcome the user
  print("Welcome to Tic Tac Toe! Player X goes first.")
  print("Here is the current board:")
  print_board(board)

  # Start the game loop
  while not game_over:
    # Get the user's move
    row = int(input("\nEnter the row for your next move: "))
    col = int(input("Enter the column for your next move: "))

    # Make the move if it is valid
    if board[row][col] == " ":
      board[row][col] = current_player
      game_over = check_game_over(board)
      if game_over:
        break
      # Switch to the other player
      if current_player == "X":
        current_player = "O"
      else:
        current_player = "X"
      print("\nHere is the current board:")
      print_board(board)
    else:
      print("\nThat space is already occupied. Try again.")

  # Print a message if the game is over
  if game_over:
    print("Game over! Thanks for playing.")
  else:
    print("It's a tie!")

def print_board(board):
  print("\n  0 1 2")
  for i, row in enumerate(board):
    print(i, *row)

def check_game_over(board):
  # Check for a winning row
  for row in board:
    if row[0] != " " and row[0] == row[1] == row[2]:
      return True

  # Check for a winning column
  for col in range(3):
    if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
      return True

  # Check for a winning diagonal
  if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
    return True
  if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
    return True

  # Check for a tie
  for row in board:
    if " " in row:
      return False
  return True

tic_tac_toe()
