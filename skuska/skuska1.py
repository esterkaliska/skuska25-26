class Highlighter:
    def __init__(self):
        self.vowels = "aeiyoôuáéíýóúůäAEIYOÔUÁÉÍÝÓÚŮÄ"
        self.allowed = ("abcdefghijklmnopqrstuvwxyzáéíýóúůäčďľĺňŕšťž"
                         "ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÝÓÚŮÄČĎĽĹŇŔŠŤŽ"
                         "0123456789 ,.?!;")

    def process_text(self, text):
        result = ""
        for symbol in text:
            if symbol in self.vowels:
                result += f"({symbol})"
            elif symbol in self.allowed:
                result += symbol
        return result

function = Highlighter()

text = input("Input text (allowed languages: English, Slovak, Czech): ")
result = function.process_text(text)

print("Result:", result)
