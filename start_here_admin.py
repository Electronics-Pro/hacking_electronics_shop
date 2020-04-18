import tkinter.ttk as ttk
import mysql.connector as sql
import smtplib
import atexit
import os
from email.message import EmailMessage
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

#Environment variables
admin_user = os.environ.get('adminus')
admin_pass = os.environ.get('adminpa')
email_user = os.environ.get('mailus')
email_pass = os.environ.get('mailpa')
sql_pass = os.environ.get('mysqlpa')

#defining functions
def onExit():
    he_db.close()
    messagebox.showinfo("Thank you!","Database and program has been closed.")

def mainpage():
	global mainscrn
	mainscrn = Tk()
	mainscrn.grab_set()
	mainscrn.focus_force()
	mainscrn.geometry("640x360")
	mainscrn.resizable(0, 0)
	mainscrn.title("Hacking Electronics Shop")
	mainscrn.iconbitmap('images/icon.ico')
	frm1 = LabelFrame(mainscrn,text="Please login to continue.")
	lbl1 = Label(mainscrn,text="Welcome to Hacking Electronics Workshop",font=("Arial Bold",10))
	lbl3 = Label(frm1,text="UserID:")
	lbl4 = Label(frm1,text="Password:")
	but1 = Button(mainscrn,text="Login",command=lambda:login(usern.get(),passw.get()))
	usern = Entry(frm1,width=35)
	passw = Entry(frm1,show='*',width=35)
	bg_topl = ImageTk.PhotoImage(Image.open("images/top_bg.jpg"))
	bg_botl = ImageTk.PhotoImage(Image.open("images/bottom_bg.jpg"))
	bg_leftl = ImageTk.PhotoImage(Image.open("images/left_bg.jpg"))
	bg_rightl = ImageTk.PhotoImage(Image.open("images/right_bg.jpg"))
	lbl5 = Label(image=bg_topl)
	lbl6 = Label(image=bg_botl)
	lbl7 = Label(image=bg_leftl)
	lbl8 = Label(image=bg_rightl)

	frm1.grid(row=2,column=1)
	lbl1.grid(row=1,column=1)
	lbl3.grid(row=0,column=0,sticky=E)
	lbl4.grid(row=1,column=0,sticky=E)
	but1.grid(row=3,column=1)
	usern.grid(row=0,column=1)
	passw.grid(row=1,column=1)
	lbl5.grid(row=0,column=1)
	lbl6.grid(row=4,column=1)
	lbl7.grid(row=0,column=0,rowspan=5)
	lbl8.grid(row=0,column=2,rowspan=5)
	mainscrn.mainloop()

def send_email(msg):
	with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
		smtp.login(email_user,email_pass)
		smtp.send_message(msg)

def login(username,password):
	if username == admin_user and password == admin_pass:
		master_login()
	else:
		messagebox.showerror("Login Failed","Login Failed. Please check User ID and Password")

def master_login():
	global mainscrn
	mainscrn.destroy()
	mainscrn = Tk()
	mainscrn.grab_set()
	mainscrn.focus_force()
	mainscrn.title("Hacking Electronics Admin")
	mainscrn.iconbitmap('images/icon.ico')
	lbl1 = Label(mainscrn,text="Welcome Hacking Electronics Admin.",font=("Arial Bold",10))
	but1 = Button(mainscrn,text="Logout",command=master_logout)
	but2 = Button(mainscrn,text="Add Products",command=lambda:add_prod('',False))
	but3 = Button(mainscrn,text="Edit Products",command=edit_prod)
	but4 = Button(mainscrn,text="Approve/Reject Register Requests.",command=approv_reg)
	lbl1.grid(row=0,column=0,pady=5)
	but1.grid(row=1,column=0,pady=5)
	but2.grid(row=2,column=0,pady=5)
	but3.grid(row=3,column=0,pady=5)
	but4.grid(row=4,column=0,pady=5)
	mainscrn.mainloop()

def master_logout():
	global mainscrn
	mainscrn.destroy()
	mainpage()

def approv_reg():
	global mainscrn
	sql_query = "SELECT * FROM he_users WHERE approved = 'n'"
	he_cursor.execute(sql_query)
	app_result = he_cursor.fetchall()
	if len(app_result) == 0:
		messagebox.showinfo("No requests.","No requests yet.")
	else:
		mainscrn.destroy()
		mainscrn = Tk()
		mainscrn.grab_set()
		mainscrn.focus_force()
		mainscrn.title("Hacking Electronics Admin")
		mainscrn.iconbitmap('images/icon.ico')
		mainscrn.geometry("960x550")
		mainscrn.resizable(0, 0)

		frm1 = Frame(mainscrn)
		frm2 = Frame(mainscrn)
		scrollbarx = Scrollbar(frm1,orient = HORIZONTAL)
		scrollbary = Scrollbar(frm1,orient = VERTICAL)
		tree = ttk.Treeview(frm1,columns = ("uid","email","fname","lname","mob","add1","add2","city","state","pin","doj"),height = 20,selectmode = "extended",yscrollcommand = scrollbary.set,xscrollcommand = scrollbarx.set)
		scrollbary.config(command = tree.yview)
		scrollbary.pack(side = RIGHT,fill = Y)
		scrollbarx.config(command = tree.xview)
		scrollbarx.pack(side = BOTTOM,fill = X)
		tree.heading("#0",text="Sr. No.",anchor = W)
		tree.heading("uid",text="User ID",anchor = W)
		tree.heading("email",text="Email",anchor = W)
		tree.heading("fname",text="First Name",anchor = W)
		tree.heading("lname",text="Last Name",anchor = W)
		tree.heading("mob",text="Mobile",anchor = W)
		tree.heading("add1",text="Address Line 1",anchor = W)
		tree.heading("add2",text="Address Line 2",anchor = W)
		tree.heading("city",text="City",anchor = W)
		tree.heading("state",text="State",anchor = W)
		tree.heading("pin",text="Pin",anchor = W)
		tree.heading("doj",text="Date of Registration",anchor = W)
		tree.column("#0",stretch = NO,minwidth = 10, width=50)
		tree.column("uid",stretch = NO,minwidth = 10, width=100)
		tree.column("email",stretch = NO,minwidth = 10, width=150)
		tree.column("fname",stretch = NO,minwidth = 10, width=100)
		tree.column("lname",stretch = NO,minwidth = 10, width=100)
		tree.column("mob",stretch = NO,minwidth = 10, width=80)
		tree.column("add1",stretch = NO,minwidth = 10, width=200)
		tree.column("add2",stretch = NO,minwidth = 10, width=200)
		tree.column("city",stretch = NO,minwidth = 10, width=100)
		tree.column("state",stretch = NO,minwidth = 10, width=100)
		tree.column("pin",stretch = NO,minwidth = 10, width=50)
		tree.column("doj",stretch = NO,minwidth = 10, width=125)
		tree.pack()

		for qur_res in app_result:
			tree.insert('','end',values=(qur_res[0],qur_res[1],qur_res[3],qur_res[4],qur_res[5],qur_res[6],qur_res[7],qur_res[8],qur_res[9],qur_res[10],qur_res[12]))

		bg_approv_left = ImageTk.PhotoImage(Image.open("images/approv_bg1.jpg"))
		bg_approv_right = ImageTk.PhotoImage(Image.open("images/approv_bg2.jpg"))
		lbl1 = Label(frm2,text="Select a user and then click approve/reject:")
		lbl2 = Label(frm2,image=bg_approv_left)
		lbl3 = Label(frm2,image=bg_approv_right)
		ent1 = Entry(frm2,width=10)
		but1 = Button(frm2,text="Approve",command=lambda:ar_user(True,tree))
		but2 = Button(frm2,text="Reject",command=lambda:ar_user(False,tree))
		but3 = Button(frm2,text="Return",command=master_login)
		lbl1.grid(row=0,column=1,columnspan=2,pady=5)
		but1.grid(row=1,column=1,padx=5,pady=5)
		but2.grid(row=1,column=2)
		but3.grid(row=2,column=1,pady=5,padx=10,ipadx=92,columnspan=2)
		lbl2.grid(row=0,column=0,rowspan=3)
		lbl3.grid(row=0,column=4,rowspan=3)
		frm1.pack()
		frm2.place(x=-2,y=442)
		mainscrn.mainloop()

def ar_user(aok,tree):
	edit_user = tree.item(tree.focus())['values'][0]
	if aok:
		approv_ok(edit_user)
	else:
		approv_nok(edit_user)

def approv_ok(uid):
	sql_query = "UPDATE he_users SET approved = 'y' WHERE user_id = '{}'".format(uid)
	he_cursor.execute(sql_query)
	he_db.commit()
	messagebox.showinfo("Approval Success","User has been approved.")
	approv_reg()

def approv_nok(uid):
	sql_query = "UPDATE he_users SET approved = 'r' WHERE user_id = '{}'".format(uid)
	he_cursor.execute(sql_query)
	he_db.commit()
	messagebox.showinfo("Approval Rejected","User has been rejected.")
	approv_reg()

def add_prod(edit_item,editing):
	global mainscrn
	mainscrn.destroy()
	mainscrn = Tk()
	mainscrn.grab_set()
	mainscrn.focus_force()
	mainscrn.resizable(0, 0)
	mainscrn.title("Register to Hacking Electronics Shop")
	mainscrn.iconbitmap('images/icon.ico')
	
	frm2 = LabelFrame(mainscrn)
	lbl7 = Label(mainscrn,text="Please enter your product details",font=("Arial Bold",10))
	lbl8 = Label(frm2,text="Name:")
	lbl9 = Label(frm2,text="Category:")
	lbl10 = Label(frm2,text="Price:")
	lbl11 = Label(frm2,text="GST rate:")
	lbl12 = Label(frm2,text="Availability:")
	lbl13 = Label(frm2,text="Description:")
	lbl14 = Label(frm2,text="Icon filename:")
	lbl15 = Label(frm2,text="Img1 filename:")
	lbl16 = Label(frm2,text="Img2 filename:")
	lbl17 = Label(frm2,text="Img3 filename:")
	frm2.grid(row=1,column=0,columnspan=3,padx=4)
	lbl7.grid(row=0,column=0,columnspan=3)
	lbl8.grid(row=0,column=0,sticky=E)
	lbl9.grid(row=1,column=0,sticky=E)
	lbl10.grid(row=2,column=0,sticky=E)
	lbl11.grid(row=3,column=0,sticky=E)
	lbl12.grid(row=4,column=0,sticky=E)
	lbl14.grid(row=5,column=0,sticky=E)
	lbl15.grid(row=6,column=0,sticky=E)
	lbl16.grid(row=7,column=0,sticky=E)
	lbl17.grid(row=8,column=0,sticky=E)
	lbl13.grid(row=9,column=0,sticky=NE)

	global namer
	global categ
	global pricr
	global gstrr
	global avair
	global descr
	global iconr
	global img1r
	global img2r
	global img3r	
	
	namer = Entry(frm2,width=60)
	pricr = Entry(frm2,width=10)
	gstrr = Entry(frm2,width=10)
	avair = Entry(frm2,width=10)
	iconr = Entry(frm2,width=60)
	img1r = Entry(frm2,width=60)
	img2r = Entry(frm2,width=60)
	img3r = Entry(frm2,width=60)
	descr = Text(frm2,height=10,width=45)

	categ = StringVar()

	if editing:
		sql_query = "SELECT * FROM he_products where prod_id = '{}'".format(edit_item)
		he_cursor.execute(sql_query)
		edit_result = he_cursor.fetchall()
		categ.set(edit_result[0][2])
		namer.insert(0,edit_result[0][1])
		pricr.insert(0,edit_result[0][3])
		gstrr.insert(0,edit_result[0][4])
		avair.insert(0,edit_result[0][5])
		iconr.insert(0,edit_result[0][7])
		img1r.insert(0,edit_result[0][8])
		img2r.insert(0,edit_result[0][9])
		img3r.insert(0,edit_result[0][10])
		descr.insert('1.0',edit_result[0][6])
	else:
		categ.set("Select Category")
		iconr.insert(0,"images/product_images/img_unav.jpeg")
		img1r.insert(0,"images/product_images/img_unav.jpeg")
		img2r.insert(0,"images/product_images/img_unav.jpeg")
		img3r.insert(0,"images/product_images/img_unav.jpeg")
		descr.insert('1.0',"No description yet.")

	categs = ["Beginner Kits","Drone Parts","EBike Parts","3D Printer Parts","Batteries","Motors, Drivers, Actuators",
	"Development Boards","Arduino","Raspberry Pi","Sensors","IoT and Wireless","Electronic Modules",
	"Electronic Components","Wires and Cables","Instruments and Tools","Mechanical Parts"]
	cater = OptionMenu(frm2,categ,*categs)
	
	namer.grid(row=0,column=1)
	cater.grid(row=1,column=1,sticky=W)
	pricr.grid(row=2,column=1,sticky=W)
	gstrr.grid(row=3,column=1,sticky=W)
	avair.grid(row=4,column=1,sticky=W)
	iconr.grid(row=5,column=1)
	img1r.grid(row=6,column=1)
	img2r.grid(row=7,column=1)
	img3r.grid(row=8,column=1)
	descr.grid(row=9,column=1,ipady=35)

	but5 = Button(mainscrn,text="Clear",command=prod_clr)
	but6 = Button(mainscrn,text="Cancel",command=master_login)
	but7 = Button(mainscrn,text="Add",command=lambda:prod_add(edit_item,editing))
	but5.grid(row=2,column=0,pady=5)
	but6.grid(row=2,column=1,pady=5)
	but7.grid(row=2,column=2,pady=5)

	mainscrn.mainloop()

def prod_clr():
	namer.delete(0,END)
	pricr.delete(0,END)
	gstrr.delete(0,END)
	avair.delete(0,END)
	descr.delete('1.0',END)
	iconr.delete(0,END)
	img1r.delete(0,END)
	img2r.delete(0,END)
	img3r.delete(0,END)
	iconr.insert(0,"images/product_images/img_unav.jpeg")
	img1r.insert(0,"images/product_images/img_unav.jpeg")
	img2r.insert(0,"images/product_images/img_unav.jpeg")
	img3r.insert(0,"images/product_images/img_unav.jpeg")
	descr.insert('1.0',"No description yet.")
	categ.set("Select Category")

def prod_add(edit_item,editing):
	add_prob = False
	if len(namer.get()) == 0 or len(namer.get()) > 255:
		messagebox.showerror("Add product failed","Product name should have less than 255 characters OR No name entered.")
		add_prob = True
	if len(pricr.get()) == 0 or len(pricr.get()) > 9:
		messagebox.showerror("Add product failed","Price should be less than 10 characters OR No price entered.")
		add_prob = True
	if len(gstrr.get()) == 0 or len(gstrr.get()) > 2:
		messagebox.showerror("Add product failed","GST should be less than 3 characters OR No GST entered.")
		add_prob = True
	if len(avair.get()) == 0 or len(avair.get()) > 9:
		messagebox.showerror("Add product failed","Availability should be less than 10 characters OR No availability of product entered.")
		add_prob = True
	if len(descr.get('1.0',END)) == 0 or len(descr.get('1.0',END)) > 65535:
		messagebox.showerror("Add product failed","Description should be less than 65536 characters OR No description of product entered.")
		add_prob = True
	if categ.get() == "Select Category":
		messagebox.showerror("Add product failed","Please specify category.")
		add_prob = True
	try:
		float(pricr.get())
		float(gstrr.get())
		int(avair.get())
		price = ((float(pricr.get())*100)//100)
	except:
		messagebox.showerror("Add product failed","Please check if price, GST are float, availability integer.")
	else:
		try:
			Image.open(iconr.get())
			Image.open(img1r.get())
			Image.open(img2r.get())
			Image.open(img3r.get())
		except:
			messagebox.showerror("Add product failed","Check location of image")
		else:
			if editing and not add_prob:
				sql_query = "UPDATE he_products SET prod_nm = '{}',prod_categ = '{}',prod_price = {},prod_gst = {},prod_avail = {},prod_desc = '{}',prod_icon = '{}',prod_img1 = '{}',prod_img2 = '{}',prod_img3 = '{}' WHERE prod_id = {}".format(namer.get(),categ.get(),price,gstrr.get(),avair.get(),descr.get('1.0',END),iconr.get(),img1r.get(),img2r.get(),img3r.get(),edit_item)
				try:
					he_cursor.execute(sql_query)
				except:
					messagebox.showerror("Edit product failed. Please give a unique name/same name as before.")
				else:
					he_db.commit()
					editing = False
					messagebox.showinfo("Success","Product edited successfully.")
					master_login()
			else:
				sql_query = "SELECT prod_nm FROM he_products"
				he_cursor.execute(sql_query)
				result = he_cursor.fetchall()
				for query_result in result:
					if namer.get() == query_result[0]:
						messagebox.showerror("Add product failed","Please give unique name to product.")
						add_prob = True
						break
				if not add_prob:
					sql_query = "INSERT INTO he_products(prod_nm,prod_categ,prod_price,prod_gst,prod_avail,prod_desc,prod_icon,prod_img1,prod_img2,prod_img3) VALUES('{}','{}',{},{},{},'{}','{}','{}','{}','{}')".format(namer.get(),categ.get(),price,gstrr.get(),avair.get(),descr.get('1.0',END),iconr.get(),img1r.get(),img2r.get(),img3r.get())
					he_cursor.execute(sql_query)
					he_db.commit()
					messagebox.showinfo("Success","Product added successfully.")
					master_login()

def edit_prod():
	global mainscrn
	sql_query = "SELECT * FROM he_products"
	he_cursor.execute(sql_query)
	edit_result = he_cursor.fetchall()
	if len(edit_result) == 0:
		messagebox.showinfo("No Products","No products added yet!")
		master_login()
	else:
		mainscrn.destroy()
		mainscrn = Tk()
		mainscrn.grab_set()
		mainscrn.focus_force()
		mainscrn.title("Hacking Electronics Admin")
		mainscrn.iconbitmap('images/icon.ico')
		mainscrn.geometry("720x405")
		mainscrn.resizable(0, 0)

		frm1 = Frame(mainscrn)
		scrollbarx = Scrollbar(frm1,orient = HORIZONTAL)
		scrollbary = Scrollbar(frm1,orient = VERTICAL)
		tree = ttk.Treeview(frm1,columns = ("prod_nm","prod_categ","prod_price","prod_gst","prod_avail","prod_desc","prod_icon","prod_img1","prod_img2","prod_img3","doa"),height = 12,selectmode = "extended",yscrollcommand = scrollbary.set,xscrollcommand = scrollbarx.set)
		scrollbary.config(command = tree.yview)
		scrollbary.pack(side = RIGHT,fill = Y)
		scrollbarx.config(command = tree.xview)
		scrollbarx.pack(side = BOTTOM,fill = X)
		tree.heading("#0",text="Prod ID",anchor = W)
		tree.heading("prod_nm",text="Prod Name",anchor = W)
		tree.heading("prod_categ",text="Category",anchor = W)
		tree.heading("prod_price",text="Price",anchor = W)
		tree.heading("prod_gst",text="GST",anchor = W)
		tree.heading("prod_avail",text="Availability",anchor = W)
		tree.heading("prod_desc",text="Description",anchor = W)
		tree.heading("prod_icon",text="Icon loc",anchor = W)
		tree.heading("prod_img1",text="Image loc 1",anchor = W)
		tree.heading("prod_img2",text="Image loc 2",anchor = W)
		tree.heading("prod_img3",text="Image loc 3",anchor = W)
		tree.heading("doa",text="Date of Addition",anchor = W)
		tree.column("#0",stretch = NO,minwidth = 10, width=50)
		tree.column("prod_nm",stretch = NO,minwidth = 10, width=100)
		tree.column("prod_categ",stretch = NO,minwidth = 10, width=100)
		tree.column("prod_price",stretch = NO,minwidth = 10, width=50)
		tree.column("prod_gst",stretch = NO,minwidth = 10, width=50)
		tree.column("prod_avail",stretch = NO,minwidth = 10, width=50)
		tree.column("prod_desc",stretch = NO,minwidth = 10, width=200)
		tree.column("prod_icon",stretch = NO,minwidth = 10, width=150)
		tree.column("prod_img1",stretch = NO,minwidth = 10, width=150)
		tree.column("prod_img2",stretch = NO,minwidth = 10, width=150)
		tree.column("prod_img3",stretch = NO,minwidth = 10, width=150)
		tree.column("doa",stretch = NO,minwidth = 10, width=125)
		tree.pack()
		for qur_res in edit_result:
			tree.insert('','end',text=qur_res[0],values=(qur_res[1],qur_res[2],qur_res[3],qur_res[4],qur_res[5],qur_res[6],qur_res[7],qur_res[8],qur_res[9],qur_res[10],qur_res[11]))

		lbl1 = Label(mainscrn,text="Select product to edit and click Edit:")
		but1 = Button(mainscrn,text="Edit",command=lambda:edItem(tree))
		but2 = Button(mainscrn,text="Exit",command=master_login)
		lbl1.pack(pady=5)
		frm1.pack(pady=5)
		but1.pack(ipadx=100,pady=5)
		but2.pack(ipadx=100,pady=5)
		mainscrn.mainloop()

def edItem(tree):
	selItem1 = tree.focus()
	selItem = tree.item(selItem1)
	edit_item = selItem['text']
	add_prod(edit_item,True)

#Check if db and tables are present and continue
try:
	he_db = sql.connect(host="localhost",user="root",passwd=sql_pass,database="hack_ele")
	he_cursor = he_db.cursor(buffered=True)
except:
	messagebox.showerror("Application failed","Application failed to load. Error Code: no_db")
else:
	sql_query = "SHOW TABLES"
	he_cursor.execute(sql_query)
	query_result = he_cursor.fetchall()
	for qur in query_result:
		if qur[0] == "he_users":
			noprob1 = True
			break
		else:
			noprob1 = False
	for qur in query_result:
		if qur[0] == "he_products":
			noprob2 = True
			break
		else:
			noprob2 = False
	for qur in query_result:
		if qur[0] == "he_orders":
			noprob3 = True
			break
		else:
			noprob3 = False
	if noprob1 and noprob2 and noprob3:
		#Main window:
		mainpage()
	else:
		messagebox.showerror("Application failed","Application failed to load. Error Code: no_tbl")

atexit.register(onExit)
