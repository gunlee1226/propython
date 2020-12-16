import cx_Oracle

def insert(t):

    try:
        connection = cx_Oracle.connect("desr/desr@localhost/xe")
    except Exception as err:
        print("Error while creating the connction", err)
    else:
        print(connection.version)
        try:
            cursor = connection.cursor()
            query = """INSERT INTO kinds values (:1,:2,:3,:4)"""
            cursor.execute(query,t)
            row = cursor.fetchone()
            print(row)
        except Exception as err:
            print("Error while inserting the data ", err)
        else:
            print("insert Completed.")
            connection.commit
    finally:
        cursor.close()
        connection.close()


def select():
    connection = cx_Oracle.connect("desr/desr@localhost/xe")

    cursor = connection.cursor()

    query = "select * from DESSERT"
    cursor.execute(query)
    row = cursor.fetchone()
    print(row)
    connection.commit()
    connection.close()








