# connectMySql.py
import pymysql.cursors
conn=pymysql.connect(host='127.0.0.1', port=3306, user='test', passwd='root', db='test')
cursor = conn.cursor()
cursor.execute('SELECT *FROM `t_user` WHERE t_id = 1')
cursor.fetchone() #获取第一行数据
conn.close() #关闭数据库

#另外一种方式:
#sql = 'SELECT *FROM `b_user` WHERE user_id = "%s"'
#data = (2011302577)
#cursor.execute(sql % data)