import rethinkdb as r

from jsonschema import validate
from sketchcase.helpers import connection


def list(table):
    with connection() as conn:
        return [doc for doc in r.table(table).run(conn)]


def retrieve(table, id):
    with connection() as conn:
        return r.table(table).get(id).run(conn)


def create(table, data, schema):
    validate(data, schema)

    with connection() as conn:
        result = r.table(table).insert(data).run(conn)
        if result['inserted'] == 1:
            data['id'] = result['generated_keys'][0]
            return data
        else:
            return None


def update(table, id, data, schema):
    validate(data, schema)

    with connection() as conn:
        result = r.table(table).get(id).update(data).run(conn)

        # TODO deal with results somehow

        return r.table(table).get(id).run(conn)


def delete(table, id):
    with connection() as conn:
        r.table(table).get(id).delete().run(conn)
