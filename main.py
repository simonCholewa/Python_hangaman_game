import random
import wordsList
import ascii
from replit import clear


print(ascii.logo)

word_list = wordsList.word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
print(chosen_word)



display = []
for _ in range(word_length):
  display.append("_")


while not end_of_game:
  
  guess = input("Guess a letter: ").lower()

  clear()

  if guess not in chosen_word:
    lives -= 1
  
  for pos in range(word_length):
    if chosen_word[pos] == guess:
      display[pos] = guess
   
  print(display)

  if "_" not in display:
    end_of_game = True
    print("You won!")
  elif lives == 0:
    end_of_game = True
    print("You lose")
  print(ascii.stages[lives])