import csv
import logging
import Database.db_connect
import logs.logfile

def csv_to_db(Filename):
    # importing database connection from Database module
    con=Database.db_connect.db_con()
    # importing logging from logs module
    logs.logfile.log()
    cursor = con.cursor()
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
        con.commit()
        con.close()
file=input("Enter your file name or file path:")
csv_to_db(file)