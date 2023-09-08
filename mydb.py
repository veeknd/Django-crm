import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Doforit16'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE Drogon")

print("all done")