import mysql.connector

db_config = {
    'host': 'db',
    'user': 'root',
    'password': input('enter your password: ')
}

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()


create_database_query = "CREATE DATABASE IF NOT EXISTS Working_database;"
cursor.execute(create_database_query)


cursor.close()
connection.close()
