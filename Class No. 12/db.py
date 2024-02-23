import mysql.connector

demo_db = mysql.connector.connect(
    host = "localhost"
    user ="root"
    password = ""
)
print(demo_db)