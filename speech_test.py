from  gtts import gTTS
import os
win = "заебись ты это сделал"
lose = 'а-та-та твоя жопа будет гореть'
language = 'ru'
lose_sound = gTTS(text=lose, lang=language, slow=False)
win_sound = gTTS(text=win, lang = language, slow = False)
lose_sound.save('lose.mp3')
win_sound.save('done.mp3')	
os.system('lose.mp3')