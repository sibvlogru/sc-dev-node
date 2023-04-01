import re
import textwrap
from io import BytesIO
from gtts import gTTS
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from nltk.tokenize import sent_tokenize
import chardet
import nltk
nltk.download('punkt')

LANGUAGE = "ru"
SENTENCES_COUNT = 5

# Определение кодировки текста
with open("text.txt", "rb") as f:
    text_bytes = f.read()
    result = chardet.detect(text_bytes)
    encoding = result['encoding']
    print(f"Кодировка текста: {encoding}")

# Чтение текста
with open("text.txt", "r", encoding=encoding) as f:
    text = f.read()

# Токенизация и суммаризация текста
parser = PlaintextParser.from_string(text, Tokenizer("russian"))
summarizer = TextRankSummarizer()
summary = summarizer(parser.document, SENTENCES_COUNT)

print("Результаты:")
print("Сокращенный текст:")
summary_text = ""
for sentence in summary:
    summary_text += str(sentence) + "\n"
    print(sentence)

text = re.sub(r"[^\w\s.,!?;:-]+", "", text)
# Сохранение результата в файл
with open("summary.txt", "w", encoding="utf-8") as f:
    for sentence in summary:
        wrapped_text = textwrap.fill(str(sentence), width=80)
        f.write(wrapped_text + "\n")
