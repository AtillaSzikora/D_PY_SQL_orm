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


def sql_to_csv():
	with open("new_order_details.csv", "w") as new_order_details:
		new_order_details.write("OrderID;ProductID;UnitPrice;Quantity;Discount" + "\n")
	with open("new_order_details.csv", "a") as new_order_details:
		sql_cmd = "SELECT * FROM orderdetails"
		cursor.execute(sql_cmd)
		sql_lst = cursor.fetchall()
		for i in sql_lst:
			sql_tpls = i
			joined_str = ""
			for j in sql_tpls:
				joined_str += str(int(j)) + ";"
			new_order_details.write(joined_str[:(len(joined_str)-1)] + "\n")


def csv_to_sql():
	with open("order_details.csv", "r") as order_details:
		csv_row = order_details.readline()
		for i in range(100):
			csv_row = order_details.readline().split(";")
			joined_str = ", ".join(csv_row).strip("\n")
			sql_cmd = "INSERT INTO orderdetails VALUES(" + joined_str + ");"
			cursor.execute(sql_cmd)
			database_connector.commit()
