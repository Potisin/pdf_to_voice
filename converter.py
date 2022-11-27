from gtts import gTTS
import pdfplumber


def converter(file, language='en'):
    with pdfplumber.PDF()) as pdf:
