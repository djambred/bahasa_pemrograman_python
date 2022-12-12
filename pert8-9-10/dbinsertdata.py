import mysql.connector

mydb = mysql.connector.connect(
  host="172.31.192.23",
  port=23306,
  user="root",
  password="p455w0rd",
  database="basis_data"
)

db = mydb.cursor()

sql = "INSERT INTO students (name, nim) VALUES (%s, %s)"
val = ("John", "1234567890")
db.execute(sql, val)
mydb.commit()

print(db.rowcount, "berhasil insert")