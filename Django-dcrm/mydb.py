import mysql.connector

dataBase=mysql.connector.connect(
	host='localhost',
	user='root',
	passwd='ritik'
)


cursorOb= dataBase.cursor()

cursorOb.execute("create database elderco")

print("All Done")