import re


class TextPreprocessor:

    def clean_text(self, text):

        clean_text = re.sub(r"\n+", "\n", text)

        clean_text = clean_text.replace("\t", " ")

        clean_text = " ".join(clean_text.split())

        return clean_text