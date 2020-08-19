from model import * 


p1 = 5000
sl = {
    'splosna' : True,
    'invalidska' : True,
    'dodatno_pok' : 200
}
st = 3
pr1 = p1 * 0.22

p2 = 4000
pr2 = p2 * 0.22

d1 = Dohodnina(p1, pr1, sl, st)
d2 = Dohodnina(p2, pr2, sl, st)

print(Dohodnina.optimalec(d1, d2))
