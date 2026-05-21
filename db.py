import mariadb

def get_connection():
    conn = mariadb.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="JimlethDB"
    )
    return conn
