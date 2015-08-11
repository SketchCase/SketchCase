import rethinkdb as r


def connection(db='sketchcase'):
    return r.connect(host='rethinkdb', port=28015, db=db)
