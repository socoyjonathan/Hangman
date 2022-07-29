# install random_word module
pip install random_word

#import random_word module and get a random word
from random_word import RandomWords
r = RandomWords()

guess = r.get_random_word()

hung_man_count = 6
tries_left = hung_man_count
real_guess, guess_2, user_guesses  = [], [], []
guess_2[:0] = len(guess)*"_"

while hung_man_count > 0:
  print(guess_2)
  user_guess = input("Please guess a letter:\n")[0]

  if user_guess in user_guesses:
    user_guess = input("Please guess another letter:\n")[0]

  user_guesses.append(user_guess)
  real_guess = []
  real_guess[:0] = guess

  for g in guess:
    if g == user_guess:
      indexes = [i for i in range(len(guess)) if guess[i] == user_guess]
      for i in indexes:
        guess_2[i] = (real_guess[i])

  if user_guess not in guess:
    if (tries_left > 0):
      print("Incorrect letter")
      tries_left = tries_left - 1
      if (tries_left == 0):
        print("You lost! Hangman")
        break
      print(f"Tries left: {str(tries_left)} \n")

  if guess_2 == real_guess:
    print(f"You win. The word is {guess}")
    break
