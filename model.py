
class Dohodnina_1:
    
    def __init__(self, placa, sez_znacka):#sez_znacka vsebuje znacke ki predstavljajo dolocene olajsave, placa je bruto mesecna placa
        self.placa = placa 
        self.sez_znacka = sez_znacka
    
    def prispevki(self):
        if student in self.sez_znacka and vzdrzevan in self.sez_znacka:
            return self.placa * 0.155
        elif upokojenec in self.sez_znacka:
            return 0
        else:
            return self.placa * 0.221


    def racunalo(self):
        #placa = prispevki(self.placa)
        pass

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
