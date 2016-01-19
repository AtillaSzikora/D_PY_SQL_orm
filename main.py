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

import mysql


