import mysql.connector as sql

global db_exists

he_db = sql.connect(host="localhost",user="root",passwd="rootLQSyM123987!")
he_cursor = he_db.cursor()
he_cursor.execute("SHOW DATABASES")
t_result = he_cursor.fetchall()

a = 'n'
b = 'n'

def chk_tbl(t_name):
	global table_exists
	he_cursor.execute("SHOW TABLES")
	t_result = he_cursor.fetchall()
	if len(t_result) == 0:
		table_exists = False
	else:
		for tbl in t_result:
			if tbl[0] == t_name:
				table_exists = True
				break
			else:
				table_exists = False

def crt_user():
	chk_tbl("he_users")
	if table_exists:
		print("Table already exists.")
	else:
		he_cursor.execute("CREATE TABLE he_users(user_id VARCHAR(15) PRIMARY KEY,email VARCHAR(255) UNIQUE NOT NULL,pass VARCHAR(30) NOT NULL,f_name VARCHAR(255) NOT NULL,l_name VARCHAR(255) NOT NULL,mob VARCHAR(10) NOT NULL UNIQUE,add1 VARCHAR(255) NOT NULL,add2 VARCHAR(255) NOT NULL,city VARCHAR(50) NOT NULL,state VARCHAR(50) NOT NULL,pin VARCHAR(6) NOT NULL,approved VARCHAR(1) DEFAULT 'n' NOT NULL,doj TIMESTAMP)")
		print("Table created Successfully.")
		he_db.commit()

def del_user():
	chk_tbl("he_users")
	if table_exists:
		he_cursor.execute("DROP TABLE he_users")
		print("Table deleted Successfully.")
		he_db.commit()
	else:
		print("Error!","Table does not exist.")

def crt_ord():
	chk_tbl("he_orders")
	if table_exists:
		print("Table already exists.")
	else:
		he_cursor.execute("CREATE TABLE he_orders(order_no int AUTO_INCREMENT PRIMARY KEY,user_id VARCHAR(15) UNIQUE NOT NULL,pay_id VARCHAR(20) NOT NULL,pay_msg VARCHAR(50) NOT NULL,inv_no VARCHAR(20) NOT NULL,status VARCHAR(255) NOT NULL,tracking_id VARCHAR(100) NOT NULL,doa TIMESTAMP)")
		he_cursor.execute("ALTER TABLE he_orders AUTO_INCREMENT=1000001")
		print("Table created Successfully.")
		he_db.commit()

def del_ord():
	chk_tbl("he_orders")
	if table_exists:
		he_cursor.execute("DROP TABLE he_orders")
		print("Table deleted Successfully.")
		he_db.commit()
	else:
		messagebox.showerror("Error!","Table does not exist.")

def crt_prod():
	chk_tbl("he_products")
	if table_exists:
		print("Table already exists.")
	else:
		he_cursor.execute("CREATE TABLE he_products(prod_id int(10) AUTO_INCREMENT PRIMARY KEY,prod_nm VARCHAR(255) UNIQUE NOT NULL,prod_categ VARCHAR(255) NOT NULL,prod_price DECIMAL(10,2) NOT NULL,prod_gst int(2) NOT NULL,prod_avail int(10) NOT NULL,prod_desc text NOT NULL,prod_icon VARCHAR(255) NOT NULL DEFAULT 'images/img_unav.jpeg',prod_img1 VARCHAR(255) NOT NULL DEFAULT 'images/img_unav.jpeg',prod_img2 VARCHAR(255) NOT NULL DEFAULT 'images/img_unav.jpeg',prod_img3 VARCHAR(255) NOT NULL DEFAULT 'images/img_unav.jpeg',doa TIMESTAMP)")
		he_cursor.execute("ALTER TABLE he_products AUTO_INCREMENT=10001")
		print("Table created Successfully.")
		he_db.commit()

def del_prod():
	chk_tbl("he_products")
	if table_exists:
		he_cursor.execute("DROP TABLE he_products")
		print("Table deleted Successfully.")
		he_db.commit()
	else:
		print("Table does not exist.")

for db in t_result:
	if db[0] == "hack_ele":
		db_exists = True
		print("Database exists.")
		a = input("Do you want to delete database? (y/n): ")
		break
	else:
		db_exists = False
if db_exists == False:
	print("Database does not exist.")
	b = input("Do you want to create database? (y/n): ")

if b == 'y':
	he_cursor.execute("CREATE DATABASE hack_ele")
	print("Database created. List of existing databases:")
	db_exists = True
	he_cursor.execute("SHOW DATABASES")
	for db in he_cursor:
		print(db[0])
elif a == 'y':
	he_cursor.execute("DROP DATABASE hack_ele")
	print("Database deleted. List of existing databases:")
	db_exists = False
	he_cursor.execute("SHOW DATABASES")
	for db in he_cursor:
		print(db[0])
elif b != 'n' or a != 'n':
	print("Invalid Command!")

if db_exists:
	he_db = sql.connect(host="localhost",user="root",passwd="rootLQSyM123987!",database="hack_ele")
	he_cursor = he_db.cursor()
	d = input("""1: Create he_users
2: Delete he_users
3: Create he_orders
4: Delete he_orders
5: Create he_products
6: Delete he_products
(Any key): Quit
Your ans: """)

	try:
		c = int(d)
	except:
		pass
	else:
		if c == 1:
			crt_user()
		elif c == 2:
			del_user()
		elif c == 3:
			crt_ord()
		elif c == 4:
			del_ord()
		elif c == 5:
			crt_prod()
		elif c == 6:
			del_prod()
