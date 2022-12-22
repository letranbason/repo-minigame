from random import randint

def play_game():
  print("Welcome to the game!")
  name = input("What is your name? ")
  print(f"Hello, {name}! Let's get started.")

  # Set the initial score to 0
  score = 0

  # Start the game loop
  while True:
    # Generate a random number between 1 and 10
    number = randint(1, 10)

    # Prompt the user to guess the number
    guess = int(input("Guess a number between 1 and 10: "))

    # If the guess is correct, increase the score by 1 and print a message
    if guess == number:
      print("Correct!")
      score += 1
    else:
      print("Incorrect. The number was", number)
    
    # Ask the user if they want to keep playing
    play_again = input("Do you want to play again? [Y/n] ")
    if play_again.lower() != "y":
      break
  
  # Print the final score
  print(f"Thank you for playing, {name}. Your final score was {score}.")

play_game()
