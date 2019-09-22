from DbConnection import mysql

class DbOperation(object):

	def InsertUser(username,password,email,contact):
		uid=0
		sql="INSERT INTO users (username,password,email,contact) VALUES(%s,%s,%s,%s)"
		data=(username,password,email,contact)
		con=mysql.connect()
		cursor=con.cursor()
		cursor.execute(sql,data)
		con.commit()
		cursor.close()
		print(cursor.lastrowid)
		uid=cursor.lastrowid
		#return cursor.lastrowid
		if uid>0:
			return True #data inserted successfully
		elif uid<0:
			return False #data insertion failed

	def UserExitOrNot(email):
		sql="SELECT id From users WHERE email=%s"
		data=(email)
		con=mysql.connect()
		cursor=con.cursor()
		cursor.execute(sql,data)
		con.commit()
		cursor.close()
		uid=cursor.fetchone()
		#return cursor.lastrowid
	
		return uid 
