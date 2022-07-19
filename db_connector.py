import mysql.connector
import config


mydb=mysql.connector.connect(
        host=config.db['host'],
        user=config.db['user'],
        password=config.db['password'],
        database=config.db['database']
)
mycursor = mydb.cursor()