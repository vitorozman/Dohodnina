import bottle
from model import *


@bottle.get('/')
def zacetna_stran():
    return bottle.template('zacetna_stran.html')

@bottle.get('/ena_oseba/')
def ena_oseba():
    return bottle.template('ena_oseba.html')



@bottle.get('/izracunaj/')
def izracunaj():
    sl_olajsave = {}
    dohodek = int(bottle.request.query['dohodek'])
    prispevki = int(bottle.request.query['prispevki'])
    akontacija = int(bottle.request.query['akontacija'])

    st_otrok = int(bottle.request.query['st_otrok'])

    try:
        splosna = bool(bottle.request.query['splosna'])
    except KeyError:
        splosna = False
    try:
        invalidska = bool(bottle.request.query['invalidska'])
    except KeyError:
        invalidska = False
    try:
        dodatno_pok = int(bottle.request.query['dodatno_pok'])
    except ValueError:
        dodatno_pok = 0
    sl_olajsave['splosna'] = splosna
    sl_olajsave['invalidska'] = invalidska
    sl_olajsave['dodatno_pok'] = dodatno_pok

    d = Dohodnina(dohodek, prispevki, sl_olajsave, st_otrok)

    znesek = round(d.rangiranje(), 2) - akontacija
    if znesek <= 0:
        izpis = f'Od drzave dobite {abs(znesek)}'
    else:
        izpis = f'Dohodnina zanas {znesek}'
    
    return bottle.template('izpis_ena.html', izpis=izpis)
    




bottle.run(debug=True, reloader=True)
