import cx_Oracle


connection = cx_Oracle.connect("desr/desr@localhost:1521/xe")

cursor = connection.cursor()

query = """select * from dessert order by des_code asc"""
cursor.execute(query)
row = cursor.fetchall()

for output in row:
    print(output)
connection.close()

