sl_olajsave = {
    'splosna' : False,
    'invalidska' : False,
    'dodatno_pok' : 0
    }

na_otroka = {
        0 : 0,
        1 : 203.08,
        2 : 220.77,
        3 : 368.21,
        4 : 515.65,
        5 : 663.09
        }

class Dohodnina():

    def __init__(self, dohodek, prispevki, sl_olajsave, st_otrok):
        self.dohodek = dohodek #letni dohodek
        self.prispevki = prispevki
        self.sl_olajsave = sl_olajsave
        self.st_otrok = st_otrok

    #vrne znesek za olajsave brez posebne olajsave(otroci, clani)
    def olajsave_brez_otrok(self):
        olajsava = 0
        if self.sl_olajsave['splosna']: 
            if self.dohodek <= 13316.83:
                olajsava += 3500 + 18700.38 - (1.40427 * self.dohodek)
            else:
                olajsava += 3500
        if self.sl_olajsave['invalidska']:
            olajsava += 17658.84
        if self.sl_olajsave['dodatno_pok'] > 0:
            olajsava += min(2819.09, self.dohodek * 0.05844, self.sl_olajsave['dodatno_pok'])
        return olajsava

    def olajsave_z_otroki(self, st_mesecev=12):#za eno osebo mora biti st mesecev = 12
        olajsava = 0
        petplus = na_otroka[5]
        for n in range(self.st_otrok + 1):
            if n >= 6:
                petplus += 147.44
                olajsava += petplus
            else:
                olajsava += na_otroka[n]
        return olajsava * st_mesecev
    
    #dolocilec = {true, false} doloci ali je osnova z otroki al i ne
    def osnova(self, dolocilec=True):
        if dolocilec:
            return self.dohodek - self.prispevki - self.olajsave_brez_otrok() - self.olajsave_z_otroki()
        else:
            return self.dohodek - self.prispevki - self.olajsave_brez_otrok()


    #vrne dohodnino glede na rang v katerem si
    def rangiranje(self, osnova=0):
        if osnova == 0:
            osnova = self.osnova()
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
    

    #d1 je dohodnina za 1.osebo d2 pa 2. osebo
    @staticmethod
    def optimalec(d1, d2):
        osnova1 = d1.osnova(False)
        osnova2 = d2.osnova(False)
        sl_moznosti = moznosti()
        skupna_d = {}
        for n in range(13):
            ol1 = d1.olajsave_z_otroki(n)
            ol2 = d2.olajsave_z_otroki(12 - n)
            o1 = osnova1 - ol1
            o2 = osnova2 - ol2
            skupna = d1.rangiranje(o1) + d2.rangiranje(o2)
            sl_moznosti[n]['prvi'] = d1.rangiranje(o1)
            sl_moznosti[n]['drugi'] = d2.rangiranje(o2)
            skupna_d[skupna] = sl_moznosti[n]
        return min(skupna_d.items()) #vrne (min skupna d, {'1': st_mesecev, '2':st_mesecev}


######## funkcije ###################################################################

#naredi slovar z moznostmi kako prijavito otroke
def moznosti():
    sl_moznosti = {}
    os1, os2 = '1', '2'
    for st_mesecev in range(13):
        sl_moznosti[st_mesecev] = {os1 : st_mesecev, os2 : 12 - st_mesecev}
    return sl_moznosti
