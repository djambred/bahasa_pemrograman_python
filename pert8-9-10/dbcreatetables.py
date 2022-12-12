import mysql.connector

mydb = mysql.connector.connect(
  host="172.25.147.253",
  port=23306,
  user="root",
  password="p455w0rd",
  database="sample"
)

db = mydb.cursor()

db.execute("CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), nim VARCHAR(255))")