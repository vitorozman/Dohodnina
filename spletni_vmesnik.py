import bottle



@bottle.get('/')
def zacetna_stran():
    return 'Zivjo'



bottle.run(debug=True, reloader=True)
