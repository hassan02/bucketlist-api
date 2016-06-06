import sqlite3
import os

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

def removeDbFile():
    if os.path.exists(database_name):
      os.remove(database_name)
