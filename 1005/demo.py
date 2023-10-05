import pymysql

# 1. Connect
conn,cursor = None

try :
    conn = pymysql.connect(host='3.36.26.135', port=3306, user='root', password='pythonmysql')
# 2. Cursor
    cursor = conn.cursor()
# 3. SQL Statement
    sql = 'SELECT NOW()'
    cursor.execute(sql)
# 4. Fetch
    result = cursor.fetchone()
    print(result)
    
except Exception as err:
    print(err)
    
finally:
# 5. Close
    cursor.close()
    conn.close()