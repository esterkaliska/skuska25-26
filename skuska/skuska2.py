import scipy.stats as stats
import os

class AnalyzaDat:
    def __init__(self, subor):
        priečinok_skriptu = os.path.dirname(os.path.abspath(__file__))
        self.subor = os.path.join(priečinok_skriptu, subor)
        self.data = []

    def nacitaj_data(self):
        try:
            with open (self.subor, "r", encoding="utf-8") as subor:
                for hodnota in subor:
                    hodnota = hodnota.strip()
                    if not hodnota: continue
                    self.data.append(float(hodnota))
                return self.data 
        except FileNotFoundError: 
            print("Chyba! Súbor nebol nájdený.")
            return None
        except ValueError: 
            print("Chyba! V súbore sú nečitateľné údaje.")
            return None
        except Exception:
            print("CHYBA!")
            return None

    def vypocitaj_normalitu(self):
        if len(self.data) < 3:
            return "Nedostatok dát na analýzu."

        statistika, p_hodnota = stats.shapiro(self.data)
        
        print(f"Výsledná p-hodnota: {p_hodnota:.4f}")

        if p_hodnota > 0.05:
            return "Výsledok: Dáta MAJÚ normálne rozdelenie (p > 0.05)."
        else:
            return "Výsledok: Dáta NEMAJÚ normálne rozdelenie (p < 0.05)."

data = input("Zadaj názov súboru (napr. data.txt): ")
funkcia = AnalyzaDat(data)
funkcia.nacitaj_data()
vysledok = funkcia.vypocitaj_normalitu()

print(vysledok)

                        
