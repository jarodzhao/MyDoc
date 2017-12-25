"""
Usage:
"""

import pymysql

# 这样可以显示数据库中的中文字符了
db = pymysql.connect(host="127.0.0.1",user="root",password="root",database="xzjcy1207",charset='utf8')

cursor = db.cursor()

cursor.execute("select apply_dept_name,apply_user_name,sign_time,type,sign_flag"
               " from t_sign_record_late WHERE apply_user_name = '苏晓' order by attendance_date desc limit 10")

data = cursor.fetchall()

for row in data:    
    print(type(row))
    for it in row:
	  #缩进不一定要4个空格，但不能用 Tab 缩进
      print(it, end='')
      print(type(it), end='')
      print(it.find(':'))
    print()
db.close()

print(type(0))
print(type(2.3))
print(type('abc'))
