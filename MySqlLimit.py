import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "future"
)

mycursor = mydb.cursor()

#query = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
query = "UPDATE customers SET address = %s WHERE address = %s"
value = ("Canyon 123", "Valley 345")

#mycursor.execute(query)
mycursor.execute(query,value)

mydb.commit()

print(mycursor.rowcount, "record(s) affected") 