import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "future"
)

mycursor = mydb.cursor()
query = "INSERT INTO customers (name, address) VALUES (%s, %s)"

"""
#Inserts a single record in table with a query statement
value = ("John", "Highway 21")
mycursor.execute(query, value)
"""

"""
#Inserts multiple rows
values = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(query, values)
"""



#Insert single row test getting ID last insert
value = ("Michelle", "Blue Village")
mycursor.execute(query, value)
mydb.commit()

#Counts records inserted
#print(mycursor.rowcount, "record(s) inserted.")

#Get the ID of the last row inserted
print("1 record inserted, ID:", mycursor.lastrowid) 