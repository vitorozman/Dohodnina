import bottle
from model import *

@bottle.get('/')
def vstop():
    return bottle.template('osnovna.html')

@bottle.get('/zacetna_stran/')
def zacetna_stran():
    return bottle.template('zacetna_stran.html')

@bottle.get('/ena_oseba/')
def ena_oseba():
    return bottle.template('ena_oseba.html')

@bottle.get('/dve_osebi/')
def dve_osebi():
    return bottle.template('dve_osebi.html')

@bottle.get('/izracunaj/')
def izracunaj():
    sl_olajsave = {}
    dohodek = float(bottle.request.query['dohodek'])
    prispevki = float(bottle.request.query['prispevki'])
    akontacija = float(bottle.request.query['akontacija'])

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
        dodatno_pok = float(bottle.request.query['dodatno_pok'])
    except ValueError:
        dodatno_pok = 0
    sl_olajsave['splosna'] = splosna
    sl_olajsave['invalidska'] = invalidska
    sl_olajsave['dodatno_pok'] = dodatno_pok

    d = Dohodnina(dohodek, prispevki, sl_olajsave, st_otrok)

    olajsave = round(d.olajsave_brez_otrok() + d.olajsave_z_otroki(), 2)
    znesek = round(d.rangiranje() - akontacija, 2)
    if znesek <= 0:
        niz = f'Vračilo zanša {abs(znesek)} €'
    else:
        niz = f'Doplačilo zanša {znesek} €'
    
    return bottle.template('izpis_ena.html', niz=niz, olajsave=olajsave)
    

@bottle.get('/optimalec/')
def za_dva():
    #skupno stevilo otrok
    st_otrok = int(bottle.request.query['st_otrok'])
    #prva oseba
    sl_olajsave1 = {}
    dohodek1 = float(bottle.request.query['dohodek1'])
    prispevki1 = float(bottle.request.query['prispevki1'])
    akontacija1 = float(bottle.request.query['akontacija1'])
    try:
        splosna1 = bool(bottle.request.query['splosna1'])
    except KeyError:
        splosna1 = False
    try:
        invalidska1 = bool(bottle.request.query['invalidska1'])
    except KeyError:
        invalidska1 = False
    try:
        dodatno_pok1 = float(bottle.request.query['dodatno_pok1'])
    except ValueError:
        dodatno_pok1 = 0
    sl_olajsave1['splosna'] = splosna1
    sl_olajsave1['invalidska'] = invalidska1
    sl_olajsave1['dodatno_pok'] = dodatno_pok1
    #druga oseba
    sl_olajsave2 = {}
    dohodek2 = float(bottle.request.query['dohodek2'])
    prispevki2 = float(bottle.request.query['prispevki2'])
    akontacija2 = float(bottle.request.query['akontacija2'])
    try:
        splosna2 = bool(bottle.request.query['splosna2'])
    except KeyError:
        splosna2 = False
    try:
        invalidska2 = bool(bottle.request.query['invalidska2'])
    except KeyError:
        invalidska2 = False
    try:
        dodatno_pok2 = float(bottle.request.query['dodatno_pok2'])
    except ValueError:
        dodatno_pok2 = 0
    sl_olajsave2['splosna'] = splosna2
    sl_olajsave2['invalidska'] = invalidska2
    sl_olajsave2['dodatno_pok'] = dodatno_pok2

    d1 = Dohodnina(dohodek1, prispevki1, sl_olajsave1, st_otrok)
    d2 = Dohodnina(dohodek2, prispevki2, sl_olajsave2, st_otrok)
    _, opt = Dohodnina.optimalec(d1, d2)

    return bottle.template('izpis_dva.html', opt=opt, akontacija1=akontacija1, akontacija2=akontacija2)

bottle.run(debug=True, reloader=True)