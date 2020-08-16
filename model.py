from kriterij import *


class Dohodnina_1:
    
    def __init__(self, placa, sez_znacka, sl_osebe):#sez_znacka vsebuje znacke ki predstavljajo dolocene olajsave, placa je bruto letna placa
        self.dohodek = placa 
        self.sez_znacka = sez_znacka
        self.sl_osebe = sl_osebe #slovar ki vsebuje st otrok, ostalih vzdrzevanih clanov, invalidnih otrok, znesek ki ga placujejo za dodatno pokijnino
    
    def prispevki(self):
        if 'P' in self.sez_znacka:
            return self.dohodek * 0.155
        elif 'Up' in self.sez_znacka:
            return 0
        else:
            return self.dohodek * 0.221

    def olajsave_brez_otrok(self):
        olajsava = 0
        if 'S' in self.sez_znacka: #slosna olajsava
            if self.dohodek * 12 <= 13316.83:
                olajsava += 3500 + 18700.38 - (1.40427 * self.dohodek * 12)
            else:
                olajsava += 3500
        if 'O' in self.sez_znacka:#invalidska olajsava
            olajsava = 17658.84
        if 'P' in self.sez_znacka:#student
            olajsava += 3500
        if 'PoI' in self.sez_znacka:#vzdrzevani otrok s potrednimi potrebami
            olajsava += self.sl_osebe['st_inv_otrok'] * 8830
        if 'Pc' in self.sez_znacka:#vzdrzevani clan
            olajsava += self.sl_osebe['st_vzd_clan'] * 2436.62
        if 'Z' in self.sez_znacka:#doddatno pokojninsko zavarovanje
            olajsava += min(2819.09, self.dohodek * 0.05844, self.sl_osebe['dodatno_pok'])
        return olajsava

    def oljasava_z_otroki(self):
        olajsava = 0
        if 'Po' in self.sez_znacka:#vzdrzevani otrok
            na_dodatnega = na_otroka[5]
            for otrok in range(1, self.sl_osebe['st_otrok'] + 1):  # za vsakega otroka pogleda koliko je olajsava in doda
                if otrok >= 6:
                    na_dodatnega += 1769.3
                    olajsava += na_dodatnega
                else:
                    olajsava += na_otroka[otrok]

    














############## letno ##############
    def racunalo_d(self, osnova):
            if osnova <= 8500:
                return self.dohodek * 0.16
            elif 8500 < osnova <= 25000:
                return 1360 + (osnova - 8500) * 0.26
            elif 25000 < osnova <= 50000:
                return 5650 + (osnova - 25000) * 0.33
            elif 25000 < osnova <= 72000:
                return 13900 + (osnova - 4166.67) * 0.39
            else:
                return 22480  + (osnova - 72000) * 0.5




    #n = {1, 2} stevilo oseb za izracun dohodnine
    def osnova_d(self, n=1):
        if n == 1:
            return self.dohodek - self.prispevki() - self.olajsave()
        else:
            return self.dohodek - self.prispevki() - self.olajsava_opt()
    
    def olajsava_opt(self, st_o, st_m):
        pass


    


class Optimalec:

    def __init__(self, dohodek1, dohodek2, st_otrok):
        self.dohodek1 = dohodek1
        self.dohodek2 = dohodek2
        self.st_otrok = st_otrok


    def dohodnina(self, osnova, dohodek):
            if osnova <= 8500:
                return dohodek * 0.16
            elif 8500 < osnova <= 25000:
                return 1360 + (osnova - 8500) * 0.26
            elif 25000 < osnova <= 50000:
                return 5650 + (osnova - 25000) * 0.33
            elif 25000 < osnova <= 72000:
                return 13900 + (osnova - 4166.67) * 0.39
            else:
                return 22480  + (osnova - 72000) * 0.5

    
    def preracun(self, osnova1, osnova2, st_otrok, kombinacija):#kombinacija je {'1':n, '2':12-n}
        olajsava = 0
        for st in range(st_otrok + 1):
            olajsava = na_otroka_mesecno[st]
        osnova1 = osnova1 - olajsava * kombinacija['1']
        osnova2 = osnova2 - olajsava * kombinacija['2']
        return self.dohodnina(osnova1, self.dohodek1) + self.dohodnina(osnova2, self.dohodek2)

    def osnova_brez_otrok(self, dohodek, prispevki, olajsave):
        return dohodek - prispevki - olajsave





def moznosti():
        sl_moznosti = {}
        os1, os2 = '1', '2'
        for n in range(13):
            sl_moznosti[n] = {os1 : n, os2 : 12 - n}
        return sl_moznosti

    