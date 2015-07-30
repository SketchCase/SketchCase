import rethinkdb as r

from sketchcase.helpers import connection


def sync_db():
    with connection() as conn:
        r.table_create('documents').run(conn)
        r.table_create('artboards').run(conn)
        r.table_create('revisions').run(conn)

if __name__ == '__main__':
    sync_db()
