import bottle



@bottle.get('/')
def zacetna_stran():
    return bottle.template('zacetna_stran.html')

@bottle.post('/izracunaj/')
def izracunaj():
    dohodek = int(bottle.request.forms['dohodek'])
    prispevki = int(bottle.request.forms['prispevki'])
    akontacija = int(bottle.request.forms['akontacija'])
    bottle.redirect('/')
    print(dohodek)
    print(prispevki)
    print(akontacija)




bottle.run(debug=True, reloader=True)
