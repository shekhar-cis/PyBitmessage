"""
Insert values into sent table
"""
from helper_sql import sqlExecute


def insert(t):
    """Perform an insert into the `sent` table"""
    sqlExecute('''INSERT INTO sent VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', *t)

def delete(data_index):
    sqlExecute("DELETE FROM sent WHERE ackdata = ?", data_index)