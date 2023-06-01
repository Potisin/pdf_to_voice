from gtts import gTTS
import pdfplumber


def converter(file, language='ru'):
    with pdfplumber.open(file) as pdf:
        pages = [page.extract_text() for page in pdf.pages]
    text = ''.join(pages)
    text = text.replace('\n', '')
    voice = gTTS(text=text, lang=language, slow=False)
    voice.save(f'{file.filename}.mp3')
    return voice

def test():
    pass
