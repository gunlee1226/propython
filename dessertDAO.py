import cx_Oracle

def insert(t):
    try:
        connection = cx_Oracle.connect("desr/desr@localhost:1521/xe")
    except Exception as err:
        print("Error while creating the connction", err)
    else:
        print(connection.version)
        try:
            cursor = connection.cursor()
            query = "INSERT INTO DESSERT " \
                    "values(seq_des_code.nextval,:1,:2, '댓글', :3,:4,:5,'링크1','링크2','링크3',:6)"
            cursor.execute(query,t)

        except Exception as err:
            print("Error while inserting the data ", err)
        else:
            print("insert Completed.")
            connection.commit()

    finally:
        cursor.close()
        connection.close()


def select():
    connection = cx_Oracle.connect("desr/desr@localhost:1521/xe")

    cursor = connection.cursor()

    query = """select * from dessert"""
    cursor.execute(query)
    row = cursor.fetchall()
    print(row)
    connection.close()
    for output in row:
        print(output)

def delete(d):
    try:
        connection = cx_Oracle.connect("desr/desr@localhost:1521/xe")
    except Exception as err:
        print("Error while creating the connction", err)
    else:
        print(connection.version)
        try:
            cursor = connection.cursor()
            query = "delete from DESSERT where DES_CODE =:1"
            cursor.execute(query,d)

        except Exception as err:
            print("Error while deleting the data ", err)
        else:
            print("Delete Completed.")
            connection.commit()

    finally:
        cursor.close()
        connection.close()

