import mysql.connector

def db_con():

    # connection for cloud db
    conn = mysql.connector.connect(user='admin', password='admin123',
                                       host='python-db-b1.ck3etxnc3ebl.us-east-1.rds.amazonaws.com',
                                       database='pythondb', port=3306)
    return conn

    # connection for local db
    # conn = mysql.connector.connect(user='root', password='123456',
    #                                host='localhost',
    #                                database='py_db', port=3306)
    # return conn