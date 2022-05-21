import mysql.connector
from mysql.connector import Error

def insert_survey(data):
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='cordaid',
                                         user='cordaid',
                                         password='cordaid123')
        if connection.is_connected():
            mySql_insert_query = """INSERT INTO answers (facility_id,patient_id,first,second,third,fourth,fifth,sixth,extra_information) 
                           VALUES
                           (%s,%s,%s,%s,%s,%s,%s,%s,%s) """

            cursor = connection.cursor()
            cursor.execute(mySql_insert_query,data)
            connection.commit()
            cursor.close()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
