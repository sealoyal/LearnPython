import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "future"
)

mycursor = mydb.cursor()

#Inserts records in table with a query statement
query = "DELETE FROM customers"
where = " WHERE address = 'Mountain 21'"
mycursor.execute(query)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")