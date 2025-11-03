import random

words = ["candy", "dune", "tiger", "california", "pineapple", "sprite"]

random_word = random.choice(words)
guessed = []
attempts = 6

print(f"Guess the {len(word)} letter word?")

while attempts > 0:
  for letter in word:
    if letter in guessed:
      print(letter, end=" ")
    else:
      print(" ", end=" ")
    print(f"Attempts remaining: {attempts}")

    if all(letter in guessed for letter in word):
        print(f"You guessed the word correctly! {word}")
        break

    guess = input("Guess a letter: ".lower()

    if guess in word:
      print("Correct")
      guessed.append(guess)
    else:
      print"Wrong! Try again")
      attempts -=1
else:
print(f"Out of trys! the word was {word}")
                    
    
