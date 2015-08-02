import rethinkdb as r

from sketchcase.helpers import connection


def sync_db():
    with connection() as conn:
        r.table_create('documents').run(conn)
        r.table_create('artboards').run(conn)
        r.table_create('revisions').run(conn)

        r.table('documents').index_create('name').run(conn)
        r.table('revisions').index_create('artboard_id').run(conn)
        r.table('artboards').index_create(
            'name_and_document', [r.row['name'], r.row['document_id']]
        ).run(conn)

if __name__ == '__main__':
    sync_db()
