#coding=utf-8
import sys
import pymysql

db = pymysql.connect('localhost', 'root', 'root', 'xzjcy1023')

cursor = db.cursor()
# cursor.execute('SET NAMES UTF8')

cursor.execute("SELECT apply_user_name,apply_dept_name,sign_time,type FROM t_sign_record WHERE LEFT (sign_time,10) = CURDATE() ORDER BY sign_time DESC LIMIT 10")
# cursor.execute("SHOW variables like 'char%'")

db.close()

for result in cursor:
    print(result)

