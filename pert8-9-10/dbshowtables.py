import mysql.connector

mydb = mysql.connector.connect(
  host="172.31.192.23",
  port=23306,
  user="root",
  password="p455w0rd",
  database="basis_data"
)

db = mydb.cursor()

db.execute("SHOW TABLES")

for x in db:
  print(x)