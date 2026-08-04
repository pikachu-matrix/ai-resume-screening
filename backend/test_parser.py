from app.services.parser import ParserService

text = ParserService.extract_text("sample.pdf")

print(text)