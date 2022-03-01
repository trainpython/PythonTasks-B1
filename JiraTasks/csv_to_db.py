import csv
import mysql.connector
import logging

def csv_to_db(Filename):
    logging.basicConfig(filename="logs.txt", level=logging.WARNING,
                        format='%(asctime)s:%(levelname)s:%(message)s:%(lineno)d', datefmt='%d/%m/%Y%I:%M:%S%p')
    conn = mysql.connector.connect(user='root', password='123456',
                                   host='localhost',
                                   database='py_db', port=3306)
    cursor = conn.cursor()
    # create_tb="create table Customers (Id int,Name varchar(255),MobileNo bigint,City varchar(255),email varchar(155));"
    # cursor.execute(create_tb)
    try:
        with open(Filename,'r') as f:
            r=csv.reader(f)
            data=list(r)
            all_values=[]
            for i in range(1,len(data)):
                all_values.append(data[i])
        query="insert into Customers(Id,Name,MobileNo,City,email) values(%s,%s,%s,%s,%s);"
        cursor.executemany(query,all_values)
    except FileNotFoundError as e:
        logging.error("File Not Found")
    except Exception as e:
        logging.error(e)
    finally:
        conn.commit()
        conn.close()
file=input("Enter your file name or file path:")
csv_to_db(file)