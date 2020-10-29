from gtts import gTTS
import os
tts = gTTS(text='Olá, sou feito em python ', lang='PT-BR')
tts.save("good.mp3")
os.system("good.mp3")