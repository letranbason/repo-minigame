def hangman():
  # Set up the game variables
  word = "python"
  word_letters = set(word)
  alphabet = set("abcdefghijklmnopqrstuvwxyz")
  used_letters = set()
  mistakes = 0
  max_mistakes = 6

  # Welcome the user
  print("Welcome to Hangman! Can you guess the word before you run out of tries?")
  print(f"The word is {len(word)} letters long.")

  # Start the game loop
  while mistakes < max_mistakes:
    # Print the current status of the game
    print("\nCurrent: ", end="")
    for letter in word:
      if letter in used_letters:
        print(letter, end="")
      else:
        print("_", end="")
    print(f"\nLetters used: {', '.join(used_letters)}")

    # Get the user's guess
    guess = input("\nGuess a letter: ").lower()

    # Check if the guess is valid
    if guess in alphabet - used_letters:
      used_letters.add(guess)
      if guess in word_letters:
        print("Correct!")
        word_letters -= set(guess)
        if not word_letters:
          print("You won!")
          break
      else:
        print("Incorrect.")
        mistakes += 1
    elif guess in used_letters:
      print("You already used that letter. Try again.")
    else:
      print("Invalid input. Try again.")
  
  # Print a message if the user lost
  if mistakes == max_mistakes:
    print("You lost. The word was", word)

hangman()
