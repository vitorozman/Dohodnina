from model import * 


p1 = 11286.96
sl = {
    'splosna' : True,
    'invalidska' : False,
    'dodatno_pok' : 0
}
st = 0
pr1 = p1 * 0.22

p2 = 1105
pr2 = p2 * 0.22

d1 = Dohodnina(p1, pr1, sl, st)
d2 = Dohodnina(p2, pr2, sl, st)

#print(Dohodnina.optimalec(d1, d2))
print(d1.rangiranje())
