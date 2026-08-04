from app.services.parser import ParserService
from app.services.text_cleaner import TextCleaner

text = ParserService.extract_text("sample.pdf")

clean_text = TextCleaner.clean(text)

print(clean_text)