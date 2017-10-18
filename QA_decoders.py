#author  = Natesh M Bhat
#python version = 3.4
def connect():

	import pymysql

	try:
		con = pymysql.connect(host='localhost',
		                             user='user',
		                             password='passwd',
		                             db='db',
		                             charset='utf8mb4',
		                             cursorclass=pymysql.cursors.DictCursor) ; 
		cur = con.cursor() ;

		command = "" ;

		cur.execute(command) ;

		con.commit() ;
		
	finally:
		con.close() ;



if(__name__ =='__main__'):
	connect() ;
