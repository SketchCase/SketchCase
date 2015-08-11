import rethinkdb as r

from sketchcase.utils.db import connection


def setup_db():
    with connection(db=None) as conn:
        r.db_create('sketchcase').run(conn)

        rdb = r.db('sketchcase')
        rdb.table_create('documents').run(conn)
        rdb.table_create('artboards').run(conn)
        rdb.table_create('revisions').run(conn)

        rdb.table('documents').index_create('name').run(conn)
        rdb.table('revisions').index_create('artboard_id').run(conn)
        rdb.table('artboards').index_create(
            'name_and_document', [r.row['name'], r.row['document_id']]
        ).run(conn)

if __name__ == '__main__':
    setup_db()
