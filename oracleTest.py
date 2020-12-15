import cx_Oracle


# [아이디]/[비밀번호]@[서버 주소]/[SID] 형태로 들어가야 합니다.
connection = cx_Oracle.connect("desr/desr@localhost/xe")

cursor = connection.cursor()


#query = ''' select date, name, content from sample_table where date between %s and %s ''' % (startDate, endDate)
query = 'select * from dessert'

# 실행을 시킵니다.
cursor.execute(query)
row = cursor.fetchone()
# 아래와 같이 차례대로 불러온 컬럼명르 잡아주게 되면 개별 변수에 차례대로 값이 들어가게 됩니다.
print(row)
connection.close()


