import mysql.connector

mydb = mysql.connector.connect(
  host="172.31.192.23",
  port=23306,
  user="root",
  password="p455w0rd",
)

db = mydb.cursor()
db.execute("CREATE DATABASE basis_data")