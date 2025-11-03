import random 
import pytest

words = ["candy", "dune", "tiger", "california", "pineapple", "sprite"]

def test_words_list():
  word = random.choice(words)
  assert word in words

def correct_guess():
  word ="candy"
  guess = "d"
  assert guess in word

def incorrect_guess()
word = "candy"
guess = "x"
assert guess not in word
