# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 17:08:53 2024

@author: mk9di
"""

import pyodbc

server = "(LocalDb)\MSSQLLocalDB"
database = "Books"
username = ""
password = ""
conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + server + 
                      ";DATABASE=" +database)

cursor = conn.cursor()

cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()