import pymysql

host = '3.36.26.135'
port = 3306
user = 'root'
password = 'pythonmysql'
database = 'mycompany'
conn = pymysql.connect(port=port, user=user, host=host, password=password, database=database)

cursor = conn.cursor()

sql = "SELECT EMPNO< ENAME, JOB, SAL, DEPTNO FROM EMP WHERE DEPTNO = 20"
cursor.execute(sql)
result = cursor.fetchall()
for emp in result :
    print(emp[1], emp[3], sep=',\t')

cursor.close()
conn.close()