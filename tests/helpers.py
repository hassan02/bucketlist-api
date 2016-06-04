import sqlite3
import os

def setupDatabase():
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    database_name = os.path.join(BASEDIR, 'bucketlist_test.sqlite')
    db_conn = sqlite3.connect(database_name)
    db_cursor = db_conn.cursor()
    db_cursor.execute('DELETE FROM user')
    db_cursor.execute('DELETE FROM bucket_list')
    db_cursor.execute('DELETE FROM bucket_list_item')
    db_conn.commit()
    db_conn.close()
    
