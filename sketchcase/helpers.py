import rethinkdb as r


def connection():
    return r.connect(host='rethinkdb', port=28015, db='sketchcase')
