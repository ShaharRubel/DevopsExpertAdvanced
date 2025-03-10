import pymysql
import datetime

def connect_db():
    """Connect to remote DB named DevopsExperts as per the documentation of aiven
    https://console.aiven.io/account/a51aa96da1f1/project/devopsexperts/services/mysql-23b9542e/overview
    """
    try:
        connection = 0
        timeout = 10
        connection = pymysql.connect(
            charset="utf8mb4",
            connect_timeout=timeout,
            cursorclass=pymysql.cursors.DictCursor,
            db="DevopsExperts",
            host="mysql-23b9542e-devopsexperts.c.aivencloud.com",
            password="AVNS_WEPQrf0gLBZxdjuphDx",
            read_timeout=timeout,
            port=26733,
            user="avnadmin",
            write_timeout=timeout,
        )
        return connection
    except Exception as e:
        print(e)

def create_table():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE users (user_id int PRIMARY KEY, user_name varchar(50), creation_date varchar(50));")
    connection.commit()
    connection.close( )




if __name__ == '__main__':
    connection = connect_db()
    cursor = connection.cursor()
    # cursor.execute("SELECT * FROM DevopsExperts.users;")
    # cursor.execute("DELETE FROM DevopsExperts.users WHERE user_id =1")
    # connection.commit()
    create_table()
    cursor.execute("SHOW TABLES")
    print(cursor.fetchall())



    connection.close()