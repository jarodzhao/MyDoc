"""
Usage:
"""
# -*- coding: utf-8 -*-

import pymysql

# 这样可以显示数据库中的中文字符了
db = pymysql.connect(host="127.0.0.1",user="root",password="root",database="abc",charset='utf8')

cursor = db.cursor()

cursor.execute("select * from t_book")

data = cursor.fetchall()

for row in data:
    print(row)
    


db.close()

