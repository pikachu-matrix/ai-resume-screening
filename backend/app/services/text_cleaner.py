import re

class TextCleaner:

    @staticmethod
    def clean(text: str) -> str:

       #remove extra spaces
       text = re.sub(r"\s+", " ", text)

        #remove empty lines
       text = re.sub(r"\n+", "\n", text)

       #remove tabs
       text=text.replace("\t", " ")

       #remove non-printable characters
       text ="".join(
           character
           for character in text
              if character.isprintable()
       )

       return text.strip()