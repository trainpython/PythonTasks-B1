import mysql.connector
def get_connection():
    conn=mysql.connector.connect(user='admin',password='admin123',host='python-db-b1.ck3etxnc3ebl.us-east-1.rds.amazonaws.com',

                             database='pythondb',port=3306)


    cursor=conn.cursor()
# querystring="create table emp_R(ename varchar2(20),joining_date date,email varchar2(20)"
# querystring1="insert into emp_R values('venkat',2022-3-2,'pvenkatakrishna16@gmail.com')"

    querystring1="select * from emp_R;"
# cursor.execute(querystring)
    cursor.execute(querystring1)
    records= cursor.fetchall()

    print("\nPrinting each row")
    print("\n")
    for row in records:
       return records
#cursor.executemany(querystring,values)
#conn.commit()
# print(conn)

    conn.close()
