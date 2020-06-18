import random
import os
from  gtts import gTTS

#list with words to guess
library = ['word', 'forest', 'butterfly', 'fly', 'house', 'random', 'laptop', 'neighbour', 'uncle', 'human', 'magnificent', 'library', 'satisfying', 'ocean', 'landscape', 'chicken', 'unique', 'offer', 'procrastination', 'collection']
random_word = random.choice(library) #choosing random word
word = ['*' for x in range(len(random_word))] #changing every letter in chosen word with '*' character

win = f"Congratulations the word is {random_word}" #text for win sound
lose = "I can smell your ass burning" #text for lose sound
language = 'en' #language setting for audio file
lose_sound = gTTS(text=lose, lang=language, slow=False) # creating lose audio file
win_sound = gTTS(text=win, lang = language, slow = False) # creating win audio file
lose_sound.save('lose.mp3') # saving lose audio file
win_sound.save('done.mp3') # saving win audio file


print(f'Try to guess the word {word}') # displaying coded word on the screen

def hanged_man(word = word, tries = 0): 
	while tries < 5: # number of tries
		guess = str(input('Guess the letter: ')) # input guess letter
		if guess in random_word:
			for ind, item in enumerate(random_word):
				if item==guess:
					word[ind]=guess
					if '*' in word:
						print(f'Good one! There is letter "{guess}"! And now word looks like {word}')
					else:
						os.system('done.mp3')
						return f'Congratulations! The word is {"".join(word)}'
		else:
			print(f'Try again!You have {5 - tries}')
			tries += 1
	if tries==5 and "*" in word:
		os.system('lose.mp3')
		return 'You lose!'

print(hanged_man())
