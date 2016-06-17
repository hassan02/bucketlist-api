import os
import sqlite3

BASEDIR = os.path.abspath(os.path.dirname(__file__))
database_name = os.path.join(BASEDIR, 'bucketlist_test.sqlite')


def setupDatabase():
    db_conn = sqlite3.connect(database_name)
    db_cursor = db_conn.cursor()
    db_cursor.execute('DELETE FROM user')
    db_cursor.execute('DELETE FROM bucket_list')
    db_cursor.execute('DELETE FROM bucket_list_item')
    db_conn.commit()
    db_conn.close()


def url(bucketlist_id=None, item_id=None):
    if bucketlist_id and item_id:
        return '/api/v1/bucketlists/{}/items/{}'.format(bucketlist_id, item_id)
    elif bucketlist_id:
        return '/api/v1/bucketlists/{}'.format(bucketlist_id)
    else:
        return '/api/v1/bucketlists/'
