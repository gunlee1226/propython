import cx_Oracle

def insert():

    connection = cx_Oracle.connect("desr/desr@localhost/xe")

    cursor = connection.cursor()

    query = "INSERT INTO DESSERT values(seq_des_code.nextval,:1,:2, '댓글','사진', '재료',:3,'링크1','링크2','링크3');"
    cursor.execute(query, t)
    cursor.close()
    row = cursor.fetchone()
    connection.commit()
    connection.close()



