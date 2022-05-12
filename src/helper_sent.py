"""
Insert values into sent table
"""
from helper_sql import sqlExecute, sqlQuery


def insert(t):
    """Perform an insert into the `sent` table"""
    sqlExecute('''INSERT INTO sent VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', *t)

def delete(ack_data):
    """Perform delete ack data"""
    sqlExecute("DELETE FROM sent WHERE ackdata = ?", ack_data)

def retrieve_message_details(ack_data):
    """Retriving Message details"""
    data = sqlQuery(
        "select toaddress, fromaddress, subject, message, received from inbox where"
        " msgid = ?;", ack_data
    )
    return data
