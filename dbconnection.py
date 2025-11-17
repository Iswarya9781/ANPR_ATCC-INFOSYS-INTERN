# dbconnection.py
import pymysql

def get_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='IsWarya@7811',
        database='mydb'
    )
    return conn