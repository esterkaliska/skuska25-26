class Zvyraznovac:
    def __init__(self):
        self.samohlasky = "aeiyoôuáéíýóúůäAEIYOÔUÁÉÍÝÓÚŮÄ"
        self.povolene = ("abcdefghijklmnopqrstuvwxyzáéíýóúůäčďľĺňŕšťž"
                         "ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÝÓÚŮÄČĎĽĹŇŔŠŤŽ"
                         "0123456789 ,.?!;")

    def spracuj_text(self, text):
        vysledok = ""
        for znak in text:
            if znak in self.samohlasky:
                vysledok += f"({znak})"
            elif znak in self.povolene:
                vysledok += znak
        return vysledok

funkcia = Zvyraznovac()

text = input("Zadaj text: ")
vysledok = funkcia.spracuj_text(text)

print("Výsledok:", vysledok)