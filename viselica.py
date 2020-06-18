import random
import os
from  gtts import gTTS
import os

library = ['word', 'forest', 'butterfly', 'fly', 'house', 'random', 'laptop', 'neighbour', 'uncle', 'human', 'magnificent', 'library', 'satisfying', 'ocean', 'landscape', 'chicken', 'unic', 'offer', 'procrastination', 'collection']
random_word = random.choice(library)
word = ['*' for x in range(len(random_word))]

# word_sound = gTTS(text=random_word, lang='en', slow=False)
win = f"Congratulations the word is {random_word}"
lose = "I can smell your ass burning"
language = 'en'
lose_sound = gTTS(text=lose, lang=language, slow=False)
win_sound = gTTS(text=win, lang = language, slow = False)
# word_sound.save('word.mp3')
lose_sound.save('lose.mp3')
win_sound.save('done.mp3')


print(f'Try to guess the word {word}')

def hanged_man(word = word, tries = 0):
	while tries < 5:
		guess = str(input('Guess the letter: '))
		if guess in random_word:
			for ind, item in enumerate(random_word):
				if item==guess:
					word[ind]=guess
					if '*' in word:
						print(f'Good one! There is letter "{guess}"! And now word looks like {word}')
					else:
						# os.system('word.mp3')
						os.system('done.mp3')
						return f'Congratulations! The word is {"".join(word)}'
		else:
			print(f'Try again!You have {5 - tries}')
			tries += 1
	if tries==5 and "*" in word:
		os.system('lose.mp3')
		return 'You lose!'

print(hanged_man())