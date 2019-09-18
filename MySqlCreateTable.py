import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "future"
)

mycursor = mydb.cursor()

#Creates table with a query statement
queryCreateNoPK = "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
queryCreatePK = "CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"
queryAlterPK = "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"

mycursor.execute(queryCreatePK)

#Check if table exists
queryCheck = "SHOW TABLES"
mycursor.execute(queryCheck)

for x in mycursor:
  print(x) 