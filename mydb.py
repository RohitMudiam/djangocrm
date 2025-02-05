import mysql.connector

# Connect to MySQL with the authentication plugin explicitly set
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root@123',
    auth_plugin='mysql_native_password'
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE crmdatabase")
print("All Done!")
