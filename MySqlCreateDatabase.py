import mysql.connector

dbCredentials = []

#Connects to the database
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = ""
)

#Creates database called 'Future'
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Future")

#Check if database exists
mycursor.execute("SHOW DATABASES")

#Print how many databases are in my localhost server
for x in mycursor:
    print(x)