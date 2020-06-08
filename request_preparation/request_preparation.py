'''
Extract the last row from the MySQL DB and store it in a local csv file
as : (org, s, o, a, c)
'''
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import csv
from get_access import *


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='caraccess_db',
                                         user='root',
                                         password='')

    sql_select_Query = "SELECT * FROM requests_db ORDER BY id DESC LIMIT 1"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in requests_db is: ", cursor.rowcount)

    print("\nPrinting each record")
    for row in records:
        print("Id = ", row[0])
        print("Car = ", row[1])
        print("From date  = ", row[2])
        print("To date  = ", row[3])
        print("Cin  = ", row[4])
        print("num_days  = ", (datetime.strptime(row[3], "%Y-%m-%d")-datetime.strptime(row[2], "%Y-%m-%d")).days)
        print("Organization  = ", row[5], "\n")
        fields=[row[0], row[5], row[4], row[1], (datetime.strptime(row[3], "%Y-%m-%d")-datetime.strptime(row[2], "%Y-%m-%d")).days, row[2], row[3]]
        # save fields in request.csv file
        with open(r'request.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
            get_axx(fields)

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
