import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "future"
)

mycursor = mydb.cursor()

query = "SELECT * FROM customers"
#query = "SELECT name, address FROM customers"
#query = "SELECT * FROM customers WHERE address ='Park Lane 38'"

#Select records where the address contains the word "way" using wildcard
#query = "SELECT * FROM customers WHERE address LIKE '%way%'"

#Select the 5 first records in the "customers" table
query = "SELECT * FROM customers LIMIT 5"

#Start from position 3, and return 5 records:
query = "SELECT * FROM customers LIMIT 5 OFFSET 2" 

#Prevents injection
#query = "SELECT * FROM customers WHERE address = %s"
value = ("Yellow Garden 2")

#query = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(query)
#mycursor.execute(query,value)

myresult = mycursor.fetchall() #Fetch all results
#myresult = mycursor.fetchone() #Fetch first row of result

for x in myresult:
  print(x)