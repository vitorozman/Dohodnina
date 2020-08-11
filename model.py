from kriterij import *


class Dohodnina_1:
    
    def __init__(self, placa, sez_znacka):#sez_znacka vsebuje znacke ki predstavljajo dolocene olajsave, placa je bruto mesecna placa
        self.placa = placa 
        self.sez_znacka = sez_znacka
    
    def prispevki(self):
        if 'P' in self.sez_znacka:
            return self.placa * 0.155
        elif 'Up' in self.sez_znacka:
            return 0
        else:
            return self.placa * 0.221

    def olajsave(self, st_otrok, st_inv_otrok, st_vzd_clan, dodatno_pok):
        olajsava = 0
        if 'O' in self.sez_znacka:
            olajsava = 17658.84
        if 'P' in self.sez_znacka:
            olajsava += 3500
        if 'Po' in self.sez_znacka:
            na_dodatnega = na_otroka[5]
            for otrok in range(1, st_otrok + 1):  # za vsakega otroka pogleda koliko je olajsava in doda
                if otrok >= 6:
                    na_dodatnega += 1769.3
                    olajsava += na_dodatnega
                else:
                    olajsava += na_otroka[otrok]
        if 'PoI' in self.sez_znacka:
            olajsava += st_inv_otrok * 8830
        if 'Pc' in self.sez_znacka:
            olajsava += st_vzd_clan * 2436.62
        if 'Z' in self.sez_znacka:
            olajsava += min(2819.09, self.placa * 0.05844, dodatno_pok)
        return olajsava
    

############## letno ##############
def racunalo(self):
        osnova = self.placa - self.prispevki() - olajsave()
        if osnova <= 8500:
            return self.placa * 0.16
        elif 8500 < osnova <= 25000:
            return 1360 + (osnova - 8500) * 0.26
        elif 25000 < osnova <= 50000:
            return 5650 + (osnova - 25000) * 0.33
        elif 25000 < osnova <= 72000:
            return 13900 + (osnova - 4166.67) * 0.39
        else:
            return 22480  + (osnova - 72000) * 0.5


############# mesecno #############
    def racunalo(self):
        osnova = self.placa - self.prispevki() - olajsave()
        if osnova <= 708.33:
            return self.placa * 0.16
        elif 708.33 < osnova <= 2083.33:
            return 113.33 + (osnova - 708.33) * 0.26
        elif 1083.33 < osnova <= 4166.67:
            return 470.83 + (osnova - 2083.33) * 0.33
        elif 4166.67 < osnova <= 6000:
            return 1158.33 + (osnova - 4166.67) * 0.39
        else:
            return 1873.33  + (osnova - 6000) * 0.5

class Dohodnina_2(Dohodnina_1):

    def __init__(self, placa1, placa2, sez_znacka1, sez_znacka2):
        self.placa1 = placa1
        self.placa2 = placa2
        self.sez_znacka1 = sez_znacka1
        self.sez_znacka2 = sez_znacka2


def splona(placa):
    if placa <= 1109.74:
        return 291.67 + (1558.37 - 1404.27 * placa)
    else:
        return 291.67
