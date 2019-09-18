import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "future"
)

mycursor = mydb.cursor()

queryDrop = "DROP TABLE customers"
queryDropIfExists = "DROP TABLE IF EXISTS customers"
mycursor.execute(queryDrop)