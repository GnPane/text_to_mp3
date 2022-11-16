from gtts import gTTS
from pathlib import Path


def text_to_mp3(file_text, file_name='MP3_file.mp3', lang='ru'):
    mp3 = gTTS(text=file_text, lang=lang)
    file_name = Path(file_name).stem
    mp3.save(f'{file_name}.mp3')
