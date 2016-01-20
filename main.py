"""
Create a python application which can import data from a CSV file,
parses the containing data to objects and stores the data in MySQL database.
The application has to be able to export data from database to CSV file.
The application uses the previously created Northwind DB. Import and export functions are limited to use these tables:
Employees, Customers, Orders and OrderDetails so you don't need to create a class for every tables in the DB!
All of the classes should contain a static parse() method which require a string as a parameter (CSV row)
and creates (and returns) an object from it.
The classes should contain a persist() method (procedure) with no parameter.
Define a to_csv() method which returns a string representation of the current object
which can be written out as a CSV row.
"""

import mysql.connector
mitnezel = open('mitnezel.txt', 'r').read()

database_connector = mysql.connector.connect(user='root', password=mitnezel, host='127.0.0.1', db='northwind')
cursor = database_connector.cursor()


def csvtosql():
	with open("order_details.csv", "r") as order_details:
		splitted_str = order_details.readline().split(";")
		splitted_str = order_details.readline().split(";")
		joined_str = ", ".join(splitted_str).strip("\n")
		sql_str = "INSERT INTO orderdetails VALUES(" + joined_str + ");"
		cursor.execute(sql_str)
		database_connector.commit()


def sqltocsv():
	with open("new_order_details.csv", "w") as new_order_details:
		sql_str = "SELECT * FROM orderdetails LIMIT 1;"
		cursor.execute(sql_str)
		csv_str = (cursor.fetchall())[0]
		joined_str = ""
		for i in csv_str:
			joined_str += str(int(i)) + ";"
		print(joined_str)

sqltocsv()
